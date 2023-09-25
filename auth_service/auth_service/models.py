from peewee import *


db = SqliteDatabase("./base.db")

class User(Model):
    email = CharField(index=True, unique=True)
    password = CharField()

    class Meta:
        database = db

class Token(Model):
    token = CharField(index=True, unique=True)
    user = ForeignKeyField(User, backref='user')

    class Meta:
        database = db
