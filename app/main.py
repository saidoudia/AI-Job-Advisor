# app/main.py
from fastapi import FastAPI
from app.routes import cv, motivation, jobs, profile

app = FastAPI()

# Inclure les routes pour chaque fonctionnalité
app.include_router(cv.router, prefix="/cv", tags=["CV"])
app.include_router(motivation.router, prefix="/motivation", tags=["Motivation"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(profile.router, prefix="/profile", tags=["Profile"])
   


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Bienvenue dans l'API AI-Job-Advisor."}

# Assure-toi qu'il n'y a pas d'espaces ou tabulations inattendues


