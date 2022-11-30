class motorcycle:

    def __init__(self, type, brand):
        self.type = str(type)
        self.brand = str(brand)
        self.price = None
    
    def give_price(self, price):
        self.price = float(price)

print("tipo motociclo: ")
t = str(input())
print()

print("azienda produttrice: ")
b = str(input())
print()

print("prezzo in euro: ")
p = float(input())
if p <= 0:
    while p <= 0:
        print("il prezzo del motociclo non può essere inferiore o uguale a 0")
        print("prezzo in euro: ")
        p = float(input())
print()

m_cycle = motorcycle(t, b)

m_cycle.give_price(p)

print("il", m_cycle.type, "è prodotto dalla", m_cycle.brand,"e costa", m_cycle.price, "euro")
print()

print("gli attributi della classe motorcycle sono:")
print("type, brand, price")
print("l'unico metodo della classe motorcycle è:")
print("give_price")
