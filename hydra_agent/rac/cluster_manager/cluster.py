class Cluster:
    def __init__(self, raw: str):
        result = self.__parse(raw)
        self.host = result['host']
        self.port = int(result['port'])
        self.name = result['name']
        self.expiration_timeout = int(result['expiration-timeout'])
        self.lifetime_limit = int(result['lifetime-limit'])
        self.max_memory_size = int(result['max-memory-size'])
        self.max_memory_time_limit = int(result['max-memory-time-limit'])
        # TODO: Может лучше перечисление?
        self.security_level = int(result['security-level'])
        # TODO: Может лучше перечисление?
        self.session_fault_tolerance_level = int(result['session-fault-tolerance-level'])
        # TODO: Может лучше перечисление?
        self.load_balancing_mode = result['load-balancing-mode']
        self.errors_count_threshold = int(result['errors-count-threshold'])
        # TODO: Может лучше перечисление?
        self.kill_problem_processes = int(result['kill-problem-processes'])

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __parse(self, raw):
        result = {}
        for i in raw.strip().split('\n'):
            k, v = i.split(':', 1)
            result[k.strip()] = v.strip()
        return result
