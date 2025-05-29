import uvicorn
from uvicorn.server import Server
from fastapi import FastAPI
import os
import logging

log = logging.getLogger("main")

class FastApiServer:
    def __init__(self):
        self.server: Server = None
        self.app: FastAPI = None

    async def _startup(self):
        log.info("App is up and running")

    async def _shutdown(self):
        log.info("App is shutting down")

    def begin(self) -> FastAPI:
        self.app = FastAPI(
            title="Academic Status Classification API Service",
            description="REST API for Academic Status Classification",
            version="0.0.1"
        )
        self.app.add_event_handler("startup", self._startup)
        self.app.add_event_handler("shutdown", self._shutdown)

        # Import router disini atau sebelumnya, dan include router
        from controller.router.router import router
        self.app.include_router(router)

        config = uvicorn.Config(
            self.app,
            host=os.getenv("SERVER_HOST"),
            port=int(os.getenv("SERVER_PORT")),
            reload=True,
            log_config=None
        )
        self.server = uvicorn.Server(config)
        return self.app

    async def run(self):
        if not self.server:
            raise RuntimeError("Server is not initialized. Call begin() first.")
        await self.server.serve()

    async def close(self):
        if self.server:
            await self.server.shutdown()
