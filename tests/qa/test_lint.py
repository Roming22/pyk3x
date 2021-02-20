import os
import unittest


def test_lint(project_path, run):
    cmds = [
        [os.path.join(project_path, "tools", "qa", "lint.sh")],
        [
            os.path.join(project_path, "tools", "qa", "dictionary", "update.sh"),
            "--check",
        ],
    ]
    for cmd in cmds:
        run(cmd)


if __name__ == "__main__":
    unittest.main()
