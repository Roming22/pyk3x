import os
import unittest


def test_type_check(project_path, run):
    cmd = [os.path.join(project_path, "tools", "qa", "type_check.sh")]
    run(cmd)


if __name__ == "__main__":
    unittest.main()
