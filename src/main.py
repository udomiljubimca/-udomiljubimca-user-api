import logging
import uvicorn
from fastapi import FastAPI, status
from crud import PersonalUser_db, TestDB
from schemas import PersonalUserBase
from pydantic import BaseModel
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

app = FastAPI()

@app.post("/insert-user")
async def asasign_userDB(item : PersonalUserBase):
    status = PersonalUser_db(item.name, item.surname, item.email, item.about_me, item.city, item.age).insert_user()
    return {"message" : status["message"]}
@app.get("/health")
async def index():
    return {"HEALTH" : "OK"}

@app.get("/health-db")
async def testdb():
    test_conn = TestDB.db_conn_check()
    if test_conn["HEALTH"] == "OK":
        return test_conn
    else:
        return test_conn

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")