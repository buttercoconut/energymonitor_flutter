from fastapi import FastAPI
from routers import energy, users
from database import engine, Base

app = FastAPI(title="Energy Monitor API")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(energy.router, prefix="/energy", tags=["energy"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to Energy Monitor API"}
