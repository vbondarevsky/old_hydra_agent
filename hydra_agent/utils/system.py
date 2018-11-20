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

import asyncio
import platform
import subprocess
import sys
from tempfile import NamedTemporaryFile


def is_linux():
    return platform.system() == "Linux"


def is_windows():
    return platform.system() == "Windows"


def is_mac():
    return platform.system() == "Darwin"


def temp_file_name():
    with NamedTemporaryFile(delete=False) as tmp:
        return tmp.name


def run_command(args):
    r = subprocess.run(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        check=True,
        encoding=encoding()
    )
    return r.stdout.strip()


def encoding():
    if is_windows():
        import ctypes
        return f"cp{ctypes.windll.kernel32.GetOEMCP()}"
    else:
        return (sys.stdout.encoding if sys.stdout.isatty() else
                sys.stderr.encoding if sys.stderr.isatty() else
                sys.getfilesystemencoding() or "utf-8")


async def run_command_async(args, env=None):
    process = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=env)
    stdout, stderr = await process.communicate()
    return stdout.decode(encoding()).strip()
