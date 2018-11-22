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
import uuid

from hydra_agent import config
from hydra_agent.utils import is_windows
from hydra_agent.utils.system import run_command_async
from hydra_agent.utils.system import temp_file_name


class V8:
    def __init__(self, connection_string, access_code=None, settings=None):
        self.connection_string = connection_string
        self.access_code = access_code
        if not settings:
            settings = config.v8
        self.path = os.path.join(settings.path, "1cv8" + (".exe" if is_windows() else ""))
        self.display = settings.display

    async def save_db(self, out):
        await self._run_command([
            "DESIGNER",
            "/S", f"{self.connection_string.server}\\{self.connection_string.name}",
            "/N", str(self.connection_string.user),
            "P", str(self.connection_string.password),
            "/DumpIB", out,
            "/DisableSplash",
            "/DisableStartupDialogs",
            "/DisableStartupMessages",
        ])

    async def load_db(self, file_db):
        await self._run_designer(["/RestoreIB", file_db])

    async def create_db(self, name=None, template=None):
        args = [str(self.connection_string)]
        if name:
            args.extend(["/AddToList", name])
        if template:
            args.extend(["/UseTemplate", template])
        await self._run_creation(args)

    async def update_cf(self, file_cf):
        await self._run_designer(["/UpdateCfg", file_cf])

    async def update_db(self):
        await self._run_designer(["/UpdateDBCfg"])

    async def load_extension(self, extension_file):
        extension = "extension_" + uuid.uuid4().hex
        args = [
            "/LoadCfg", extension_file,
            "-Extension", extension,
            "/UpdateDBCfg"
        ]
        await self._run_designer(args)

    async def run_data_processor(self, data_processor):
        await self._run_enterprise(["/Execute", data_processor])

    async def _run_designer(self, args):
        args.extend(["/IBConnectionString", str(self.connection_string)])
        await self._run_command([
            "DESIGNER",
            *args,
            "/DisableSplash",
            "/DisableStartupDialogs",
            "/DisableStartupMessages",
        ])

    async def _run_enterprise(self, args):
        args.extend(["/IBConnectionString", str(self.connection_string)])
        await self._run_command([
            "ENTERPRISE",
            *args,
            "/DisableSplash",
            "/DisableStartupDialogs",
            "/DisableStartupMessages",
        ])

    async def _run_creation(self, args):
        await self._run_command([
            "CREATEINFOBASE",
            *args,
        ])

    async def _run_command(self, args):
        if self.access_code:
            args.extend(["/UC", self.access_code])
        log_file = temp_file_name()
        print(log_file)
        env = os.environ.copy()
        if self.display:
            env["DISPLAY"] = str(self.display)
        result = await run_command_async([self.path, *args, "/Out", log_file], env)
        log = open(log_file).read()
        print(log)
        os.remove(log_file)
        return result
