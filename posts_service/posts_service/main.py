from flask import Flask, request
import datetime
from serializer import PostSerializer
from models import Post, db
import jwt

app = Flask(__name__)

db.connect()
db.create_tables([Post])

@app.route("/posts", methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        posts = Post.filter()
        json = []
        for post in posts:
            json.append(PostSerializer(post).to_json())
        return json
    if request.method == 'POST':
        data = request.get_json()
        post = Post(title=data['title'], subtitle=data['subtitle'], content=data['content'])
        post.save()
        return PostSerializer(post).to_json()

if __name__ == '__main__':
    app.run("0.0.0.0", port=5004)



