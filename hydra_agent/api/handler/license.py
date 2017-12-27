from aiohttp import web

from hydra_agent import license_manager


class LicenseHandler(web.View):
    async def get(self):
        license_manager.list()
        return web.json_response(license_manager.list())
