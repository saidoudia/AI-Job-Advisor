
from fastapi import APIRouter

router = APIRouter()

@router.get("/search/")
async def search_jobs():
    return {"message": "Recherche d'emplois en cours"}
