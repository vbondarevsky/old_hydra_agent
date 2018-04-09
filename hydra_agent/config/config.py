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


import yaml

from hydra_agent.config.api_config import ApiConfig
from hydra_agent.config.rac_config import RacConfig
from hydra_agent.config.ring_config import RingConfig
from hydra_agent.config.v8_config import V8Config

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Config:
    def __init__(self, path="", source=""):
        self._load(path, source)

    def __str__(self):
        return f"rac: {self.rac}, ring: {self.ring}, api: {self.api}, v8: {self.v8}"

    def reload(self, path="", source=""):
        self._load(path, source)

    def _load(self, path, source):
        config = self._config(path, source)

        self.rac = self._rac_config(config)
        self.ring = self._ring_config(config)
        self.api = self._api_config(config)
        self.v8 = self._v8_config(config)

    @staticmethod
    def _rac_config(config):
        path = ""
        host = "localhost"
        port = 1545
        java = ""
        if "rac" in config:
            if "path" in config["rac"]:
                path = config["rac"]["path"]
            if "host" in config["rac"]:
                host = config["rac"]["host"]
            if "port" in config["rac"]:
                port = config["rac"]["port"]

        return RacConfig(path, host, port)

    @staticmethod
    def _ring_config(config):
        path = ""
        java = ""
        if "ring" in config:
            if "path" in config["ring"]:
                path = config["ring"]["path"]
            if "java" in config["ring"]:
                java = config["ring"]["java"]
        return RingConfig(path, java)

    @staticmethod
    def _api_config(config):
        host = "localhost"
        port = 9523
        debug = False
        if "api" in config:
            if "host" in config["api"]:
                host = config["api"]["host"]
            if "port" in config["api"]:
                port = config["api"]["port"]
            if "debug" in config["api"]:
                debug = config["api"]["debug"]
        return ApiConfig(host, port, debug)

    @staticmethod
    def _v8_config(config):
        path = ""
        if "v8" in config:
            if "path" in config["v8"]:
                path = config["v8"]["path"]
        return V8Config(path)

    @staticmethod
    def _config(path, source):
        if source:
            config = yaml.load(source, Loader)
        elif path:
            with open(path) as f:
                config = yaml.load(f, Loader)
        else:
            config = {}

        return config
