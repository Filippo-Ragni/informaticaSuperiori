print("i voti possibili sono: sufficiente, buono, distinto ed ottimo")
print("cosa inserire: sufficiente, buono, distinto ed ottimo")
peso_voti = []
studenti = []
for i in range(10):
    studente = input("nome dello studente: ")
    studenti.append(studente)
    print("che voto ha preso", studente, "?")
    voto = input().lower()
    if voto == 'sufficiente':
        voto_p = 1
    elif voto == 'buono':
        voto_p = 2
    elif voto == 'distinto':
        voto_p = 3
    else:
        voto_p = 4
    peso_voti.append(voto_p)
somma = sum(peso_voti)
media = somma / 10
print("la media dei voti degli studenti(secondo il peso dei voti) è", media)
