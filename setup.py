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
import io
import os

from setuptools import find_packages, setup

NAME = 'hydra_agent'
here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name=NAME,
    version=about[NAME],
    description='Cross-platform remote administration agent for 1C:Enterprise',
    long_description=long_description,
    author='Vladimir Bondarevskiy',
    author_email='vbondarevsky@gmail.com',
    url='https://github.com/vbondarevsky/hydra_agent',
    license="https://www.gnu.org/licenses/gpl-3.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires='>=3',
    install_requires=[
        'pyyaml',
        'aiohttp'
    ],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'hydra_agent = hydra_agent.main:run'
        ]
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
