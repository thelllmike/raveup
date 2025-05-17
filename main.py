from fastapi import FastAPI
from database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from routers import (
    racer_router,
    emergency_contact_router,
    document_router,
    event_router,
    registration_router,
    leaderboard_router,
        auth_router,
        race_router,
        snapshot_router,
)

# create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="RevUp Racing API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] for Vite
    allow_credentials=True,
    allow_methods=["*"],  # or ["POST", "GET", "OPTIONS"]
    allow_headers=["*"],
)

app.include_router(racer_router.router, prefix="/racers", tags=["racers"])
app.include_router(emergency_contact_router.router, prefix="/contacts", tags=["emergency_contacts"])
app.include_router(document_router.router, prefix="/documents", tags=["documents"])
app.include_router(event_router.router, prefix="/events", tags=["events"])
app.include_router(registration_router.router, prefix="/registrations", tags=["registrations"])
app.include_router(leaderboard_router.router, prefix="/leaderboard", tags=["leaderboard"])
app.include_router(auth_router.router)
app.include_router(race_router.router, prefix="/races", tags=["races"])
app.include_router(snapshot_router.router)
# app.include_router(auth_router.router, prefix="/auth", tags=["auth"])
