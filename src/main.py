import logging
import uvicorn
from fastapi import FastAPI

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

app = FastAPI()

@app.get("/health")
async def index():
    return {"HEALTH" : "OK"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")