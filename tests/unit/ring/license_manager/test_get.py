import hashlib
import subprocess

import pytest

import hydra_agent.utils.system
from tests.unit import success_result


@pytest.mark.parametrize('name, expected', [
    ('111111111111111-1111111111', 'c2af24740cc3ccb3a4b119c5b5fd8412'),
], ids=['success'])
def test_success(monkeypatch, fake_license_manager, name, expected):
    temp_file = hydra_agent.utils.system.temp_file_name()
    with open(temp_file, 'wb') as f:
        f.write(b'test_license')
    monkeypatch.setattr(hydra_agent.utils.system, 'temp_file_name', lambda: temp_file)
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, 'Лицензия успешно получена.'))
    assert hashlib.md5(fake_license_manager.get(name=name)).hexdigest() == expected

# TODO: добавить файлы
