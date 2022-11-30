#viene creato il dictionary e le due liste e si dice all'utente come uscire dal ciclo while
nazioni = []
capitali = []
elenco = {}
print("se vuoi smettere di inserire nazioni e capitali digita la parola: end")
print()

#ciclo while dove vengono fatti inserire le stringhe che fungeranno da chiavi e valori nel dictionary e vengono aggiunti alle rispettive liste
while True:
    print("scrivi il nome di una capitale: ")
    capitale = input()
    if capitale != "end":
        print("scrivi la rispettiva nazione: ")
        nazione = input()
        if nazione == "end":
            break 
        else:
            nazioni.append(nazione)
            capitali.append(capitale)
    else:
        break

#le chiavi e i rispettivi valori vengono aggiunti al dictionary
i = 0
for elemento in nazioni:
    elenco[capitali[i]] = nazioni[i]
    i += 1

#si dice all'utente come uscire dal ciclo while
print()
print("se vuoi smettere di chiedere le nazioni inserendo le capitali digita: end")
print()

#si chiede all'utente il valore di quale chiave si vuole conoscere con la verifica della presenza della chiave nel dictionary
while True:
    print("di qule capitale vuoi conoscere la nazione? ")
    domanda = input()
    if domanda == "end":
        break
    elif domanda in elenco:
        print("la nazione con capitale", domanda, "è", elenco[domanda])
        break
    else:
        print("la capitale selezionata non è nell'elenco")
