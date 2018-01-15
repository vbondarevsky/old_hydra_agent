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

import hydra_agent
from hydra_agent.utils.system import run_command, is_windows


class V8:
    def __init__(self, config):
        self.path = os.path.join(config['v8']['path'], '1cv8' + '.exe' if is_windows() else '')
        self.template_path = config['v8']['template']

    def update(self):
        """
        /opt/1C/v8.3/x86_64/1cv8 DESIGNER /S"localhost\acc" /N"Администратор" /P"password" /Out"/home/support1c/acc.log" /UpdateCfg"/home/support1c/acc_3.0.57.10.cf" /UpdateDBCfg
        DISPLAY=:5 nohup /home/support1c/update.sh &
        :return:
        """

    def create_ib(self):
        pass

    def install_extension(self, ib, extension_name='HYDRA'):
        extension = os.path.join(self.template_path, extension_name + '.cfe')

        args = ['designer',
                #  TODO: лучше перейти на IBConnectionString
                '/F', ib,  # TODO: Должно работать не только с файловыми базами + логин:пароль
                '/LoadCfg', extension, '-Extension', extension_name,
                '/UpdateDBCfg']
        return self._run_command(args)

    def update_cf(self):
        pass

    def _run_command(self, args):
        log = hydra_agent.utils.system.temp_file_name()

        params = [self.path]
        params.extend(args)
        params.extend(['/DisableStartupDialogs', '/DisableStartupMessages', '/Out', log])
        r = run_command(params)
        with open(log, 'r') as f:
            trace = f.read()
        if os.path.exists(log):
            os.remove(log)

        return r, trace
