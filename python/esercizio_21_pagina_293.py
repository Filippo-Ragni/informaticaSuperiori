class motorcycle:

    def __init__(self, type, brand):
        self.type = type
        self.brand = brand
        self.price = None

    def give_price(self, price):
        self.price = float(price)

class minibike(motorcycle):
    def __init__(self, type, brand, displacement, max_speed):
        super().__init__(type, brand)
        self.displacement = float(displacement)
        self.max_speed = float(max_speed)

    def print_data(self):
        print("il ciclomotore è  un:", self.type)
        print("è prodotto dall'azienda:", self.brand)
        print("costa:", self.price, "euro")
        print("ha una cilindrata di:", self.displacement, "cc")
        print("può raggiungere una velocità massima di:", self.max_speed, "km/h")

print("tipo ciclo motore: ")
t = str(input())
print()

print("azienda produttrice: ")
b = str(input())
print()

print("prezzo in euro: ")
p = float(input())
if p <= 0:
    while p <= 0:
        print("il prezzo del ciclo motore non può essere inferiore o uguale a 0")
        print("prezzo in euro: ")
        p = float(input())
print()

print("cilindrata in cc(centimetri cubici): ")
m_d = float(input())
if m_d <= 0 or m_d > 50:
    while m_d <= 0 or m_d > 50:
        print("la cilindrata del ciclomotore non può essere inferiore o uguale a 0 o superiore a 50 cc")
        print("cilindrata in cc(centimetri cubici): ")
        m_d = float(input())
print()

print("velocità massima in km/h(kilometri all'ora): ")
m_s = float(input())
if m_s <= 0 or m_s > 45:
    while m_s <= 0 or m_s > 45:
        print("la velocità massima del ciclo motore non può essere inferiore o uguale a 0 o maggire di 45 km/h")
        print("velocità massima in km/h(kilometri all'ora): ")
        m_s = float(input())
print()

cm = minibike(t, b, m_d, m_s)
cm.give_price(p)
cm.print_data()
