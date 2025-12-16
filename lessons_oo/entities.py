from config import Base
from sqlalchemy import Column, Integer, String, DateTime, func, Boolean

class User(Base):
    __tablename__='t_user'
    id=Column(Integer,primary_key=True)
    email=Column(String(255),nullable=False,unique=True,index=True)
    password=Column(String(128),nullable=False)
    is_admin=Column(Boolean,default=False)
    created_at=Column(DateTime,server_default=func.now())
    updated_at=Column(DateTime,server_onupdate=func.now())