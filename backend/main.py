from urllib import response
from fastapi import FastAPI

from models import Guess, Word
from database import init_database


init_database()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/check")
def check_guess(guess: Guess):
    guess_word = guess.word
    query = Word.get()
    secret_world = query.word
    response = []

    if len(guess_word) != len(secret_world):
        return {"message": "wrong number of letters"}

    for guess_letter, correct_letter in zip(guess_word, secret_world):
        if guess_letter == correct_letter:
            response.append(1)
        elif guess_letter in secret_world:
            response.append(2)
        else:
            response.append(0)

    return {"result": response}
