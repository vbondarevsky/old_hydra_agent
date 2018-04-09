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


import pytest

from hydra_agent.config import Config
from hydra_agent.config.rac_config import RacConfig


@pytest.mark.parametrize(
    "source, expected",
    [
        ("test:",
         RacConfig("", "localhost", 1545)),
        ("rac:\n  path: /opt/1C/v8.3/x86_64",
         RacConfig("/opt/1C/v8.3/x86_64", "localhost", 1545)),
        ("rac:\n  path: /opt/1C/v8.3/x86_64\n  host: 1c",
         RacConfig("/opt/1C/v8.3/x86_64", "1c", 1545)),
        ("rac:\n  path: /opt/1C/v8.3/x86_64\n  host: 1c\n  port: 1547",
         RacConfig("/opt/1C/v8.3/x86_64", "1c", 1547)),
        ("rac:\n  path: C:\\Program Files\\1C\\1CE\\ring\n",
         RacConfig(r"C:\Program Files\1C\1CE\ring", "localhost", 1545)),
    ],
    ids=["empty", "only_path", "path_host", "path_host_and_port", "path_windows"]
)
def test_success(source, expected):
    settings = Config(source=source)
    assert settings.rac == expected
