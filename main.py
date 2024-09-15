from fastapi import FastAPI
import uvicorn
from fastapi_site.routers import http_test

app = FastAPI()

app.include_router(http_test.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)