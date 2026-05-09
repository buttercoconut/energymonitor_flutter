"""FastAPI application entry point."""

from fastapi import FastAPI
from routers import auth as auth_router, energy as energy_router

app = FastAPI(title="Energy Monitor API")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(energy_router, prefix="/energy", tags=["energy"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Energy Monitor API"}
