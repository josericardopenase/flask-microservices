from peewee import *


db = SqliteDatabase("./base.db")

class Car(Model):
    plate_number = CharField()
    model = CharField()

    class Meta:
        database = db
