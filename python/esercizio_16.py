#viene creato il dictionary e le due liste e si dice all'utente come uscire dal ciclo while
nazioni = []
capitali = []
elenco = {}
print("se vuoi smettere di inserire nazioni e capitali digita la parola: end")
print()

#ciclo while dove vengono fatti inserire le stringhe che fungeranno da chiavi e valori nel dictionary e vengono aggiunti alle rispettive liste
while True:
    print("scrivi il nome di una nazione: ")
    nazione = input()
    if nazione != "end":
        print("scrivi la rispettiva capitale: ")
        capitale = input()
        if capitale == "end":
            break 
        else:
            nazioni.append(nazione)
            capitali.append(capitale)
    else:
        break

#le chiavi e i rispettivi valori vengono aggiunti al dictionary
i = 0
for elemento in nazioni:
    elenco[nazioni[i]] = capitali[i]
    i += 1

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
