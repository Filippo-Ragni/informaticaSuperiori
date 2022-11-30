nomi_partecipanti = []
biglietti_partecipanti = []
partecipanti = {}
inviate = []
da_inviare = []
print("numero massimo di partecipanti è: ")
n_partecipanti = int(input())
print()

def dati_partecipante():
    print()
    print("inserire il codice di 6 cifre associato al biglietto ")
    print("del partecipante che ha appena effettuato la prenotazione: ")
    codice_partecipante = input()
    if len(codice_partecipante) != 6 or codice_partecipante in biglietti_partecipanti:
        while len(codice_partecipante) != 6 or codice_partecipante in biglietti_partecipanti:
            print("il codice del partecipante deve essere di 6 cifre e non puoi inserire un codice già utilizzato;")
            print("inserire il codice di 6 cifre associato al biglietto ")
            print("del partecipante che ha appena effettuato la prenotazione: ")
            codice_partecipante = input()
    print()
    print("inserire il nome del partecipante con codice:", codice_partecipante)
    nome_partecipante = input()
    if nome_partecipante in nomi_partecipanti:
        while nome_partecipante in nomi_partecipanti:
            print("non puoi inserire un nome già utilizzato;")
            print("inserire il nome del partecipante con codice:", codice_partecipante)
            nome_partecipante = input()
    print()
    biglietti_partecipanti.append(codice_partecipante)
    nomi_partecipanti.append(nome_partecipante)
    partecipanti[codice_partecipante] = nome_partecipante
    print(biglietti_partecipanti)
    print(nomi_partecipanti)
    print(partecipanti)
    return()

def check_lettere(codice):
    print()
    print("(rispondere solo si o no alla seguente domanda)")
    print("al partecipante con codice biglietto:", codice)
    print("è stata consegnata la lettera di conferma?")
    check = input().lower()
    if check != "si" and check != "no":
        while check != "si" and check != "no":
            print("la risposta ricevuta non rispetta la richiesta espressa")
            print("(rispondere solo si o no alla seguente domanda)")
            print("al partecipante con codice biglietto:", codice)
            print("è stata consegnata la lettera di conferma?")
            check = input().lower()
    if check == "si":
        inviate.append(nome_partecipante)
    else:
        da_inviare.append(nome_partecipante)
    print(inviate)
    print(da_inviare)
    return()

for persona in range(n_partecipanti):
    dati_partecipante()
    codice_partecipante = biglietti_partecipanti[-1]
    nome_partecipante = nomi_partecipanti[-1]
    check_lettere(codice_partecipante)

print()
print("i partecipanti e i codici dei rispettivi biglietti sono:")
for entità in partecipanti:
    print(entità, partecipanti[entità])
print("in partecipanti a cui non è ancora stata inviata la lettera di conferma sono: ")
for mancante in da_inviare:
    print(mancante)
