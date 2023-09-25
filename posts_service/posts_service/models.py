from peewee import *


db = SqliteDatabase("./base.db")

class Post(Model):
    title = CharField()
    subtitle = CharField()
    content = TextField()

    class Meta:
        database = db
