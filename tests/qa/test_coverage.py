import os
import unittest


def test_run(project_path, run):
    coverage_path = os.path.join(project_path, "tools", "qa", "coverage")
    cmd = [
        "diff",
        os.path.join(coverage_path, "report.ref"),
        os.path.join(coverage_path, "report.txt"),
    ]
    run(cmd)


if __name__ == "__main__":
    unittest.main()
