from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel


class UserRequest(BaseModel):
    email : str
    password : str



class UserResponse(BaseModel):
    email : str
    is_admin : bool
    created_at : str
    updated_at : str
    