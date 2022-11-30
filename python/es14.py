print("quante coppie di numeri vuoi inserire? ")
cicli = int(input())
print("")
risultati = []
for numero in range(0, cicli):
    print("inserisci il numeor a: ")
    a = float(input())
    print("inserisci il numeor b: ")
    b = float(input())
    print("")
    if a*b > 10:
        risultato = a - b
        risultati.append(risultato)
    else:
        risultato = a + b
        risultati.append(risultato)
print(risultati)
