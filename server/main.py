from config.server import FastApiServer
from dotenv import load_dotenv
import os

load_dotenv(override=True)

server = FastApiServer()
app = server.begin()

if __name__ == "__main__":
    import asyncio, traceback, logging
    from dotenv import load_dotenv
    from util.log import log_begin

    load_dotenv(override=True)
    log_begin()
    log = logging.getLogger("main")

    async def main():
        await server.run()

    try:
        asyncio.run(main())
    except (Exception, KeyboardInterrupt):
        log.info(traceback.format_exc())
