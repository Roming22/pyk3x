import os
import unittest
from subprocess import run

from pytest import fixture


@fixture
def project_path():
    return os.path.abspath(os.getcwd())


@fixture
def exec():
    def func(cmd):
        run(cmd, capture_output=True, check=True, text=True)

    return func


def test_formatting(project_path, exec):
    cmds = [
        ["isort", "--check", "--profile=black", project_path],
        ["black", "--check", project_path],
    ]
    for cmd in cmds:
        try:
            exec(cmd)
        except Exception as ex:
            print(f"{ex.stderr}")
            assert False


if __name__ == "__main__":
    unittest.main()
