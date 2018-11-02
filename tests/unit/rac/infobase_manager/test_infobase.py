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


from hydra_agent.rac.cluster_manager.cluster import Cluster
from hydra_agent.rac.infobase_manager.infobase import InfoBase

params = {
    "infobase": "73a6a1b2-db40-11e7-049e-000d3a2c0d8b",
    "name": "test_acc",
    "descr": "Тестовая база БП",
}


def test_create_from_dict():
    infobase = InfoBase.from_dict(params, Cluster("017a66af-f7de-4a39-b988-e5fce435be46"))
    assert infobase.id == "73a6a1b2-db40-11e7-049e-000d3a2c0d8b"
    assert infobase.name == "test_acc"
    assert infobase.description == "Тестовая база БП"
    assert infobase.cluster.id == "017a66af-f7de-4a39-b988-e5fce435be46"


def test_create_from_id():
    infobase = InfoBase("73a6a1b2-db40-11e7-049e-000d3a2c0d8b\n", Cluster("017a66af-f7de-4a39-b988-e5fce435be46"))
    assert infobase.id == "73a6a1b2-db40-11e7-049e-000d3a2c0d8b"
    assert infobase.cluster.id == "017a66af-f7de-4a39-b988-e5fce435be46"
