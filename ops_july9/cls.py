class car:
    def __init__(self, body, engin, tube):
        self.body = body
        self.engin = engin
        self.tube = tube
    def milage(self):
        print("Milegae of the this car")
c = car('sod', " bo", "hg")
class tata(car):
    pass
oj = tata("body- solid", "y6", "radical")
print(oj.tube)
oj.milage()
