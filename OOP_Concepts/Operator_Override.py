class A:
    def __init__(self,pname,psalary,pfees):
        self.name = pname
        self.salary = psalary
        self.fees = pfees

    def __add__(self, other):
        return  self.salary + other.salary

    def __repr__(self):
        return f"{self.name}"

obj = A("Hammad",50000, 10000)
obj2 = A("Sajid",5000, 2000)
var = (obj+obj2)
print(var)

print(obj2)

'''Dunder method use'''