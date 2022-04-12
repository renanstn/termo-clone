import peewee
from pydantic import BaseModel


database_proxy = peewee.DatabaseProxy()


class Guess(BaseModel):
    """
    Guess model, to be received on request body
    """

    word: str
    player: str


class Word(peewee.Model):
    """
    Word model, to be stored on database
    """

    word = peewee.CharField()
    active = peewee.BooleanField()

    class Meta:
        database = database_proxy
