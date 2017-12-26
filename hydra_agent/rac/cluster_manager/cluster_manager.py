from typing import Dict

from hydra_agent import Rac
from hydra_agent.rac.cluster_manager.cluster import Cluster


class ClusterManager(Rac):
    def __init__(self, config: Dict):
        super().__init__(config)

    def list(self):
        """Returns list of `Cluster`"""

        result = []
        for cluster_info in super()._run_command(['cluster', 'list']).split('\n\n'):
            if cluster_info.strip():
                result.append(Cluster(cluster_info))
        return result
