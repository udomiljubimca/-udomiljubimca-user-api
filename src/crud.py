from sqlalchemy.orm import Session
import psycopg2
import os


class PersonalUser_db():
    def __init__(self):
        pass

    def insert_user():
        pass

    def db_conn_check():
        try:
            conn = psycopg2.connect(dbname=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"), host=os.getenv("POSTGRES_HOST"), password=os.getenv("POSTGRES_PASSWORD"))
            conn.close()
            return {"HEALTH" : "OK"}
        except:
            return {"HEALTH" : "UNHEALTHY"}