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


@pytest.mark.parametrize(
    "out, name",
    [
        ("111111111111111-1111111111", "Проверка лицензии \"111111111111111-1111111111\" выполнена успешно"),
    ],
    ids=["success"]
)
def test_success(monkeypatch, license_manager, out, name):
    monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: success_result(args, out))
    assert license_manager.validate(name=name)


@pytest.mark.parametrize(
    "name, out, return_code, path",
    [
        ("111111111111111-1111111111",
         ("Ошибка получения списка лицензий.\nПо причине: Ошибка при работе с хранилищем лицензий.\n"
          " По причине: Директория не найдена: \"/var/lic\".\n"),
         1, "/var/lic"),
        ("111111111111111-1111111111",
         "Проверка лицензии завершилась с ошибкой. Лицензия не найдена\n",
         1, None)
    ],
    ids=["wrong_path", "license_not_found"]
)
def test_fail(monkeypatch, license_manager, name, out, return_code, path):
    monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: fail_result(args, return_code, out))
    with pytest.raises(subprocess.CalledProcessError):
        license_manager.validate(name=name, path=path)
