import logging
import uvicorn
from fastapi import FastAPI, status
from crud import PersonalUser_db

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

app = FastAPI()

@app.get("/health")
async def index():
    return {"HEALTH" : "OK"}

@app.get("/health-db")
async def testdb():
    test_conn = PersonalUser_db.db_conn_check()
    if test_conn["HEALTH"] == "OK":
        return test_conn
    else:
        return test_conn

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")