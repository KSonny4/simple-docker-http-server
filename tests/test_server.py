# type: ignore
import aiohttp
import pytest

from web.web import WebServer


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "url_route",
    ["", "index.html", "text", "test/test/" * 50, "../../.."],
)
async def test_web(web: WebServer, url_route: str) -> None:
    url = f"http://{web._host}:{web._port}/{url_route}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, raise_for_status=True) as resp:
            assert "This is html test web" in await resp.text()
