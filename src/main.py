import logging
import uvicorn
from fastapi import FastAPI, status, HTTPException
from crud import PersonalUser_db, TestDB
from schemas import PersonalUserBase
from pydantic import BaseModel

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

app = FastAPI()
@app.get("/get-users")
async def get_all_users():
    users = PersonalUser_db.get_users()
    if users["check"] == True:
        return {"message" : users['users']}
    else:
        raise HTTPException(status_code = 404, detail = "Nothing found!")

@app.post("/insert-user")
async def asasign_userDB(item : PersonalUserBase):
    status = PersonalUser_db(item.name, item.surname, item.email, item.about_me, item.city, item.age, item.terms_and_condition_accepted).insert_user()
    if status["check"] == True:
        return {"message" : "User is registred!"}
    else:
        raise HTTPException(status_code = 406, detail = "Canot find any content!")

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
@app.get('/test')
async def testsql():
    s = PersonalUser_db.test()
    return{"text" : s['test']}
if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")