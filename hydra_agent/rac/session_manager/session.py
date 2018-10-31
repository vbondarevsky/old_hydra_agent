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


class Session:
    id = ""
    user = ""
    app = ""
    hibernate = False

    def __init__(self, session_id):
        self.id = session_id.strip()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def from_dict(params):
        session = Session(params["session"])
        session.user = params["user-name"]
        session.app = params["app-id"]
        session.hibernate = params["hibernate"] == "yes"
        return session

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user,
            "app": self.app,
            "hibernate": self.hibernate,
        }

# statistics: {
#     duration: {},
#     blocked: {
#         by_dbms: 0,
#         by_ls: 0,
#     },
#     bytes: {
#         all: 0,
#         last_5_min: 0
#     },
#     calls: {
#         last5min: 0,
#         all: 0,
#     }
#     memory: {
#         current: 0,
#         last5min: 0,
#         total: 0,
#     }
#     read: {
#         current: 0,
#         last5min: 0,
#         total: 0,
#     },
#     write: {
#         current: 0,
#         last5min: 0,
#         total: 0,
#     }
# }
