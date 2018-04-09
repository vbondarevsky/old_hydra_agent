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


from hydra_agent.rac.cluster_manager.load_balancing_mode import LoadBalancingMode
from hydra_agent.rac.cluster_manager.security_level import SecurityLevel


class Cluster:
    def __init__(self, raw="", id=""):
        if id:
            self.id = id.strip()
        else:
            result = self.__parse(raw)
            self.id = result["cluster"]
            self.host = result["host"]
            self.port = int(result["port"])
            self.name = result["name"]
            self.expiration_timeout = int(result["expiration-timeout"])
            self.lifetime_limit = int(result["lifetime-limit"])
            self.max_memory_size = int(result["max-memory-size"])
            self.max_memory_time_limit = int(result["max-memory-time-limit"])
            self.security_level = SecurityLevel(int(result["security-level"]))
            self.session_fault_tolerance_level = int(result["session-fault-tolerance-level"])
            self.load_balancing_mode = LoadBalancingMode(result["load-balancing-mode"])
            self.errors_count_threshold = int(result["errors-count-threshold"])
            self.kill_problem_processes = bool(int(result["kill-problem-processes"]))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __parse(self, raw):
        result = {}
        for i in raw.strip().split("\n"):
            k, v = i.split(":", 1)
            result[k.strip()] = v.strip()
        return result
