import os
import unittest


def test_run(project_path, run):
    coverage_path = project_path.joinpath("tools", "qa", "coverage")
    cmd = [
        "diff",
        coverage_path.joinpath("report.ref"),
        coverage_path.joinpath("report.txt"),
    ]
    run(cmd)


if __name__ == "__main__":
    unittest.main()
