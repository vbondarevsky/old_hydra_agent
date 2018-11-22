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


import aiohttp.web

from hydra_agent.db import PostgreSQL
from hydra_agent.rac.cluster_manager import ClusterManager
from hydra_agent.rac.infobase_manager import InfoBaseManager
from hydra_agent.v8 import V8
from hydra_agent.v8.server_connection_string import ServerConnectionString


class BackupHandler(aiohttp.web.View):
    async def get(self):
        name = self.request.rel_url.query["name"]
        user = self.request.rel_url.query["user"]
        password = self.request.rel_url.query["password"]

        headers = {"Content-Disposition": f"attachment; filename=\"{name}.dt\""}
        return aiohttp.web.FileResponse(await backup(name, user, password), headers=headers)


async def backup(name, user, password):
    name_backup = name + "_backup"
    file = name + "_backup.pg"
    file_dt = name + ".dt"

    # 1. Сохранить бэкап
    pg = PostgreSQL(name)
    print(f"save db: {pg.name} to file: {file}")
    await pg.save(file)

    # 2. Загрузить бэкап
    print(f"check ib: {name_backup}")
    cluster_manager = ClusterManager()
    cluster = list(cluster_manager.list())[0]

    infobase_manager = InfoBaseManager(cluster)
    ib_exists = name_backup in [ib.name for ib in infobase_manager.list()]

    if not ib_exists:
        dst = ServerConnectionString(f"{cluster.host}:{cluster.port}", name_backup,
                                     db_engine="PostgreSQL",
                                     db_server="localhost", db_name=name_backup,
                                     db_user="postgres", db_password="", create_if_not_exist=True,
                                     license_server_distribution=True, allow_scheduled_jobs=False,
                                     locale="ru_RU")
        v8_creator = V8(dst)
        print(f"create ib: {dst}")
        await v8_creator.create_db(name_backup)

    pg = PostgreSQL(name_backup)
    try:
        print(f"remove db: {pg.name}")
        await pg.remove()
    except:
        pass
    print(f"create db: {pg.name}")
    await pg.create()
    print(f"load db: {pg.name} from file: {file}")
    await pg.load(file)

    # 3. Выгрузить dt
    v8 = V8(ServerConnectionString(f"{cluster.host}:{cluster.port}", name_backup, user, password))
    print(f"save dt: {v8.connection_string}")
    await v8.save_db(file_dt)

    print(file_dt)

    return file_dt
