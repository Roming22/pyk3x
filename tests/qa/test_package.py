import os
import unittest


def test_run(project_path, run):
    cmd = [project_path.joinpath("tools", "qa", "package.sh")]
    run(cmd)


if __name__ == "__main__":
    unittest.main()
