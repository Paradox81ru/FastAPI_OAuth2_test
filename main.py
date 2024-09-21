from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_site.routers import http_test
from fastapi_site.middlewares.authentication import JWTTokenAuthBackend
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware import Middleware

import uvicorn

app = FastAPI()

app.include_router(http_test.router, prefix="/api")
app.add_middleware(AuthenticationMiddleware, 
                   backend=JWTTokenAuthBackend(),
                   on_error=lambda conn, exc: JSONResponse({"detail": str(exc)}, status_code=401)
                   )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)