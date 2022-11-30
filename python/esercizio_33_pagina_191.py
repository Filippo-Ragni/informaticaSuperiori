print("quante persone sono arrivate?")
n_persone = int(input())
persone = []
n = 1

for i in range(n_persone):
    print("qual'è il nome della", n, "persona?")
    persona = input()
    n += 1
    persone.append(persona)

print()
for elemento in persone:
    print(elemento)
