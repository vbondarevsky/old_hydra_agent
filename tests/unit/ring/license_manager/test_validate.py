import subprocess

import pytest

from tests.unit import success_result, fail_result


@pytest.mark.parametrize('out, name', [
    ('111111111111111-1111111111', 'Проверка лицензии "111111111111111-1111111111" выполнена успешно'),
], ids=['success'])
def test_success(monkeypatch, fake_license_manager, out, name):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
    assert fake_license_manager.validate(name=name)


@pytest.mark.parametrize('name, out, return_code, path', [
    ('111111111111111-1111111111',
     ('Ошибка получения списка лицензий.\nПо причине: Ошибка при работе с хранилищем лицензий.\n'
      ' По причине: Директория не найдена: "/var/lic".\n'),
     1, '/var/lic'),
    ('111111111111111-1111111111',
     'Проверка лицензии завершилась с ошибкой. Лицензия не найдена\n',
     1, None)
], ids=['wrong_path', 'license_not_found'])
def test_fail(monkeypatch, fake_license_manager, name, out, return_code, path):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: fail_result(args, return_code, out))
    with pytest.raises(subprocess.CalledProcessError):
        fake_license_manager.validate(name=name, path=path)
