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


import hashlib
import json
import logging
import uuid

from hydra_agent.registry.infobase import Infobase


logger = logging.getLogger("hydra.registry")


class Registry:

    def __init__(self, user):
        self._user = user
        self._digest = None

    @property
    def user_is_empty(self):
        return self._user == "00000000-0000-0000-0000-000000000000"

    @property
    def user(self):
        return uuid.uuid4().hex if self.user_is_empty else self._user

    def list(self):
        logger.info("Get infobase list for user: %s", self.user)
        # TODO: брать из списка опубликовых баз с учетом доступности пользователю
        ib = [
            Infobase("c0d2a8b2-df9e-445d-bd97-ff9ea0ae8653", "name1", "http://127.0.0.1/name1", 1001),
            Infobase("ef1721db-0a3e-4c14-9c5a-5f0212ee1a14", "name2", "http://127.0.0.1/name2", 1002),
        ]
        return "\n".join([i.v8i for i in ib])

    @property
    def digest(self):
        if not self._digest:
            self.list()
        return self._digest

    def verify(self, digest):
        logger.info("Verify infobase list: current - %s, new - %s", digest, self.digest)
        if self._user == "00000000-0000-0000-0000-000000000000":
            logger.info("Infobase list changed: %s", True)
            return True
        else:
            logger.info("Infobase list changed: %s", digest != self.digest)
            return digest != self.digest

    def _set_digest(self):
        self._digest = hashlib.md5(json.dumps(self.list()).encode("utf-8")).hexdigest()
