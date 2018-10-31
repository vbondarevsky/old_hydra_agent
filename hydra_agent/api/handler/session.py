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
from hydra_agent.rac.session_manager import SessionManager
from rac.cluster_manager.cluster import Cluster


class SessionHandler(BaseHandler):
    @property
    def routes(self):
        return [
            aiohttp.web.get(self.build_route("/clusters/{cluster_id}/sessions"), self.read),
            aiohttp.web.get(self.build_route("/clusters/{cluster_id}/sessions/{session_id}"), self.read),
        ]

    async def read(self, request):
        cluster_id = request.match_info.get("cluster_id")
        session_id = request.match_info.get("session_id", None)
        return aiohttp.web.json_response(get_sessions(cluster_id, session_id))


def get_sessions(cluster_id, session_id=None):
    if session_id:
        return get_info(cluster_id, session_id)
    else:
        return get_list(cluster_id)


def get_list(cluster_id):
    sessions = []
    for session in SessionManager(Cluster(cluster_id)).list():
        sessions.append(session.to_dict())
    return sessions


def get_info(cluster_id, session_id):
    for session in get_list(cluster_id):
        if session["id"] == session_id:
            return session
