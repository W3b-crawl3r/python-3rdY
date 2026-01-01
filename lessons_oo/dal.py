
from sqlalchemy.orm import Session
from entities import User
from typing import Optional
class UserDao:
    @staticmethod
    def search_by_email(session:Session,email:str)->User:
        #check for uniq email
        return session.query(User).filter(User.email == email).one_or_none()
    @staticmethod
    def delete_user(session:Session,email:str)->bool:
        #check for uniq email
        filtred_user:Optional[User]=UserDao.search_by_email(session,email)
        if filtred_user:
            session.delete(filtred_user)
            return True
        return False
    @staticmethod
    def creat_user(session:Session,user:User)->bool:
        #check for uniq email
        filtred_user:Optional[User]=UserDao.search_by_email(session,str(user.email))
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
    