from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import psycopg2
import os
from schemas import PersonalUserBase

class PersonalUser_db():
    def __init__(self, name, surname, email, age, city, about_me):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.city = city
        self.about_me = about_me
    def insert_user(self):
        connection = psycopg2.connect(dbname=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"), host=os.getenv("POSTGRES_HOST"), password=os.getenv("POSTGRES_PASSWORD"))
        cur = connection.cursor()
        query = """insert into udomi_ljubimca.personal_users ( name, surname, email, age, city, about_me)
             values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""".format(self.name , self.surname, self.email, self.about_me, self.city, self.age)

        try:
            cur.execute(query)
            connection.commit()
            cur.close()
            connection.close() 
            return {"message" : "the user is registered"}

        except psycopg2.OperationalError as e:
            raise e
class TestDB:
    def db_conn_check():
        try:
            conn = psycopg2.connect(dbname=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"), host=os.getenv("POSTGRES_HOST"), password=os.getenv("POSTGRES_PASSWORD"))
            cursor = conn.cursor()
            conn.close()
            return {"HEALTH" : "OK"}
        except:
            return {"HEALTH" : "UNHEALTHY"}