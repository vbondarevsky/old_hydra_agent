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

import os

from hydra_agent import config
from hydra_agent.utils import is_windows
from hydra_agent.utils.system import run_command_async


class PostgreSQL:
    def __init__(self, name, settings=None):
        self.name = name
        if not settings:
            settings = config.postgresql
        self.bin = settings.path
        self.user = settings.user
        self.password = settings.password

    def _build_path(self, exe):
        return os.path.join(self.bin, exe + (".exe" if is_windows() else ""))

    @property
    def pg_dump(self):
        return self._build_path("pg_dump")

    @property
    def pg_restore(self):
        return self._build_path("pg_restore")

    @property
    def createdb(self):
        return self._build_path("createdb")

    @property
    def dropdb(self):
        return self._build_path("dropdb")

    async def save(self, file):
        await self._run_command([
            self.pg_dump,
            "-b", "-F", "c", "-Z", "9",
            "-f", file])

    async def load(self, file):
        args = [self.pg_restore]
        if self.user:
            args.extend(["-U", self.user])
        args.extend(["-d", self.name, file])
        await run_command_async(args)

    async def create(self):
        await self._run_command([self.createdb, "-T", "template0"])

    async def remove(self):
        await self._run_command([self.dropdb])

    async def _run_command(self, args):
        if self.user:
            args.extend(["-U", self.user])
        await run_command_async([*args, self.name])
