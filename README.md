# RevUp Racing API

FastAPI backend for managing racers, events, registrations, emergency contacts, documents, and leaderboards.

## Features

- CRUD operations for:
  - **Racers** (profiles with authentication)
  - **Emergency Contacts**
  - **Racer Documents** (ID/passport uploads)
  - **Events** (racing competitions)
  - **Registrations** (event sign-ups)
  - **Leaderboard** (rankings, points, lap times)
- MySQL (via SQLAlchemy) database integration
- Pydantic models for data validation
- Automatic Swagger UI at `/docs`
- Password hashing with bcrypt

## Prerequisites

- Python 3.10+
- MySQL server (create database `raveup`)
- MySQL Workbench (optional, for managing DB)
- Git (optional)

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/revup-backend.git
   cd revup-backend

   your_project/
├── .env             # environment variables
├── .gitignore       # ignored files
├── database.py      # DB connection and Base model
├── main.py          # FastAPI app and router registrations
├── models/          # SQLAlchemy ORM models
├── schemas/         # Pydantic request/response models
├── crud/            # CRUD utility functions
└── routers/         # API route definitions