import pytest

from web.web import WebServer


@pytest.fixture
async def web():  # type: ignore
    web = WebServer(host="127.0.0.1", port=8080)
    await web.start_web_server()
    yield web
    await web.close()
