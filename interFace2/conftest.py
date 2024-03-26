import pytest


@pytest.fixture()
def context():
    return {
        "host": "127.0.0.1",
        "port": 5000
    }
