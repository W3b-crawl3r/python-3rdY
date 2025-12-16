from dal import UserDao
from config import LocalSession
from dto import *
from entities import User
class UserService:

    def __init__(self) -> None:
        self.session = LocalSession()
    def creat_user(self,userRequest:UserRequest):
        user:User=User(email=userRequest.email,password=userRequest.password) 
        return UserDao.creat_user(self.session,user)
    def get_all(self)->list[UserResponse]:
        users:list[UserResponse]=[]
        for user in UserDao.get_all_users(self.session):
            users.append(UserResponse(email=str(user.email),is_admin=bool(user.is_admin),
                                    created_at=str(user.created_at),updated_at=str(user.updated_at)))
        return users