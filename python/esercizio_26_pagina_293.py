class square:

    def __init__(self, side):
        self.side = side

    def area(self):
        self.area = self.side ** 2

    def perimeter(self):
        self.perimeter = self.side * 4

class rectangol(square):
    def __init__(self, side, height):
        super().__init__(side)
        self.height = height

    def area_and_perimeter(self):
        self.area = self.height * self.side
        self.perimeter = (self.side * 2) + (self.height * 2)
    
    def print_data(self):
        print("il rettangolo di lato:", self.side)
        print("e di altezza:", self.height)
        print("ha area di:", self.area, "metri quadrati")
        print("e perimetro di:", self.perimeter, "metri")

print("lunghezza lato in metri: ")
l_side = float(input())
if l_side <= 0:
    while l_side <= 0:
        print("il lato del rettangolo non può essere inferiore o ugualea 0")
        print("lunghezza lato in metri: ")
        l_side = float(input())
print()

print("lunghezza altezza in metri: ")
l_height = float(input())
if l_height <= 0:
    while l_height <= 0:
        print("l'altezza del rettangolo non può essere inferiore o ugualea 0")
        print("lunghezza lato in metri: ")
        l_height = float(input())
print()

r = rectangol(l_side, l_height)
r.area_and_perimeter()
r.print_data()
