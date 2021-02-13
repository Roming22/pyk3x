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
    cmd = [os.path.join(project_path, "tools", "format.sh"), "--check"]
    try:
        exec(cmd)
    except Exception as ex:
        print(f"""{ex.stderr if hasattr(ex, "stderr") else ex}""")
        assert False


def test_linting(project_path, exec):
    cmd = [os.path.join(project_path, "tools", "lint.sh")]
    try:
        exec(cmd)
    except Exception as ex:
        print(f"""{ex.stderr if hasattr(ex, "stderr") else ex}""")
        assert False


if __name__ == "__main__":
    unittest.main()
