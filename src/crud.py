from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import psycopg2
import os
from schemas import PersonalUserBase

class PersonalUser_db():
    def __init__(self, name, surname, email, age, city, about_me, terms_and_condition_accepted):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.city = city
        self.about_me = about_me
        self.terms_and_condition_accepted = terms_and_condition_accepted
    def get_users():
        lis_of_users = []
        try:
            connection = psycopg2.connect(dbname=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"), host=os.getenv("POSTGRES_HOST"), password=os.getenv("POSTGRES_PASSWORD"))
            cursor = connection.cursor()
            cursor.execute("select * from userservice.personal_users;")
            row_query = cursor.fetchall()
            connection.close()
            return {"users" : row_query, "check" : True}
        except:
            return {"check" : False}
    def insert_user(self):
        try:
            connection = psycopg2.connect(dbname=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"), host=os.getenv("POSTGRES_HOST"), password=os.getenv("POSTGRES_PASSWORD"))
            cursor = connection.cursor()
            query = """insert into userservice.personal_users ( name, surname, email, age, city, about_me, terms_and_condition_accepted)
             values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')""".format(self.name , self.surname, self.email, self.about_me, self.city, self.age, self.terms_and_condition_accepted)
            cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close() 
            return {"check" : True}

        except psycopg2.OperationalError as e:
            raise e
            
    def test():
        conn_url = 'postgresql+psycopg2://udomiljubimca:TestPassword123@user-service-postgres-dev/user-service'
        engine = create_engine(conn_url)

        db = scoped_session(sessionmaker(bind=engine))

        query_rows = db.execute("SELECT * FROM userservice.personal_users;").fetchall()
        for register in query_rows:
            return{"test" : f"{register.name}"}

class TestDB:
    def db_conn_check():
        try:
            connection = psycopg2.connect(dbname=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"), host=os.getenv("POSTGRES_HOST"), password=os.getenv("POSTGRES_PASSWORD"))
            cursor = connection.cursor()
            connection.close()
            return {"HEALTH" : "OK"}
        except:
            return {"HEALTH" : "UNHEALTHY"}

