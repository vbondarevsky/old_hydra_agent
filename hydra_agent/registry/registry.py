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
import uuid


class Registry:

    def __init__(self, user):
        self._user = user

    @property
    def user_is_empty(self):
        return self._user == "00000000-0000-0000-0000-000000000000"

    @property
    def user(self):
        return uuid.uuid4().hex if self.user_is_empty else self._user

    def list(self):
        # TODO: брать из списка опубликовых баз с учетом доступности пользователю
        ib = [
            {
                "id": "c0d2a8b2-df9e-445d-bd97-ff9ea0ae8653",
                "name": "name1",
                "url": "http://127.0.0.1/name1",
                "order": 1001,
                "folder": "/Folder",
            },
            {
                "id": "ef1721db-0a3e-4c14-9c5a-5f0212ee1a14",
                "name": "name2",
                "url": "http://127.0.0.1/name2",
                "order": 1002,
                "folder": "/Folder",
            },
        ]
        result = ""
        for i in ib:
            result = result + (f"[{i['name']}]\n"
                               f'Connect=ws="{i["url"]}";\n'
                               f'ID={i["id"]}\n'
                               f'OrderInList={i["order"]}\n'
                               f'Folder={i["folder"]}\n'
                               f'OrderInTree={i["order"]}\n'
                               "External=0\n"
                               "ClientConnectionSpeed=Normal\n"
                               "UseProxy=0\n"
                               "App=Auto\n"
                               "WA=1\n"
                               "Version=8.3\n"
                               "WSA=1\n")
        return result

    def digest(self):
        return hashlib.md5(json.dumps(self.list()).encode("utf-8")).hexdigest()

    def verify(self, digest):
        if self._user == "00000000-0000-0000-0000-000000000000":
            return True
        else:
            return digest == self.digest()
