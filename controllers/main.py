# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging
import jwt
import datetime
import requests
import uuid

_logger = logging.getLogger(__name__)

class WeChatLogin(http.Controller):

    @http.route('/wechat/miniapp/login', type='json', auth='public', csrf=False, methods=['POST'], cors='*')
    def wechat_login(self, **kw):
        """
        微信小程序登录接口
        请求参数：
            - code: 微信登录凭证
        返回：
            - code: 状态码（200 成功）
            - token: JWT 登录令牌
            - partner_id: 用户ID
            - name: 用户名
        """

        code = kw.get('code')
        if not code:
            return {
                'code': 400,
                'message': '缺少微信登录凭证 (code)',
            }

        appid = request.env['ir.config_parameter'].sudo().get_param('wechat.appid')
        secret = request.env['ir.config_parameter'].sudo().get_param('wechat.secret')
        jwt_secret = request.env['ir.config_parameter'].sudo().get_param('wechat.jwt_secret')

        if not appid or not secret:
            return {
                'code': 500,
                'message': '服务器未正确配置，请在Odoo后台设置微信AppID和Secret',
            }

        if not jwt_secret:
            jwt_secret = str(uuid.uuid4())
            request.env['ir.config_parameter'].sudo().set_param('wechat.jwt_secret', jwt_secret)

        wx_url = f'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code'
        try:
            response = requests.get(wx_url, timeout=10)
            wx_data = response.json()
        except Exception as e:
            _logger.error("请求微信服务器失败: %s", str(e))
            return {
                'code': 503,
                'message': '无法连接微信服务器，请稍后再试',
            }

        if 'errcode' in wx_data and wx_data['errcode'] != 0:
            _logger.warning("微信登录凭证错误或过期: %s", wx_data.get('errmsg'))
            return {
                'code': 401,
                'message': '微信登录凭证无效，请重新登录',
            }

        openid = wx_data.get('openid')
        session_key = wx_data.get('session_key')

        if not openid:
            return {
                'code': 500,
                'message': '未能获取用户OpenID，请重试',
            }

        Partner = request.env['res.partner'].sudo()
        partner = Partner.search([('wechat_openid', '=', openid)], limit=1)

        if not partner:
            try:
                partner = Partner.create({
                    'name': f'WeChat用户_{openid[-6:]}',
                    'wechat_openid': openid,
                    'is_company': False,
                    'customer_rank': 1,
                    'active': True,
                })
                _logger.info("新用户已创建，OpenID: %s", openid)
            except Exception as e:
                _logger.error("创建用户失败: %s", str(e))
                return {
                    'code': 500,
                    'message': '内部错误：无法创建用户，请联系管理员',
                }

        try:
            payload = {
                'partner_id': partner.id,
                'openid': openid,
                'session_key': session_key,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
                'iat': datetime.datetime.utcnow(),
            }
            token = jwt.encode(payload, jwt_secret, algorithm='HS256')
        except Exception as e:
            _logger.error("JWT 生成失败: %s", str(e))
            return {
                'code': 500,
                'message': '内部错误：Token生成失败',
            }

        return {
            'code': 200,
            'token': token,
            'partner_id': partner.id,
            'name': partner.name,
            'message': '登录成功',
        }