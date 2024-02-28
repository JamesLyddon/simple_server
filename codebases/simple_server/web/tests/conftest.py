import pytest
from codebases.simple_server.web.app import app

@pytest.fixture
def web_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
