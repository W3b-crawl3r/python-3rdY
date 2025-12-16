from services import UserService
from config import Base, LocalSession,engine
from dto import *
import uvicorn
from fastapi import FastAPI
from controller import router_users
#creat alls tables once
def init_db():
    Base.metadata.create_all(bind=engine)

app=FastAPI(title="Banking API ",version="1.0")
app.include_router(router_users)
if __name__=='__main__':
    init_db()
    uvicorn.run("main:app",host="0.0.0.0")







    """ init_db()
    user_1:UserRequest=UserRequest(email="u1@app.com",password='1234')
    user_2:UserRequest=UserRequest(email="u2@app.com",password='1234')
    userService:UserService=UserService()
    userService.creat_user(user_1)
    userService.creat_user(user_2)

    users:list[UserResponse]=userService.get_all()
    print(users) """








    """ acc:Account = CheckingAccount(500,1000)

    acc.withdraw(500)
    acc.withdraw(300)
    acc.deposit(800)
    for c in acc.transactions:
        print(c)
    print(acc.amount) """