import os
import unittest
from subprocess import CalledProcessError


def test_formatting(project_path, run):
    cmd = [os.path.join(project_path, "tools", "format.sh"), "--check"]
    try:
        run(cmd)
    except CalledProcessError as ex:
        print(f"""{ex.stderr}""")
        assert False
    except Exception as ex:
        print(f"""{ex}""")
        assert False


def test_linting(project_path, run):
    cmd = [os.path.join(project_path, "tools", "lint.sh")]
    try:
        run(cmd)
    except CalledProcessError as ex:
        print(f"""{ex.stderr}""")
        assert False
    except Exception as ex:
        print(f"""{ex}""")
        assert False


if __name__ == "__main__":
    unittest.main()
