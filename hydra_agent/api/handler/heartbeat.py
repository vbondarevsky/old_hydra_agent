import os
import platform

from aiohttp import web

from hydra_agent.__version__ import hydra_agent
from hydra_agent.utils import is_windows


class HeartbeatHandler(web.View):
    async def get(self):
        return web.json_response(heartbeat())


def heartbeat():
    data = {
        'version': hydra_agent,
        'load_average': load_average(),
        #'uptime': uptime(),
        'os': os_info(),
        'cpu': cpu_count(),
        #'memory': memory()
    }

    return data


def load_average():
    if is_windows():
        raise NotImplementedError
    else:
        return os.getloadavg()


def uptime():
    raise NotImplementedError


def os_info():
    r = platform.uname()
    result = {
        'system': r.system,
        'node': r.node,
        'release': r.release,
        'version': r.version,
        'architecture': platform.architecture()[0]
    }
    return result


def cpu_count():
    return os.cpu_count()


def memory():
    raise NotImplementedError
