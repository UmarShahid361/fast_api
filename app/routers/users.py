from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def get_users():
    return {
        "id": 1,
        "name": "Umar"
    }
