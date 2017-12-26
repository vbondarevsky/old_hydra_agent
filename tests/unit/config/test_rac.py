import pytest

from hydra_agent.config import Config


@pytest.mark.parametrize('source, expected', [
    ('test:', {'path': '', 'server': 'localhost', 'port': 1545}),
    ('rac:\n    path: /opt/1C/v8.3/x86_64', {'path': '/opt/1C/v8.3/x86_64', 'server': 'localhost', 'port': 1545}),
    ('rac:\n    path: /opt/1C/v8.3/x86_64\n    server: 1c',
     {'path': '/opt/1C/v8.3/x86_64', 'server': '1c', 'port': 1545}),
    ('rac:\n    path: /opt/1C/v8.3/x86_64\n    server: 1c\n    port: 1547',
     {'path': '/opt/1C/v8.3/x86_64', 'server': '1c', 'port': 1547}),
], ids=['empty', 'only_path', 'path_server', 'path_server_port'])
def test_success(source, expected):
    settings = Config(source=source)()
    assert settings['rac'] == expected
