import logging
import uvicorn
from fastapi import FastAPI, status
import psycopg2
import os

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

app = FastAPI()

@app.get("/health")
async def index():
    return {"HEALTH" : "OK"}

@app.get("/health-db")
async def testdb():
    try:
        conn = psycopg2.connect(dbname=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"), host=os.getenv("POSTGRES_HOST"), password=os.getenv("POSTGRES_PASSWORD"))
        conn.close()
        return {"HEALTH" : "OK"}
    except:
        return {"HEALTH" : "UNHEALTHY"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")