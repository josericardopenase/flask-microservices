from models import User, db

db.connect()
db.create_tables([User])
