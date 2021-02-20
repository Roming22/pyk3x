from pathlib import Path

from pytest import fixture


@fixture
def project_path():
    return Path(__file__).parent.parent
