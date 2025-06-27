{
    'name': 'WeChat MiniProgram Login (UniApp)',
    'version': '1.0',
    'summary': '支持UniApp微信小程序登录的Odoo模块（含后台配置）',
    'description': '提供UniApp微信小程序用户登录、注册、Token验证，并支持在Odoo后台配置appid和secret',
    'category': 'Website',
    'author': 'Your Company',
    'depends': ['base', 'web', 'contacts', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_views.xml',
    ],
    'models': [
        'models/wechat_config_settings.py',
    ],
    'controllers': [
        'controllers/main.py',
    ],
    'installable': True,
    'application': False,
}