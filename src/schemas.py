from pydantic import BaseModel

class PersonalUserBase(BaseModel):
    name: str
    surname: str
    email: str
    terms_and_condition_accepted: str
    about_me: str
    city: str
    age: int