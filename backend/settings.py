from decouple import config


DATABASE_URL = config(
    "DATABASE_URL", default="postgresql://postgres:postgres@db/termo"
)
ORIGINS = [
    "http://localhost:8002",  # frontend address
]
