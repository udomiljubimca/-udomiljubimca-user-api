import logging
import uvicorn
from fastapi import FastAPI, status
import psycopg2

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

app = FastAPI()

@app.get("/health")
async def index():
    return {"HEALTH" : "OK"}

@app.get("/health-db")
async def testdb():
    try:
        conn = psycopg2.connect(dbname="$POSTGRES_DB", user="$POSTGRES_USER", host="$POSTGRES_URL", password="$POSTGRES_PASSWORD")
        conn.close()
        return {"HEALTH" : "OK"}
    except:
        return {"HEALTH" : "UNHEALTHY"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")