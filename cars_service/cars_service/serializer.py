class CarSerializer:

    def __init__(self, car):
        self.car = car

    def to_json(self):
        return {
                "plate_number" : self.car.plate_number,
                "model" : self.car.model,
        }
