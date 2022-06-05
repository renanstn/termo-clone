from collections import Counter

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
def letter_count():
    query = Word.get()
    secret_word = query.word
    return {"letters": len(secret_word)}


@app.post("/check")
def check_guess(guess: Guess):
    guess_word = guess.word
    query = Word.get(active=True)
    secret_word = query.word
    response = []
    win = False

    if len(guess_word) != len(secret_word):
        return {"message": "wrong number of letters"}

    countered_letters = Counter(secret_word)

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

    # Check for right letters on right positions
    for guess_letter, correct_letter in zip(guess_word, secret_word):
        if guess_letter == correct_letter:
            result = 1
            countered_letters[guess_letter] -= 1
        else:
            result = 0
        response.append({"letter": guess_letter, "result": result})

    # Check for right letters on wrong positions
    counter = 0
    for guess_letter, correct_letter in zip(guess_word, secret_word):
        if guess_letter == correct_letter:
            counter += 1
            continue
        if guess_letter in secret_word and countered_letters[guess_letter] > 0:
            result = 2
            countered_letters[guess_letter] -= 1
        else:
            result = 0
        response[counter].update({"letter": guess_letter, "result": result})
        counter += 1

    return {"result": response, "attempt": guess.attempt + 1, "win": win}
