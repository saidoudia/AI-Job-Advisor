
from fastapi import APIRouter

router = APIRouter()

@router.post("/create/")
async def create_motivation_letter():
    return {"message": "Lettre de motivation créée"}
