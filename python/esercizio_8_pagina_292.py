class square:

    def __init__(self, side):
        self.side = side

    def area(self):
        self.area = self.side ** 2

    def perimeter(self):
        self.perimeter = self.side * 4

print("lunghezza lato in metri: ")
l_side = float(input())
if l_side <= 0:
    while l_side <= 0:
        print("il lato del quadrato non può essere inferiore o ugualea 0")
        print("lunghezza lato in metri: ")
        l_side = float(input())
print()

square_e = square(l_side)
square_e.area()
square_e.perimeter()

print("il quadrato di lato:", square_e.side, "metri")
print("ha un area di:", square_e.area, "metri quadrati")
print("e un perimetro di:", square_e.perimeter, "metri")
