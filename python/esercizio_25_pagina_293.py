import math

class triangle:

    def __init__(self, t_base, t_fstside, t_sndside):
        self.base = t_base
        self.fstside = t_fstside
        self.sndside = t_sndside

    def print_data_t(self):
        print("la base del triangolo misura:", self.base, "metri")
        print("uno dei lati obliqui triangolo misura:", self.fstside, "metri")
        print("l'altro lato obliquo triangolo misura:", self.sndside, "metri")
        print("l'area del triangolo misura:", self.area, "metri quadrati")
        print("il perimetro del triangolo misura", self.perimeter, "metri")
        print()

    def area_and_perimeter(self):
        self.perimeter = self.base + self.fstside + self.sndside
        self.p = self.perimeter / 2
        self.a2 = self.p * (self.p - self.base) * (self.p - self.fstside) * (self.p - self.sndside)
        self.area = math.sqrt(self.a2)

class isosceles_triangle(triangle):
    def __init__(self):
        super().__init__(t_base, t_fstside, t_sndside)
        self.oblside = self.fstside

    def print_data_ti(self):
        print("la base del triangolo isoscele misura:", self.base, "metri")
        print("i lati obliqui del triangolo isoscele misurano:", self.oblside, "metri")
        print("l'area del triangolo isoscele misura:", self.area, "metri quadrati")
        print("il perimetro del triangolo isoscele misura", self.perimeter, "metri")
        print()

    def area_and_perimeter(self):
        self.perimeter = self.base + (self.oblside * 2)
        self.p = self.perimeter / 2
        self.a2 = self.p * (self.p - self.base) * ((self.p - self.oblside)**2)
        self.area = math.sqrt(self.a2)

class equilateral_triangle(isosceles_triangle):
    def __init__(self):
        super().__init__()
        self.side = self.base

    def print_data_te(self):
        print("i lati del triangolo equilatero misurano:", self.side, "metri")
        print("l'area del triangolo equilatero misura:", self.area, "metri quadrati")
        print("il perimetro del triangolo equilatero misura", self.perimeter, "metri")
        print()

    def area_and_perimeter(self):
        self.perimeter = self.side * 3
        self.p = self.perimeter / 2
        self.a2 = self.p * ((self.p - self.side)**3)
        self.area = math.sqrt(self.a2)

print("base(in metri): ")
t_base = float(input())
if t_base <= 0:
    while t_base <= 0:
        print("la base del triangolo non può essere pari o inferiore a 0 metri")
        print("base(in metri): ")
        t_base = float(input())
print()

print("primo lato obliquo(in metri): ")
t_fstside = float(input())
if t_fstside <= 0:
    while t_fstside <= 0:
        print("il primo lato obliquo del triangolo non può essere pari o inferiore a 0 metri")
        print("primo lato obliquo(in metri): ")
        t_fstside = float(input())
print()

print("secondo lato obliquo(in metri): ")
t_sndside = float(input())
if t_sndside <= 0:
    while t_sndside <= 0:
        print("il secondo lato obliquo del triangolo non può essere pari o inferiore a 0 metri")
        print("secondo lato obliquo(in metri): ")
        t_sndside = float(input())
print()

if t_base >= (t_fstside + t_sndside):
    while t_base >= (t_fstside + t_sndside):
        print("la somma di due lati del triangolo non può essere inferiore o uguale alla base")
        print("base(in metri): ")
        t_base = float(input())
elif t_sndside >= (t_base + t_fstside):
    while t_sndside >= (t_base + t_fstside):
        print("la somma di un lato e la base del triangolo non può essere inferiore o uguale all'altro lato'")
        print("secondo lato obliquo(in metri): ")
        t_sndside = float(input())
elif t_fstside >= (t_base + t_sndside):
    while t_fstside >= (t_base + t_sndside):
        print("la somma di un lato e la base del triangolo non può essere inferiore o uguale all'altro lato'")
        print("primo lato obliquo(in metri): ")
        t_fstside = float(input())
print()

t = triangle(t_base, t_fstside, t_sndside)
t.area_and_perimeter()
t.print_data_t()

print("base(in metri): ")
t_base = float(input())
if t_base <= 0:
    while t_base <= 0:
        print("la base del triangolo isoscele non può essere pari o inferiore a 0 metri")
        print("base(in metri): ")
        t_base = float(input())
print()

print("lati obliqui(in metri): ")
t_fstside = float(input())
if t_fstside <= 0:
    while t_fstside <= 0:
        print("i lati obliqui del triangolo isoscele non possono essere pari o inferiori a 0 metri")
        print("lati obliqui(in metri): ")
        t_fstside = float(input())
    
if t_base >= (t_fstside * 2):
    while t_base >= (t_fstside * 2):
        print("la base del triangolo isoscele non può essere maggiore o uguale alla somma dei lati obliqui")
        print("base(in metri): ")
        t_base = float(input())
print()

t_i = isosceles_triangle()
t_i.area_and_perimeter()
t_i.print_data_ti()

print("lati(in metri): ")
t_base = float(input())
if t_base <= 0:
    while t_base <= 0:
        print("i lati del triangolo equilatero non possono essere pari o inferiori a 0 metri")
        print("lati(in metri): ")
        t_base = float(input())
print()

t_e = equilateral_triangle()
t_e.area_and_perimeter()
t_e.print_data_te()
