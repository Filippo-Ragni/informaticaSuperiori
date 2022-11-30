lista = []

print("quando hai smesso di inserire le parole digita: * ")
print()

parola = ""

while parola != "*":
    print("inserisci una parola: ")
    parola = input().lower()
    print()
    parola = parola.strip()
    lista.append(parola)

lista.pop()

print("la lista contiene", len(lista), "parole")
print()

lista.sort()
print("le parole in ordine alfabetico sono:")
for elemento_s in lista:
    print(elemento_s)
    print()

lista.reverse()
print("le parole in ordine contrario all'alfabetico sono:")
for elemento_r in lista:
    print(elemento_r)
