from fastapi import APIRouter, HTTPException
from services import UserService
from dto import UserResponse,UserRequest
router_users=APIRouter(prefix="/users")

user_service=UserService()
@router_users.get("/",response_model=list[UserResponse])
def get_users():
    return user_service.get_all()

@router_users.post("/",response_model=UserResponse)
def register_user(userRequest:UserRequest):
    add_ok=user_service.creat_user(userRequest)
    if add_ok:
        return UserResponse
    raise HTTPException(status_code=404,detail="registration faild")