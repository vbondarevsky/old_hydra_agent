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
from hydra_agent.rac.session_manager.session import Session


class SessionManager(Rac):
    def __init__(self, cluster, settings=None):
        if not settings:
            settings = config.rac
        super().__init__(settings)
        self.cluster = cluster

    def info(self, session_id):
        """Returns `Session` by session id"""

    def list(self):
        """Returns collection of `Session`"""

        output = super()._run_command(["session", "list", f"--cluster={self.cluster.id}"])
        for params in self._parse_output(output):
            yield Session.from_dict(params)

    def terminate(self, session, error_message=None):
        """Terminate session"""

        super()._run_command(["session", "terminate", f"--session={session}", f"--cluster={self.cluster_id}"])

    def interrupt_current_call(self, session_id, error_message=None):
        """Interrupts current server call"""
