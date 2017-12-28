from aiohttp import web

from hydra_agent import license_manager


class LicenseHandler(web.View):
    async def get(self):
        return web.json_response(license_manager.list())
