# This file is part of HYDRA - cross-platform remote administration
# system for 1C:Enterprise (https://github.com/vbondarevsky/hydra_agent).
# Copyright (C) 2017  Vladimir Bondarevskiy.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
