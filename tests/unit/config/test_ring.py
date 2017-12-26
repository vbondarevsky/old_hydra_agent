import pytest

from hydra_agent.config import Config


@pytest.mark.parametrize('source, expected', [
    ('test:', {'path': ''}),
    ('ring:\n    path: /opt/1C/v8.3/x86_64', {'path': '/opt/1C/v8.3/x86_64'}),
    ('ring:\n    path: /opt/1C/v8.3/x86_64\n    java: /usr/lib/jvm/java-8-oracle',
     {'path': '/opt/1C/v8.3/x86_64', 'java': '/usr/lib/jvm/java-8-oracle'}),
    ('ring:\n    path: C:\\Program Files\\1C\\1CE\\ring\n    java: C:\\Program Files\\Java\\jre-9.0.1',
     {'path': r'C:\Program Files\1C\1CE\ring', 'java': r'C:\Program Files\Java\jre-9.0.1'}),
], ids=['empty', 'path', 'path_java', 'windows_path_java'])
def test_success(source, expected):
    settings = Config(source=source)()
    assert settings['ring'] == expected
