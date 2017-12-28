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


from os.path import dirname, abspath, join

from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Config:
    def __init__(self, path=None, source=''):
        self.path = path or join(dirname(dirname(dirname(abspath(__file__)))), 'etc', 'hydra_agent.yml')
        self.source = source or None
        self._load_settings()

    def __call__(self, *args, **kwargs):
        return self.settings

    def _load_settings(self):
        if self.source:
            self.settings = load(self.source, Loader=Loader)
        else:
            with open(self.path) as f:
                self.settings = load(f, Loader=Loader)

        self._default_rac()
        self._default_ring()

    def _default_rac(self):
        if 'rac' not in self.settings:
            self.settings['rac'] = {'path': '', 'server': 'localhost', 'port': 1545}
        if 'server' not in self.settings['rac'] or not self.settings['rac']['server']:
            self.settings['rac']['server'] = 'localhost'
        if 'port' not in self.settings['rac'] or not self.settings['rac']['port']:
            self.settings['rac']['port'] = 1545

    def _default_ring(self):
        if 'ring' not in self.settings:
            self.settings['ring'] = {'path': ''}
