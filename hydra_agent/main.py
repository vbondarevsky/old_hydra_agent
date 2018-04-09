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


import optparse

from hydra_agent import config
from hydra_agent.api.main import run_server


def run():
    parser = optparse.OptionParser()
    parser.add_option("-c", "--config", dest="config", help="path to config file")

    (options, args) = parser.parse_args()

    if options.config:
        config.reload(path=options.config)

    run_server()


if __name__ == "__main__":
    run()
