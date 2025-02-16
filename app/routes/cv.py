
from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze/")
async def analyze_cv():
    return {"message": "Analyse du CV effectuée"}

@router.post("/improve/")
async def improve_cv():
    return {"message": "Amélioration du CV effectuée"}
