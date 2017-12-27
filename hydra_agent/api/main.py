from aiohttp import web

from hydra_agent.api.routes import setup_routes


def run_server():
    app = web.Application()
    setup_routes(app)
    web.run_app(app, host='127.0.0.1', port=9523)
