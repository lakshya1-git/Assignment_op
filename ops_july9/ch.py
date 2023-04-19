class car:
    def __init__(self, body, engine, tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre
        
    def mileage(self):
        print("Mileage of a car")
        
c = car("second_hand", "v5", "mrf")

class tata(car):
    pass

t = tata("sedan", "turbo", "bridgestone")
print(t.body, t.engine, t.tyre)
t.mileage()