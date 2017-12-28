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


from aiohttp import web

from hydra_agent.api.routes import setup_routes

DEBUG = True  # TODO: вынести в конфиг
HOST = '127.0.0.1'  # TODO: вынести в конфиг
PORT = 9523  # TODO: вынести в конфиг


def run_server():
    app = web.Application(debug=DEBUG)
    setup_routes(app)
    web.run_app(app, host=HOST, port=PORT)
