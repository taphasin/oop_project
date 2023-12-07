from typing import Union

from fastapi import FastAPI

class System:
    def __init__(self):
        self.user_list = []
    
    def add_user_in_user_list(self, user):
        self.user_list.append(user) 

    def prin(self, nam):
        for i in self.user_list:
            if nam == i.firstname:
                return i.mobile 

class Register:
    def __init__(self, nprefix, fname, lname ,email ,mobile ,password):
        self.nameprefix = nprefix
        self.firstname = fname
        self.lastname = lname
        self.email = email
        self.mobile = mobile
        self.password = password 
    

system = System()
user1 = Register("Mr", "Racha",  "Tanagtaghoul", "racha@gmail.com","0816638801", "paul11")
system.add_user_in_user_list(user1)

app = FastAPI()


@app.get("/")
async def read_root(name : str):
    people = system.prin(name)
    print(people)
    return {"name" : people}