from setuptools import setup, find_packages

setup(
    name='midas',
    version="3.1.4",
    packages=["midas", "midas.backbones"],
    package_dirs={
        "midas": "midas",
        "midas.backbones": "midas/backbones",
    },
)
