"""Package registration"""

import os.path as path
from subprocess import run
from datetime import datetime


def generate_version() -> None:
    """Generate a unique version number in version.txt

    Version numbers are in the form `X.Y.Z` where:
      - X is the major version number
      - Y is the minor version number, odd for development releases/snapshots, even for production releases
      - Z is a revision number

    For work in progress (a.k.a feature) branches:
      - X is the year and month the release was generated
      - Y is the day and hour the release was generated
      - Z is the minute and second the release was generated
    """
    branches = run(
        ["git", "branch"], capture_output=True, check=True, text=True
    ).stdout.split("\n")

    # Get current branch
    for branch in branches:
        if branch.startswith("* "):
            branch = branch[2:]
            break

    x = y = None
    if branch.startswith("release/"):
        x, y = branch.split("/")[1].split(".")
    elif branch == "dev":
        # Get releases
        releases = (
            run(
                ["git", "ls-remote", "--heads", "origin", "release/*"],
                capture_output=True,
                check=True,
                text=True,
            )
            .stdout.strip()
            .split("\n")
        )
        print(f"branches: {releases}")
        releases = [r.split("/")[-1] for r in releases]
        releases = [(int(r.split(".")[0]), int(r.split(".")[1])) for r in releases]
        print(f"releases: {releases}")

        # Get latest release version
        x, y = sorted(releases)[-1]
        y += 1

    if x and y:
        z = len(
            run(
                ["git", "tag", "--list", f"{base_version}.*"],
                capture_output=True,
                check=True,
                text=True,
            ).stdout.split("\n")
        )
    else:
        now = datetime.utcnow()
        x = now.strftime("%y%m")
        y = now.strftime("%d%H")
        z = now.strftime("%M%S")
    version = f"{x}.{y}.{z}"

    repo_path = path.abspath(path.join(path.dirname(__file__), "..", ".."))
    version_path = path.join(repo_path, "src", "k3x", "version.txt")
    with open(version_path, "w") as file:
        file.write(f"{version}")


if __name__ == "__main__":
    generate_version()