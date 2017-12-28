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
from typing import List, Dict

import hydra_agent.utils.system
from hydra_agent.ring import Ring


class LicenseManager(Ring):
    def __init__(self, config: Dict):
        super().__init__(config)

    def activate(self, license_info: Dict, serial: str, pin: str, previous_pin: str = '', path: str = '') -> bool:
        """Activates license"""

        args = [self.path, 'license', 'activate']
        for k, v in license_info.items():
            if v.strip():
                args.append(f'--{k.replace("_","-")}')
                args.append(v.strip())
        args.extend(['--pin', pin.strip()])
        if previous_pin:
            args.extend(['--previous-pin', previous_pin.strip()])
        if path:
            args.extend(['--path', path.strip()])
        self._run_command(args)
        return True

    def get(self, name: str, path: str = '') -> bytes:
        """Returns license file"""

        temp_file = hydra_agent.utils.system.temp_file_name()
        args = [self.path, 'license', 'get', '--name', name.strip(), '--license', temp_file]
        if path:
            args.extend(['--path', path.strip()])
        try:
            self._run_command(args)
            with open(temp_file, 'rb') as f:
                lic = f.read()
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        return lic

    def info(self, name: str, path: str = '') -> str:
        """Returns license info"""

        args = [self.path, 'license', 'info', '--name', name.strip()]
        if path:
            args.extend(['--path', path.strip()])
        return self._run_command(args)

    def list(self, path: str = '') -> List[str]:
        """Returns list of licenses"""

        args = [self.path, 'license', 'list']
        if path:
            args.extend(['--path', path.strip()])
        r = self._run_command(args)
        return r.split()

    def put(self, license: bytes, path: str = '') -> bool:
        """Adds license file to storage"""

        license_file = hydra_agent.utils.system.temp_file_name()
        with open(license_file, 'wb') as f:
            f.write(license)
        args = [self.path, 'license', 'put', '--license', license_file]
        if path:
            args.extend(['--path', path.strip()])
        try:
            self._run_command(args)
        finally:
            if os.path.exists(license_file):
                os.remove(license_file)
        return True

    def remove(self, name: str, path: str = '') -> bool:
        """Removes license file from storage"""

        args = [self.path, 'license', 'remove', '--name', name.strip(), '--all']
        if path:
            args.extend(['--path', path.strip()])
        self._run_command(args)
        return True

    def validate(self, name: str, path: str = '') -> bool:
        """Validates license"""

        args = [self.path, 'license', 'validate', '--name', name.strip()]
        if path:
            args.extend(['--path', path.strip()])
        self._run_command(args)
        return True
