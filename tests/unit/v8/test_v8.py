from os.path import join

from hydra_agent import v8

infobase = {
    'file': '',
    'name': 'test1',
    'cluster': {
        'server': {
            'host': 'localhost', 'port': 1541
        },
        'name': 'test1',
        'user': '',
        'password': ''
    },
    'db': {
        'engine': 'PostgreSQL',
        'host': 'localhost',
        'port': 0,
        'name': 'test1',
        'user': '',
        'password': '',
        'date_offset': 0
    },
    'license_distribution': True,
    'allow_scheduled_jobs': True,
    'create_db_if_not_exists': True,
    'locale': 'ru_RU'
}


def test_create_ib():
    ib = {
        'file': join('D:\\test bases', 'test1'),  # join(dirname(dirname(abspath(ROOT_DIR))), 'test1'),
        'name': 'test1',
        'locale': 'en_US'  # 'ru_RU'
    }
    r = v8.create_ib(ib)
    pass
