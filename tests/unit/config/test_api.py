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
from hydra_agent.config.api_config import ApiConfig


@pytest.mark.parametrize(
    "source, expected",
    [
        ("test:",
         ApiConfig("localhost", 9523, False)),
        ("api:\n  host: 1c\n",
         ApiConfig("1c", 9523, False)),
        ("api:\n  host: 1c\n  port: 8889\n",
         ApiConfig("1c", 8889, False)),
        ("api:\n  host: 1c\n  port: 8889\n  debug: True",
         ApiConfig("1c", 8889, True))
    ],
    ids=["empty", "host", "port", "debug"]
)
def test_success(source, expected):
    settings = Config(source=source)
    assert settings.api == expected
