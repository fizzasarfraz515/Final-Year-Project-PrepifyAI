from fastapi import APIRouter, Depends, HTTPException, status

from app.services.user_service import UserService

router = APIRouter(tags=["auth"])


@router.post("/login")
async def login(username: str, password: str, service: UserService = Depends(UserService)):
    token = service.authenticate(username=username, password=password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}


@router.post("/signup")
async def signup(username: str, password: str, service: UserService = Depends(UserService)):
    user = service.create_user(username=username, password=password)
    return {"id": user["id"], "username": user["username"]}
