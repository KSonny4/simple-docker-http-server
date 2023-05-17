import asyncio
import logging
import os
from typing import Tuple
import aiofiles
from aiohttp import web
from typing import Any, Dict

from pathlib import Path
import json
logger = logging.getLogger(__name__)


class WebServer:
    def __init__(
        self,
        host: str,
        port: int,
    ):
        self._host = host
        self._port = port
        self._web_app = web.Application()
        self._runner = web.AppRunner(self._web_app)
        self._response_json = None

    async def get_json_response(self) -> Dict[Any, Any]:
       # read file response.json using aiofiles
       file_path = Path(os.path.dirname(__file__) , "response.json") 
       async with aiofiles.open(file_path.resolve(), mode="r") as f:
            return json.loads(await f.read())

    def _add_routes(self) -> None:
        self._web_app.router.add_route("GET", "/{tail:.*}", self._get_json)
        self._web_app.router.add_route("HEAD", "/{tail:.*}", self._get_json)

    async def start_web_server(self) -> None:
        self._add_routes()
        await self._runner.setup()
        site = web.TCPSite(self._runner, self._host, self._port)
        self._response_json = await self.get_json_response()
        await site.start()

    async def _get_json(self, _request: web.Request) -> web.Response:
        return web.json_response(self._response_json)

    async def close(self) -> None:
        await self._runner.cleanup()


def setup() -> Tuple[str, int]:
    try:
        host = os.environ["HOST"]
        logger.info("Host is %s", host)
    except KeyError:
        host = "0.0.0.0"
        logger.warning("Host was not provided via env. variable HOST, used %s", host)
    try:
        port = int(os.environ["PORT"])
        logger.info("Port is %s", port)
    except KeyError:
        port = 8888
        logger.warning("Port was not provided via env. variable PORT, used %s", port)
    logger.info(f"Connect to http://%s:%s", host, port)
    return host, port


async def async_main() -> None:
    host, port = setup()
    web = WebServer(host, port)

    try:
        await web.start_web_server()
        while True:
            await asyncio.sleep(60)
    except KeyboardInterrupt:
        pass
    finally:
        await web.close()


def main() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
