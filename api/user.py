from fastapi import APIRouter

router = APIRouter(prefix = "users")

@router.post("/sign-up",status_code=201)
async def user_sign_up_handler():
    #1.request body(username, password)
    #2. password -> hashing -> hashed_password
    #3.User(username, hashed_password)
    #4.user -> db save
    #5. return user(id, username)
    return True