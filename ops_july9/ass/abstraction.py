class abc:
    def check_fun(self):
        pass
class ab(abc):
    def check_fun(self):
        print("Vlaue of abv")
class ac(ab):
    def check_fun(self):
        print("print value of ab")
class abcd(ac):
    def check_fun(self):
        print("vlaue of a")
b = ab()
b.check_fun()
a = ac()
d = abcd()


