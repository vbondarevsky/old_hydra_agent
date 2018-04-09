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


import os
import platform

import aiohttp.web

from hydra_agent.__version__ import hydra_agent


class HeartbeatHandler(aiohttp.web.View):
    async def get(self):
        return aiohttp.web.json_response(heartbeat())


def heartbeat():
    data = {
        "version": {
            "hydra_agent": hydra_agent,
        },
        "os": os_info(),
        "cpu": cpu_count(),
    }

    return data


def os_info():
    r = platform.uname()
    result = {
        "system": r.system,
        "node": r.node,
        "release": r.release,
        "version": r.version,
        "architecture": platform.architecture()[0]
    }
    return result


def cpu_count():
    return os.cpu_count()
