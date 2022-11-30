studenti = []
voti = []
for i in range(5):
    studente = input("nome dello studente: ")
    studenti.append(studente)
    print("che voto ha preso", studente, "?")
    voto = int(input())
    if voto < 18 or voto > 30:
        while voto < 18 or voto > 30:
            print("il voto non può essere maggiore di 30 nè minore di 18")
            print("che voto ha preso", studente, "?")
            voto = int(input())
    voti.append(voto)
somma = 0
for voto in voti:
    somma = somma + voto
vm = somma / 5
va = max(voti)
print("il voto medio è di:", vm)
sva = ("")
if voti[1] == va:
    sva = studenti[1]
elif voti[2] == va:
    sva = studenti[2]
elif voti[3] == va:
    sva = studenti[3]
elif voti[4] == va:
    sva = studenti[4]
elif voti[5] == va:
    sva = studenti[5]
print("lo studente che ha avuto il puntaggio più alto è stato:", sva)
