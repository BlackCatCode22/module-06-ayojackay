class Car:
    def __init__(self):
        self.ctype = 'Sedan'

    def info(self):
        print(f'Vehicle type is {self.ctype}.')

vehicleOne = Car()

print("type is:", type(vehicleOne))
print("dir is:", dir(vehicleOne))
print("type of vehicleOne.info is:", type(vehicleOne.info))
vehicleOne.info()