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
    word = guess.word
    secret_world = Word.get()
    print(secret_world.word)
    return word
