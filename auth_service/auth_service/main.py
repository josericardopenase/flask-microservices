from flask import Flask, request
import datetime
from models import User, Token, db
import jwt

app = Flask(__name__)

db.connect()
db.create_tables([User])

@app.route("/auth/login", methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        user = User.get(email=email)
        token = jwt.encode({"email" : email}, password, algorithm="HS256")

        if token == user.password:
            return {
                    "token" : user.password
            }
        else:
            return {
                    "status": "400",
                    "error" : "Invalid username or password"
            }
    except:
        return {
                "status": "500",
                "error" : "Internal server error"
        }

@app.route("/auth/register", methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']

        if len(User.filter(email=email)) > 0:
            return {
                    "status": "400",
                    "error" : "User does exist"
            }

        token = jwt.encode({"email" : email}, password, algorithm="HS256")
        user = User(email=email, password=token)
        user.save()

        return {
                "token" : user.password
        }
    except:
        return {
                "status": "500",
                "error" : "Internal server error"
        }
if __name__ == '__main__':
    app.run(host='auth', port=5003)

