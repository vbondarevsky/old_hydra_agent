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


from hydra_agent import Rac
from hydra_agent import config
from hydra_agent.rac.infobase_manager.infobase import InfoBase


class InfoBaseManager(Rac):
    def __init__(self, cluster, settings=None):
        if not settings:
            settings = config.rac
        super().__init__(settings)
        self.cluster = cluster

    def list(self):
        """Returns collection of `InfoBase`"""

        output = super()._run_command(["infobase", "summary", "list", f"--cluster={self.cluster.id}"])
        for params in self._parse_output(output):
            yield InfoBase.from_dict(params, self.cluster)
