import subprocess

import pytest

from tests.unit import success_result, fail_result


@pytest.mark.parametrize('name, out', [
    ('111111111111111-1111111111', 'Лицензия удалена : "111111111111111-1111111111".\n'),
    ('', 'Лицензия удалена : "111111111111111-1111111111".\n'),
], ids=['name', 'all'])
def test_success(monkeypatch, fake_license_manager, name, out):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
    assert fake_license_manager.remove(name=name)


@pytest.mark.parametrize('name, out, return_code, path', [
    ('', ('Ошибка получения списка лицензий.\nПо причине: Ошибка при работе с хранилищем лицензий.\n'
          ' По причине: Директория не найдена: "/var/lic".\n'), 1, '/var/lic'),
    ('111122223333445-1234567890', 'Ошибка удаления лицензии. Лицензия не найдена\n', 1, None),
], ids=['wrong_path', 'license_not_found'])
def test_fail(monkeypatch, fake_license_manager, name, out, return_code, path):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: fail_result(args, return_code, out))
    with pytest.raises(subprocess.CalledProcessError):
        fake_license_manager.remove(name=name, path=path)
