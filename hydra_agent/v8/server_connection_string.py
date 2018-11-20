from hydra_agent.v8.connection_string import ConnectionString


class ServerConnectionString(ConnectionString):

    def __init__(self, server, name, user=None, password=None,
                 db_engine=None, db_server=None, db_name=None, db_user=None, db_password=None,
                 date_offset=None, create_if_not_exist=None, locale=None,
                 cluster_user=None, cluster_password=None,
                 license_server_distribution=None, allow_scheduled_jobs=None):
        assert not db_engine or db_engine in ["MSSQLServer", "PostgreSQL", "IBMDB2", "OracleDatabase"]

        self.server = server
        self.name = name
        self.user = user
        self.password = password
        self.db_engine = db_engine
        self.db_server = db_server
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.date_offset = date_offset
        self._create_if_not_exist = create_if_not_exist
        self.locale = locale
        self.cluster_user = cluster_user
        self.cluster_password = cluster_password
        self._license_server_distribution = license_server_distribution
        self._allow_scheduled_jobs = allow_scheduled_jobs

    @property
    def create_if_not_exist(self):
        return self._bool2str(self._create_if_not_exist)

    @property
    def license_server_distribution(self):
        return self._bool2str(self._license_server_distribution)

    @property
    def allow_scheduled_jobs(self):
        return self._bool2str(not self._allow_scheduled_jobs)

    def _bool2str(self, value):
        if not value:
            return None
        return "Y" if value else "N"

    def _get_properties(self):
        return {
            "server": "Srvr",
            "name": "Ref",
            "user": "Usr",
            "password": "Pwd",
            "db_engine": "DBMS",
            "db_server": "DBSrvr",
            "db_name": "DB",
            "db_user": "DBUID",
            "db_password": "DBPwd",
            "date_offset": "SQLYOffs",
            "create_if_not_exist": "CrSQLDB",
            "locale": "Locale",
            "cluster_user": "SUsr",
            "cluster_password": "SPwd",
            "license_server_distribution": "LicDstr",
            "allow_scheduled_jobs": "SchJobDn",
        }
