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

from hydra_agent.rac.infobase_manager.infobase import InfoBase
from tests.unit import success_result

out_1 = "infobase : 4a824148-db94-11e7-7b82-000d3a2c0d8b\nname     : test_acc\ndescr    : \n\n"
out_2 = "infobase : a50570f4-db94-11e7-7b82-000d3a2c0d8b\nname     : test_hrm\ndescr    : \n\n"


@pytest.mark.parametrize(
    "out, expected",
    [
        ("\n\n", []),
        (out_1, [InfoBase(out_1)]),
        (out_1 + out_2, [InfoBase(out_1), InfoBase(out_2)])
    ],
    ids=["empty", "one", "few"]
)
def test_success(monkeypatch, infobase_manager, out, expected):
    monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: success_result(args, out))
    assert infobase_manager.list() == expected

# TODO: Какие фейлы можно протестировать?
