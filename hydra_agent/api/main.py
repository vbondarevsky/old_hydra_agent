from aiohttp import web

from hydra_agent.api.routes import setup_routes

DEBUG = True  # TODO: вынести в конфиг
HOST = '127.0.0.1'  # TODO: вынести в конфиг
PORT = 9523  # TODO: вынести в конфиг


def run_server():
    app = web.Application(debug=DEBUG)
    setup_routes(app)
    web.run_app(app, host=HOST, port=PORT)
