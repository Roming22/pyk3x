import os
from subprocess import run as sp_run

from pytest import fixture


@fixture
def project_path():
    return os.path.abspath(os.getcwd())


@fixture
def run():
    def func(cmd):
        sp_run(cmd, capture_output=True, check=True, text=True)

    return func
