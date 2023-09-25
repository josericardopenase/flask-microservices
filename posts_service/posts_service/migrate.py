from models import Post, db

db.connect()
db.create_tables([Post])
