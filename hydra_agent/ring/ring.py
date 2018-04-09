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
import re

from hydra_agent.utils.system import run_command, is_windows


class Ring:
    def __init__(self, config):
        self.path = os.path.join(config.path, "ring" + ".cmd" if is_windows() else "")
        self.java = config.java

    @property
    def version(self):
        return run_command([self.path, "--version"])

    @property
    def modules(self):
        result = run_command([self.path, "help", "modules"])
        p = re.compile(r"[@:-]")

        modules = []
        for i in result.split("\n")[1:]:
            if not i.strip():
                continue
            modules.append(tuple(map(str.strip, p.split(i))))
        return modules

    def _run_command(self, args):
        # TODO: запуск под sudo
        os.environ["JAVA_HOME"] = self.java
        return run_command(args)
