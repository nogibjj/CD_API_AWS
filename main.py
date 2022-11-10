""" import neccessary libs"""
from fastapi import FastAPI
import uvicorn

api = FastAPI()


@api.get("/")
async def root():
    """Root page"""
    return {"message": "Hello, this is scratch of Data Engineering api"}


if __name__ == "__main__":
    uvicorn.run(api, port=8080, host="0.0.0.0")
