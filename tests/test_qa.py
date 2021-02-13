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
    cmds = [
        [os.path.join(project_path, "tools", "lint.sh")],
        [os.path.join(project_path, "tools", "dictionary", "update.sh"), "--check"],
    ]
    for cmd in cmds:
        try:
            run(cmd)
        except CalledProcessError as ex:
            print(f"""{ex.stderr}""")
            assert False
        except Exception as ex:
            print(f"""{ex}""")
            assert False


def test_type_checking(project_path, run):
    cmd = [os.path.join(project_path, "tools", "type_check.sh")]
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
