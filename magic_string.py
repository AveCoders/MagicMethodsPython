class Car:
    def __init__(self, make, model, price):
        super().__init__()
        self.make = make
        self.model = model
        self.price = price
        self._discount = 0.25

    def __call__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
        self._discount = 0.25

    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("Price must be float!")
        return super().__setattr__(name, value)    

    def __getattr__(self, name):
        return name + " not implemented"

    def __str__(self):
        return f"{self.make}{self.model} costs {self.price}"

    def __repr__(self):
        return f"make={self.make}, model={self.model}, price={self.price}"

    def __eq__(self, value):
        if not isinstance(value, Car):
            raise ValueError("Can't compare because of type mismatch")
        return (self.make == value.make and 
                self.model == value.model and
                self.price == value.price)

    def __ge__(self, value):
        if not isinstance(value, Car):
            raise ValueError("Can't compare because of type mismatch")
        return self.price >= value.price

    def __lt__(self, value):
        if not isinstance(value, Car):
           raise ValueError("Can't compare because of type mismatch") 
        return self.price < value.price

# car1 = Car("Toyota", "Camri", 7000)
# car2 = Car("Opel", "Mokka", 14000)
# car3 = Car("Unknown", "Junk_wagon", 14)


# Swap your old car for a discount
car1 = Car("Toyota", "Camri", float(7500))
print(car1)
# car1 = ("WV","Passat", 4500.69)
# print(car1)
car1("Porsche", "Carrera", 6700000.00)
print(car1.__dict__)
# print(str(car1))
# print(repr(car2))

# print (car2 == car3)
# print (car2 == car1)

# print(car2 >= car1)
# print(car2 < car3)


# cars = [car1, car2, car3]
# cars.sort()
# print([car.model for car in cars])