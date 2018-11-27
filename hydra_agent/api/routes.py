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

from hydra_agent.api.handler.backup import BackupHandler
from hydra_agent.api.handler.cluster import ClusterHandler
from hydra_agent.api.handler.heartbeat import HeartbeatHandler
from hydra_agent.api.handler.infobase import InfoBaseHandler
from hydra_agent.api.handler.license import LicenseHandler
from hydra_agent.api.handler.registry import RegistryHandler
from hydra_agent.api.handler.session import SessionHandler


def build_route(route):
    return f"/hydra_agent/api/v1{route}"


def setup_routes(app):
    app.router.add_route("*", build_route("/license"), LicenseHandler)
    app.router.add_route("*", build_route("/heartbeat"), HeartbeatHandler)
    app.router.add_route("*", build_route("/backup"), BackupHandler)
    app.add_routes(ClusterHandler().routes)
    app.add_routes(SessionHandler().routes)
    app.add_routes(InfoBaseHandler().routes)
    app.add_routes(RegistryHandler().routes)
