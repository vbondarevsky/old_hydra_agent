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

import logging
import os
import uuid

from hydra_agent import config
from hydra_agent.utils import is_windows
from hydra_agent.utils.system import run_command_async, temp_file_name


logger = logging.getLogger("v8")


class V8:
    def __init__(self, connection_string, access_code=None, settings=None):
        self.connection_string = connection_string
        self.access_code = access_code
        if not settings:
            settings = config.v8
        self.path = os.path.join(settings.path, "1cv8" + (".exe" if is_windows() else ""))

    async def save_db(self, out):
        await self._run_designer([f'/DumpIB"{out}"'])
        return self

    async def load_db(self, file_db):
        await self._run_designer([f'/RestoreIB"{file_db}"'])
        return self

    async def create_db(self, name=None, template=None):
        logger.debug(f"create db {name}")
        args = [f'"{self.connection_string}"']
        if name:
            args.append(f'/AddToList"{name}"')
        if template:
            args.append(f'/UseTemplate"{template}"')
        await self._run_creation(args)
        return self

    async def update_cf(self, file_cf):
        logger.debug(f"update cf")
        await self._run_designer([f'/UpdateCfg"{file_cf}"'])
        return self

    async def update_db(self):
        logger.debug(f"update db")
        await self._run_designer([f'/UpdateDBCfg'])
        return self

    async def load_extension(self, extension_file):
        extension = "extension_" + uuid.uuid4().hex
        args = [
            f'/LoadCfg"{extension_file}"',
            f'-Extension"{extension}"',
            f'/UpdateDBCfg'
        ]
        await self._run_designer(args)
        return self

    async def run_data_processor(self, data_processor):
        logger.debug(f"run data processor")
        await self._run_enterprise([f'/Execute"{data_processor}"'])
        return self

    async def _run_designer(self, args):
        args.append(f'/IBConnectionString"{self.connection_string}"')
        await self._run_command([
            "DESIGNER",
            *args,
            "/DisableSplash",
            "/DisableStartupDialogs",
            "/DisableStartupMessages",
        ])

    async def _run_enterprise(self, args):
        args.append(f'/IBConnectionString"{self.connection_string}"')
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
            args.append(f'/UC"{self.access_code}"')
        log_file = temp_file_name()
        print(log_file)
        result = await run_command_async([self.path, *args, f'/Out"{log_file}"'])
        log = open(log_file).read()
        print(log)
        os.remove(log_file)
        return result
