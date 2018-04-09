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


from hydra_agent.rac.infobase_manager.infobase import InfoBase

raw = "infobase : 4a824148-db94-11e7-7b82-000d3a2c0d8b\nname     : test_acc\ndescr    : \n\n"


def test_create_from_string():
    ib = InfoBase(raw=raw)
    assert ib.id == "4a824148-db94-11e7-7b82-000d3a2c0d8b"
    assert ib.name == "test_acc"
    assert ib.description == ""


def test_create_from_id():
    ib = InfoBase(id="4a824148-db94-11e7-7b82-000d3a2c0d8b\n")
    assert ib.id == "4a824148-db94-11e7-7b82-000d3a2c0d8b"
