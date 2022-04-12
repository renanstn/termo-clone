from decouple import config


DATABASE_URL = config(
    "DATABASE_URL", default="postgresql://postgres:postgres@database/termo"
)
