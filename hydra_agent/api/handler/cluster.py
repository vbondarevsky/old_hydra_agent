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

from api.handler.base import BaseHandler
from rac.cluster_manager import ClusterManager


class ClusterHandler(BaseHandler):
    @property
    def routes(self):
        return [
            aiohttp.web.post(self.build_route("/clusters"), self.create),
            aiohttp.web.get(self.build_route("/clusters"), self.read),
            aiohttp.web.get(self.build_route("/clusters/{cluster_id}"), self.read),
            aiohttp.web.put(self.build_route("/clusters"), self.update),
            aiohttp.web.delete(self.build_route("/clusters"), self.delete),
        ]

    async def create(self, request):
        pass

    async def read(self, request):
        cluster_id = request.match_info.get('cluster_id', None)
        # TODO: если задан cluster_id нужно возвращать один элемент, а не массив
        # TODO: возвращать 404 если элемент по cluster_id не найден
        return aiohttp.web.json_response(list(get_cluster(cluster_id)))

    async def update(self, request):
        pass

    async def delete(self, request):
        pass


def get_cluster(cluster_id=None):
    for cluster in ClusterManager().list():
        if cluster_id:
            if cluster.id == cluster_id:
                yield cluster.to_dict()
        else:
            yield cluster.to_dict()
