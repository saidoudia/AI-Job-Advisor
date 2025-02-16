
from fastapi import APIRouter

router = APIRouter()

@router.get("/details/")
async def get_profile_details():
    return {"message": "Détails du profil récupérés"}
