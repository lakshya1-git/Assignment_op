class ineuron:
    def __init__(self,name):
        self.name = name
        print("Name of the student is ",self.name)
class batch(ineuron):
    def __init__(self,course):
        self.course = course
        name = "check"
        print("COurse registered is ",self.course)
class year_ch(batch):
    def __init__(self,year):
        super().__init__(batch)
        self.year = year
        print("Joined in year ", self.year)
        print("Courser registered to  ", batch.course)
i = ineuron("lskdhys")
b = batch("mca")
y = year_ch("1998")
print("Name of student is ",i.name)
print(b.ch_batch("Data Science"))
print(y.ch_year("2022"))
print(i.name) #call name from Ineuron class
print(b.name) # call name from batch class