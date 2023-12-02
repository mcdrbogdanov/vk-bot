import os

from dotenv import load_dotenv
from vkbottle import Bot, CtxStorage
from vkbottle.framework.labeler import BotLabeler

load_dotenv()
TOKEN = os.getenv('vk1.a.2L7_D0gncw08Ux7OXSOp8sYmezacEgDNI1_TMtpIvLjk9-KMBi8A1VeFwY83Dt0MV4XCWEVixdMpX08JhTdSsvGbF6UUfVGMBBO4YsRQrmtaWGdjz6_J3rlatARhOibRx3IsUBIXiwJHBTcsBdcCBY_qsOYe34x4VMjEgfHJAdrzhSAcaImK8EFlW4pR0sbdJKuKW2DtelwdpveZTpdAHA')
ADMIN_ID = os.getenv('677016482')

labeler = BotLabeler()
bot = Bot(
    token=TOKEN,
    labeler=labeler
)

admin_list = CtxStorage()

MODELS = [
    'users.models',
    'mining.models',
    'income.models',
    'admin.models',
    'aerich.models'
]

DATABASE_CONFIG = {
    'connections': {
        'default': 'sqlite://src/database/db.sqlite3?journal_mode=delete'
    },
    'apps': {
        'models': {
            'models': MODELS,
            'default_connection': 'default',
        }
    },
}


USER_STATUSES = {
    0: 'Пользователь',
    1: 'Хелпер',
    2: 'Администратор',
    3: 'Гл.Администратор',
    4: 'Основатель'
}

ADMIN_GRADES = {
    'Хелпер': {
        'lvl': 1,
        'emoji': '🦺',
        'commands': []
    },
    'Администратор': {
        'lvl': 2,
        'emoji': '👔',
        'commands': [
            '/setstatus <vk_id> <lvl> - изменить статус пользователя',
        ]
    },
    'Гл.Администратор': {
        'lvl': 3,
        'emoji': '🎩',
        'commands': [
            '/givemoney <vk_id> <money> - пополнить баланс пользователя',
            '/setmoney <vk_id> <money> - изменить баланс пользователя',
        ]
    },
    'Основатель': {
        'lvl': 5,
        'emoji': '👑',
        'commands': [
            '/del <vk_id> - удаление аккаунта пользователя',
        ]
    }
}
