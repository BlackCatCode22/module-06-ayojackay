class Car:
    def __init__(self, ctype, color):
        self.ctype = ctype
        self.color = color

    def info(self):
        print(f"Car is a {self.ctype} and is the color {self.color}.")

    def __del__(self):
        print("I've destructed. ", self.ctype)


vehicleOne = Car('Sedan', 'Red')
vehicleOne.info()
vehicleTwo = Car('Hatchback', 'Blue')
vehicleTwo.info()

