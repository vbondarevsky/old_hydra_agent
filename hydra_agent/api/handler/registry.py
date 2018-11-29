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
from hydra_agent.registry import Registry


class RegistryHandler(BaseHandler):
    @property
    def routes(self):
        return [
            aiohttp.web.head(self.build_route("/registry/WebCommonInfoBases"), self.ok),
            aiohttp.web.get(self.build_route("/registry/WebCommonInfoBases/CheckInfoBases"), self.check),
            aiohttp.web.get(self.build_route("/registry/WebCommonInfoBases/GetInfoBases"), self.list),
        ]

    @staticmethod
    async def ok(request):
        return aiohttp.web.Response()

    @staticmethod
    async def check(request):
        user = request.rel_url.query["ClientID"]
        digest = request.rel_url.query["InfoBasesCheckCode"]

        result = {
            "root": {
                "InfoBasesChanged": Registry(user).verify(digest),
            }
        }
        return aiohttp.web.json_response(result)

    @staticmethod
    async def list(request):
        # return aiohttp.web.HTTPUnauthorized()

        user = request.rel_url.query["ClientID"]

        registry = Registry(user)

        result = {
            "root": {
                "ClientID": registry.user,
                "InfoBasesCheckCode": registry.digest,
                "InfoBases": registry.list(),
            }
        }
        return aiohttp.web.json_response(result)
