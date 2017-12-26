import pytest

from hydra_agent.config import Config


@pytest.mark.parametrize('source, expected', [
    ('test:', {'path': ''}),
    ('ring:\n    path: /opt/1C/v8.3/x86_64', {'path': '/opt/1C/v8.3/x86_64'}),
], ids=['empty', 'path'])
def test_success(source, expected):
    settings = Config(source=source)()
    assert settings['ring'] == expected
