from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Guess, Word
from database import init_database
import settings


init_database()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/letter_count")
def letter_cont():
    query = Word.get()
    secret_word = query.word
    return {"letters": len(secret_word)}


@app.post("/check")
def check_guess(guess: Guess):
    guess_word = guess.word
    query = Word.get()
    secret_word = query.word
    response = []

    if len(guess_word) != len(secret_word):
        return {"message": "wrong number of letters"}

    for guess_letter, correct_letter in zip(guess_word, secret_word):
        if guess_letter == correct_letter:
            response.append(1)
        elif guess_letter in secret_word:
            response.append(2)
        else:
            response.append(0)

    return {"result": response}
