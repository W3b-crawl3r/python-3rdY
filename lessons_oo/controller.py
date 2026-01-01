from fastapi import APIRouter, HTTPException,Response
from services import UserService
from dto import UserResponse,UserRequest
router_users=APIRouter(prefix="/users")

user_service=UserService()
@router_users.get("/",response_model=list[UserResponse])
def get_users():
    return user_service.get_all()

@router_users.delete("/{email}")
def delete_user(email:str):
    delete_ok=user_service.delete_user(email)
    if delete_ok:
        return Response(status_code=201,content='deleted ok')
    raise HTTPException(status_code=404,detail="email not found")

@router_users.post("/",response_model=UserResponse)
def register_user(userRequest:UserRequest):
    add_ok=user_service.creat_user(userRequest)
    if add_ok:
        return UserResponse(email=userRequest.email,is_admin=False,created_at='',updated_at='')
    raise HTTPException(status_code=404,detail="registration faild")

@router_users.get("/{email}",response_model=UserResponse)
def search_by_email(email: str)->UserResponse:
    filtred_user = user_service.search_by_email(email)
    if filtred_user:
        return UserResponse(email=str(filtred_user.email),is_admin=bool(filtred_user.is_admin),
                            created_at=str(filtred_user.created_at),updated_at=str(filtred_user.updated_at))
    raise HTTPException(status_code=504,detail="user not found")

@router_users.put("/",response_model=UserResponse)
def update(userRequest:UserRequest):
    pass