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
    id = ""
    host = ""
    port = 0
    name = ""
    expiration_timeout = 0
    lifetime_limit = 0
    max_memory_size = 0
    max_memory_time_limit = 0
    security_level = SecurityLevel.InsecureConnection
    session_fault_tolerance_level = 0
    load_balancing_mode = LoadBalancingMode.Performance
    errors_count_threshold = 0
    kill_problem_processes = False

    def __init__(self, cluster_id):
        self.id = cluster_id.strip()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"<Cluster(id={self.id})>"

    @staticmethod
    def from_dict(params):
        cluster = Cluster(params["cluster"])
        cluster.host = params["host"]
        cluster.port = int(params["port"])
        cluster.name = params["name"]
        cluster.expiration_timeout = int(params["expiration-timeout"])
        cluster.lifetime_limit = int(params["lifetime-limit"])
        cluster.max_memory_size = int(params["max-memory-size"])
        cluster.max_memory_time_limit = int(params["max-memory-time-limit"])
        cluster.security_level = SecurityLevel(int(params["security-level"]))
        cluster.session_fault_tolerance_level = int(params["session-fault-tolerance-level"])
        cluster.load_balancing_mode = LoadBalancingMode(params["load-balancing-mode"])
        cluster.errors_count_threshold = int(params["errors-count-threshold"])
        cluster.kill_problem_processes = bool(int(params["kill-problem-processes"]))
        return cluster

    def to_dict(self):
        return {
            "id": self.id,
            "host": self.host,
            "port": self.port,
            "name": self.name,
            "expiration_timeout": self.expiration_timeout,
            "lifetime_limit": self.lifetime_limit,
            "max_memory_size": self.max_memory_size,
            "max_memory_time_limit": self.max_memory_time_limit,
            "security_level": self.security_level.value,
            "session_fault_tolerance_level": self.session_fault_tolerance_level,
            "load_balancing_mode": self.load_balancing_mode.value,
            "errors_count_threshold": self.errors_count_threshold,
            "kill_problem_processes": self.kill_problem_processes,
        }
