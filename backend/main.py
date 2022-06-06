from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Guess, Word
from database import init_database
import settings
from game_logic import word_checker


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
def letter_count():
    query = Word.get()
    secret_word = query.word
    return {"letters": len(secret_word)}


@app.post("/check")
def check_guess(guess: Guess):
    guess_word = guess.word
    query = Word.get(active=True)
    secret_word = query.word
    win = False

    if len(guess_word) != len(secret_word):
        return {"message": "wrong number of letters"}

    # Check win case
    if guess_word == secret_word:
        win = True
        return {
            "result": [
                {"letter": letter, "result": 2} for letter in guess_word
            ],
            "attempt": guess.attempt + 1,
            "win": win,
        }

    results = word_checker(guess_word, secret_word)

    return {"result": results, "attempt": guess.attempt + 1, "win": win}
