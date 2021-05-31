from pydantic import BaseModel

class PersonalUserBase(BaseModel):
    name: str
    surname: str
    email: str
    about_me: str
    city: str
    age: int
    terms_and_condition_accepted : str