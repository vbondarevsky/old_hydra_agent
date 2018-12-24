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
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from hydra_agent import config


def basic_auth(excluded_urls):
    async def factory(app, handler):
        async def middleware(request):
            for url in excluded_urls:
                if request.path.startswith(url):
                    continue

                try:
                    username, password, _ = aiohttp.BasicAuth.decode(request.headers["Authorization"])
                    if username == config.auth.user and pbkdf2_sha256.verify(password, config.auth.hash):
                        return await handler(request)
                    return aiohttp.web.HTTPUnauthorized(headers={'WWW-Authenticate': 'Basic'})
                except KeyError:
                    return aiohttp.web.HTTPUnauthorized(headers={'WWW-Authenticate': 'Basic'})
            return await handler(request)

        return middleware

    return factory
