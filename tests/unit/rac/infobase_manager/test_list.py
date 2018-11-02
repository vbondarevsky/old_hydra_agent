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
from rac.cluster_manager.cluster import Cluster
from tests.unit import success_result

out1 = ("infobase : df9533ac-4042-46b1-b445-2fa5d5be62a7\n"
        "name     : test_acc\n"
        "descr    : \"Тестовая база\"\n"
        "\n")
out2 = ("infobase : 017a66af-f7de-4a39-b988-e5fce435be46\n"
        "name     : test_hrm\n"
        "descr    :\n"
        "\n")

params1 = {
    "infobase": "df9533ac-4042-46b1-b445-2fa5d5be62a7",
    "name": "test_acc",
    "descr": "\"Тестовая база\"",
}

params2 = {
    "infobase": "017a66af-f7de-4a39-b988-e5fce435be46",
    "name": "test_hrm",
    "descr": "",
}

cluster = Cluster("73a6a1b2-db40-11e7-049e-000d3a2c0d8b")

infobase1 = InfoBase.from_dict(params1, cluster)
infobase2 = InfoBase.from_dict(params2, cluster)


@pytest.mark.parametrize(
    "out, expected",
    [
        ("\n", []),
        (out1, [infobase1]),
        (out1 + out2, [infobase1, infobase2])
    ],
    ids=["empty", "one", "few"]
)
def test_summary_success(monkeypatch, infobase_manager, out, expected):
    monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: success_result(args, out))
    assert list(infobase_manager.list()) == expected

# TODO: Какие фейлы можно протестировать?
