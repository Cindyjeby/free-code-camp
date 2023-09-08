class Laptop:
    def type(self):
        print("Different types")
class Brands(Laptop):
    """creates a class Brands that inherits from Laptop"""
    def __init__(self, brand, gen):
        """defines a method"""
        self.brand = brand
        self.gen = gen

    def Hp(self):
        print("SSD")

name = Brands("elitebook", "3rd")
print(name.brand)
print(name.gen)
name.Hp()
name.type()