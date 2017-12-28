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

from hydra_agent import Config
from hydra_agent.rac.cluster_manager.cluster import Cluster
from hydra_agent.rac.infobase_manager import InfoBaseManager


@pytest.fixture
def fake_infobase_manager():
    settings = Config(source='rac:\n    path: /opt/1C/v8.3/x86_64')()
    return InfoBaseManager(config=settings, cluster=Cluster(id='73a6a1b2-db40-11e7-049e-000d3a2c0d8b'))
