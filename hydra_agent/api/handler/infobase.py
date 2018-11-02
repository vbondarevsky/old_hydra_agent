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

import aiohttp.web

from hydra_agent.api.handler.base import BaseHandler
from hydra_agent.rac.cluster_manager.cluster import Cluster
from hydra_agent.rac.infobase_manager import InfoBaseManager


class InfoBaseHandler(BaseHandler):
    @property
    def routes(self):
        return [
            aiohttp.web.get(self.build_route("/clusters/{cluster_id}/infobases"), self.read),
            aiohttp.web.get(self.build_route("/clusters/{cluster_id}/infobases/{infobase_id}"), self.read),
        ]

    async def read(self, request):
        cluster_id = request.match_info.get("cluster_id")
        infobase_id = request.match_info.get("infobase_id", None)
        return aiohttp.web.json_response(get_infobases(cluster_id, infobase_id))


def get_infobases(cluster_id, infobase_id=None):
    if infobase_id:
        return get_info(cluster_id, infobase_id)
    else:
        return get_list(cluster_id)


def get_list(cluster_id):
    infobases = []
    for infobase in InfoBaseManager(Cluster(cluster_id)).list():
        infobases.append(infobase.to_dict())
    return infobases


def get_info(cluster_id, infobase_id):
    for infobase in get_list(cluster_id):
        if infobase["id"] == infobase_id:
            return infobase
