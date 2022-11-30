nomi = []
caps = []
cap_citta = {}
citta_cap = {}

print("se hai finito di inserire i le citta ed i corrispettivicodici di avviamento postale(cap) digita : end")
print()

while True:
    print("inserisci il nome della citta da memorizzare : ")
    nome = input().lower()
    if nome == "end":
        print()
        break
    elif nome in nomi:
        print("non puoi inserire un nome già presente")
        print("inserisci il nome della citta da memorizzare : ")
    else:
        print("inserisci il codice di avviamento postale di", nome, " : ")
        cap = input().lower()
        if cap == "end":
            print()
            break
        elif cap in caps:
            print("non puoi inserire un codice di avviamento postale già presente")
            print("inserisci il codice di avviamento postale di", nome, " : ")
        else:
            citta_cap[nome] = cap
            cap_citta[cap] = nome
            nomi.append(nome)
            caps.append(cap)
    print()

print("le citta e i cap inseriti nel dizionario sono : ")
for elemento in nomi:
    print(elemento, ":", citta_cap[elemento])
print()

print("se vuoi conoscere le citta tramite i cap digita : cap")
print("se vuoi conoscere i cap tramite le citta digita : citta")
metodo = input().lower()

if metodo != "citta" and metodo != "cap":
    while metodo != "citta" and metodo != "cap":
        print("non puoi inserire un valore diverso dai due precedentemente indicati")
        print("se vuoi conoscere le citta tramite i cap digita : cap")
        print("se vuoi conoscere le cap tramite i citta digita : citta")
        metodo = input().lower()
        print()

if metodo == "citta":
    print("se hai finito di chiedere i cap di cui hai inserito il nomi delle rispettive citta digita : end")
    print()

    while True:
        print("digita il nome della citta di cui vuoi conoscere il cap : ")
        domanda = input().lower()
        if domanda == "end":
            break
        elif domanda in nomi:
            print("il cap di", domanda, "è", citta_cap[domanda])
        else:
            print("questo nome non è stato memorizzato")
            print("digita il nome della citta di cui vuoi conoscere il cap : ")
        print()

elif metodo == "cap":
    print("se hai finito di chiedere i nomi delle citta di cui hai inserito i cap digita : end")
    print()

    while True:
        print("digita il cap di cui vuoi conoscere il nome della citta : ")
        domanda = input().lower()
        if domanda == "end":
            break
        elif domanda in caps:
            print("il nome della citta di", domanda, "è", cap_citta[domanda])
        else:
            print("questo cap non è stato memorizzato")
            print("digita il cap di cui vuoi conoscere il nome della citta : ")
        print()
