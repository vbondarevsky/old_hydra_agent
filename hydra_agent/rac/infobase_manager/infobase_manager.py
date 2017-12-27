from typing import Dict

from hydra_agent import Rac
from hydra_agent.rac.cluster_manager.cluster import Cluster
from hydra_agent.rac.infobase_manager.infobase import InfoBase


class InfoBaseManager(Rac):
    def __init__(self, config: Dict, cluster: Cluster):
        super().__init__(config)
        self.cluster = cluster

    def list(self):
        """Returns list of `InfoBase`"""

        result = []
        for ib_info in self._run_command(['infobase', 'summary', 'list']).split('\n\n'):
            if ib_info.strip():
                result.append(InfoBase(ib_info))
        return result

    def _run_command(self, args):
        args.append(f'--cluster={self.cluster.id}')
        return super()._run_command(args)
