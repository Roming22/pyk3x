import os
import unittest


def test_run(project_path, run):
    cmd = [os.path.join(project_path, "tools", "qa", "format.sh"), "--check"]
    run(cmd)


if __name__ == "__main__":
    unittest.main()
