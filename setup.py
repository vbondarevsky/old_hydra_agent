import os

from setuptools import find_packages, setup

NAME = 'hydra_agent'
here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name=NAME,
    version=about[NAME],
    description='Cross-platform remote administration agent for 1C:Enterprise',
    author='Vladimir Bondarevskiy',
    author_email='vbondarevsky@gmail.com',
    url='https://github.com/vbondarevsky/hydra_agent',
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
    }
)
