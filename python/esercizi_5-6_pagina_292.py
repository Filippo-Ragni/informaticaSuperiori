class product:

    def __init__(self, name, quantity):
        self.name = str(name)
        self.quantity = int(quantity)
        self.price = None
    
    def give_price(self, price):
        self.price = float(price)

print("nome prodotto: ")
n = str(input())
print()

print("articoli disponibili: ")
q = int(input())
print()

print("prezzo per articolo in euro: ")
p = float(input())
if p < 0:
    while p < 0:
        print("il prezzo del prodotto non può essere inferiore a 0")
        print("prezzo in euro: ")
        p = float(input())
print()

commodity = product(n, q)

commodity.give_price(p)

print("ci sono", commodity.quantity, "di", commodity.name, "rimasti")
print("ognuno di essi costa:", commodity.price, "euro")

print("quanti", commodity.name, "vuoi comprare?")
answer = int(input())
if answer < 1 or answer > commodity.quantity:
    while answer < 1 or answer > commodity.quantity:
        print("non puoi comprarne meno di 0 nè più di", commodity.quantity)
        print("quanti", commodity.name, "vuoi comprare?")
        answer = int(input())
print()

print("importo totale:", answer*commodity.price, "euro")
print()

print("gli attributi della classe product sono:")
print("name, quantity, price")
print("l'unico metodo della classe product è:")
print("give_price")
