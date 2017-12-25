import subprocess

import pytest

from tests.unit import success_result, fail_result


@pytest.mark.parametrize('license, out', [
    (b'test_license', 'Лицензия успешно добавлена.\n'),
], ids=['put_license'])
def test_success(monkeypatch, fake_license_manager, license, out):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
    assert fake_license_manager.put(license=license)


@pytest.mark.parametrize('out, return_code, path', [
    (('Ошибка добавления файла лицензии.\nПо причине: Ошибка при работе с хранилищем лицензий.\n'
      ' По причине: Файл уже существует. Невозможно создать файл: '
      '"C:\\ProgramData\\1C\\licenses\\20171109214105.lic".\n'), 1, None),
    (('Ошибка удаления лицензии.\nПо причине: Ошибка при работе с хранилищем лицензий.\n'
      ' По причине: Директория не найдена: "c:\\license".\n'), 1, "c:\\license"),
], ids=['license_already_exists', 'wrong_path'])
def test_fail(monkeypatch, fake_license_manager, out, return_code, path):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: fail_result(args, return_code, out))
    with pytest.raises(subprocess.CalledProcessError):
        fake_license_manager.put(license=b'test_license', path=path)
