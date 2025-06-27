# 微信配置设置界面（系统参数）
from odoo import models, fields

class WeChatConfigSettings(models.TransientModel):
    _name = 'wechat.config.settings'
    _description = 'WeChat 配置设置'
    _inherit = 'res.config.settings'

    wechat_appid = fields.Char(
        string='微信小程序 AppID',
        config_parameter='wechat.appid',
        groups='base.group_system'
    )
    wechat_secret = fields.Char(
        string='微信小程序 Secret',
        config_parameter='wechat.secret',
        groups='base.group_system'
    )
    jwt_secret = fields.Char(
        string='JWT 密钥',
        config_parameter='wechat.jwt_secret',
        groups='base.group_system'
    )