
from sqlalchemy.orm import Session
from entities import User
from typing import Optional
class UserDao:
    @staticmethod
    def creat_user(session:Session,user:User)->bool:
        #check for uniq email
        filtred_user:Optional[User]=session.query(User).filter(User.email == user.email).one_or_none()
        if filtred_user:
            return False
        session.add(user)
        try :
            session.commit()
            session.refresh(user)
            return True
        except :
            session.rollback()
            return False
    @staticmethod
    def get_all_users(session:Session):
        return session.query(User).all()