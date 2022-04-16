from decouple import config


DATABASE_URL = config(
    "DATABASE_URL", default="postgresql://postgres:postgres@database/termo"
)
ORIGINS = [
    "http://localhost:8080",
]
