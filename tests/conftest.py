import pytest # type: ignore

from web.web import WebServer


@pytest.fixture
async def web():
    web = WebServer(host="127.0.0.1", port=8080)
    await web.start_web_server()
    yield web
    await web.close()
