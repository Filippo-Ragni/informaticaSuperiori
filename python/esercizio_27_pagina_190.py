nomi = []
numeri = []
elenco = {}

print("se hai inserito tutti i nomi e i numeri ad essi associati nell'elenco digita : end")
print()

while True:
    print("inserire il nome della persona di cui si vuole inserire il numero : ")
    nome = input().lower()
    if nome == "end":
        print()
        break
    elif nome in nomi:
        print("non puoi inserire un nome già presente")
        print()
    else:
        print("inserire il numero di", nome, ": ")
        numero = input().lower()
        if numero == "end":
            print()
            break
        elif numero in numeri:
            print("non puoi inserire un numero già presente")
            print()
        else:
            elenco[nome] = numero
            nomi.append(nome)
            numeri.append(numero)
    print()

print("nell'elenco sono presenti i numeri di : ")
for elemento in nomi:
    print(elemento)
print()

print("se hai finito di chiedere i numeri delle persone di cui hai inserito il nome digita : end")
print()

while True:
    print("digita il nome della persona di cui vuoi conoscere il numero : ")
    domanda = input().lower()
    if domanda == "end":
        break
    elif domanda in nomi:
        print("il numero di", domanda, "è", elenco[domanda])
    else:
        print("questo nome non è presente nell'elenco")
        print("digita il nome della persona di cui vuoi conoscere il numero : ")
    print()
