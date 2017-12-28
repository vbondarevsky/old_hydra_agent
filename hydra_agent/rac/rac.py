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


import os.path
from typing import Dict

from hydra_agent.utils.system import run_command


class Rac:
    def __init__(self, config: Dict):
        self.path = os.path.join(config['rac']['path'], 'rac')
        self.server = config['rac']['server']
        self.port = config['rac']['port']

    @property
    def version(self):
        return self._run_command([self.path, '--version'])

    def _run_command(self, args):
        return run_command(self.__add_server([self.path, '--version']))

    def __add_server(self, args):
        args.append(f"{self.server}:{self.port}")
        return args
