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


import hashlib
import subprocess

import pytest

import hydra_agent.utils.system
from tests.unit import success_result, fail_result


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


@pytest.mark.parametrize('out, return_code, path', [
    ('Ошибка получения файла лицензии. Лицензия не найдена\n', 1, None),
    (('Ошибка получения списка лицензий.\nПо причине: Ошибка при работе с хранилищем лицензий.\n'
      ' По причине: Директория не найдена: "/var/lic".\n'), 1, '/var/lic'),
], ids=['wrong_name', 'wrong_path'])
def test_fail(monkeypatch, fake_license_manager, out, return_code, path):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: fail_result(args, return_code, out))
    with pytest.raises(subprocess.CalledProcessError):
        fake_license_manager.get(name='111111111111111-1111111111', path=path)
