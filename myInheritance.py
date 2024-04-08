class Car:
    def __init__(self, ctype, color):
        self.ctype = ctype
        self.color = color

    def info(self):
        print(f"Car is a {self.ctype} and is the color {self.color}.")

    def changeColor(self, color):
        self.color = color
        print(f"You've changed the color of your vehicle.")


class AutoRetailer(Car):
    def __init__(self, ctype, color, cost):
        super().__init__(ctype, color)
        self.cost = cost

    def forSaleInfo(self):
        print(f"Vehicle for sale: \nType: {self.ctype}\nColor: {self.color}\nCost: ${self.cost}")


vehicleOne = Car('Sedan', 'Blue')
vehicleOne.info()
vehicleForSaleOne = AutoRetailer('Hatchback', 'Red', 5000)
vehicleForSaleOne.info()
vehicleForSaleOne.forSaleInfo()


