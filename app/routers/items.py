from fastapi import APIRouter

router = APIRouter()


@router.get("/items/", tags=["items"])
async def get_users():
    return {
        "id": 1,
        "name": "Item # 1"
    }
