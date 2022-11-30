print("da quante parole è formata la lista? ")
lunghezza = int(input())
lista_parole = []
lista_lunghezze = []
for parola in range(lunghezza):
    print("inserisci una parola: ")
    parola = input()
    lista_parole.append(parola)
    lunghezza_parola = len(parola)
    lista_lunghezze.append(lunghezza_parola)
print(lista_lunghezze)
