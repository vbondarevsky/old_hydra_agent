import setuptools

import hydra_agent

configuration = {
    "name": "hydra_agent",
    "version": hydra_agent.__version__,
    "description": "The management agent 1C-infrastructure",
    "author": "Vladimir Bondarevskiy",
    "author_email": "vbondarevsky@gmail.com",
    "packages": setuptools.find_packages(exclude=["tests", "tests.*"]),
    "include_package_data": True,
    "install_requires": [
        "yaml",
    ],
    "zip_safe": True,
}
setuptools.setup(**configuration)
