from flask import Flask, request
import datetime
from serializer import CarSerializer
from models import Car, db
import jwt

app = Flask(__name__)

db.connect()
db.create_tables([Car])

@app.route("/cars", methods=['GET', 'POST'])
def cars():
    if request.method == 'GET':
        cars = Car.filter()
        json = []
        for car in cars:
            json.append(CarSerializer(car).to_json())
        return json
    if request.method == 'POST':
        data = request.get_json()
        car = Car(plate_number=data['plate_number'], model = data['model'])
        car.save()
        return CarSerializer(car).to_json()

if __name__ == '__main__':
    app.run("0.0.0.0", port=5005)



