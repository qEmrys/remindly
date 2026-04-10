# Remindly

## Setup

cp .env.example .env

docker-compose up -d

## Apply migrations

alembic upgrade head

## Run app

uvicorn app.main:app --reload

## Endpoints

GET /api/health
POST /api/reminders
GET /api/reminders
GET /reminders/{id} 
PATCH /reminders/{id}
DELETE /reminders/{id}