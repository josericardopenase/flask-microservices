from models import Car, db

db.connect()
db.create_tables([Car])
