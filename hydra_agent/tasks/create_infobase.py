from hydra_agent.clients import settings

path = r'"C:\Program Files (x86)\1cv8\8.3.12.1002\bin\1cv8.exe"'
is_windows = True

parameters = {'platform': path,
              }
infobase = {
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
def create(infobase, template=None):
    params = []
    params.append(settings.platform)
    params.append('createinfobase')
    params.append(connection_string(infobase))
    params.append(f"/AddToList \"{infobase['cluster']['name']}\"")
    if template:
        params.append(f'"{template}"')
    params.append(f'/Out \"{log_file}\"')
    params.append(f"/L {infobase['locale']}")



    if is_windows:

        pass
    else:
        pass
    command = ' '.join(params)

    params = {'cluster': {'server': {'host': '', 'port': 0},
                          'name': '', 'user': '', 'password': ''},
              'db': {'engine': ['MSSQLServer', 'PostgreSQL', 'IBMDB2', 'OracleDatabase'],
                     'host': '', 'port': 0, 'name': '', 'user': '', 'password': '',
                     'date_offset': 0},
              'license_distribution': [True, False],
              'allow_scheduled_jobs': [True, False],
              'create_db_if_not_exists': [True, False],
              'locale': ['ru_RU',...],
              }

    # файловая база:
    # File=//...;
    # Locale=Формат();
    #
    # клиент-сервер:
    # Srvr=[<протокол>://]<адрес>[:<порт>];
    # Ref=sdfljsldfj;
    #
    # CREATEINFOBASE < строка соединения >
    # [ / AddToList[ < имя ИБ >]]
    # [ / UseTemplate < имя файла шаблона >]
    # [ / Out < имя файла >]
    # [ / L]
    # [ / DumpResult < имя файла >]