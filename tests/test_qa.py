import os
import unittest

from pytest import fixture
from subprocess import run


@fixture
def project_path():
    return os.path.abspath(os.getcwd())


@fixture
def exec():
    def func(cmd):
        run(cmd, capture_output=True, check=True, text=True)

    return func


def test_formatting(project_path, exec):
    cmd = ["black", "--check", project_path]
    try:
        exec(cmd)
    except Exception as ex:
        print(f"{ex.stderr}")
        assert False


if __name__ == "__main__":
    unittest.main()
