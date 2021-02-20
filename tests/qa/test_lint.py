import os
import unittest


def test_lint_python(project_path, run):
    cmds = [
        [os.path.join(project_path, "tools", "qa", "lint.sh"), "--pylint"],
        [
            os.path.join(project_path, "tools", "qa", "dictionary", "update.sh"),
            "--check",
        ],
    ]
    for cmd in cmds:
        run(cmd)


def test_lint_shell(project_path, run):
    cmd = [os.path.join(project_path, "tools", "qa", "lint.sh"), "--shellcheck"]
    run(cmd)


if __name__ == "__main__":
    unittest.main()
