import aiohttp
import pytest
from web.web import WebServer

@pytest.mark.asyncio
async def test_web(web: WebServer) -> None:
    url = f"http://{web._host}:{web._port}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, raise_for_status=True) as resp:            
            assert "This is html test web" in await resp.text()
