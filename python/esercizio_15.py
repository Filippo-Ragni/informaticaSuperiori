#viene creato il dictionary e si dice all'utente come uscire dal ciclo while
elenco = {}
print("se vuoi smettere di inserire nazioni e capitali digita la parola: end")
print()

#ciclo while dove vengono fatti inserire le chiavi ed i rispettivi valori e vengono aggiunti al dictionary
while True:
    print("scrivi il nome di una nazione: ")
    nazione = input()
    if nazione != "end":
        print("scrivi la rispettiva capitale: ")
        capitale = input()
        if capitale == "end":
            break 
        else:
            elenco[nazione] = capitale
    else:
        break

#si dice all'utente come uscire dal ciclo while
print()
print("se vuoi smettere di chiedere le capitali inserendo le nazioni digita: end")
print()

#si chiede all'utente il valore di quale chiave si vuole conoscere con la verifica della presenza della chiave nel dictionary
while True:
    print("di qule nazione vuoi conoscere la capitale? ")
    domanda = input()
    if domanda == "end":
        break
    elif domanda in elenco:
        print("la capitale del", domanda, "è", elenco[domanda])
        break
    else:
        print("la nazione selezionata non è nell'elenco")
