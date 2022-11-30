#si crea un dizionario di 30 coppie di chiavi del tipo [ nome_studente , voto_prova_di_italiano ]
#printa i voti in ordine crescente
#visualizza tutti i voti diversi in ordine(se uno è ripetuto printalo una sola volta)

voti = []
valutazioni = {}

print("quanti voti devi inserire?")
n = int(input())
print()

for matricola in range(n):
    print("come si chiama lo studente ? ")
    nome = input()
    print("quanto ha preso", nome, "?")
    voto = float(input())
    if voto < 0 or voto > 10:
        while voto < 0 or voto > 10:
            print("il voto non può essere maggiore di 10 o inferiore a 0")
            print("quanto ha preso", nome, "?")
            voto = float(input())
    valutazioni[nome] = voto
    voti.append(voto)
    print()

crescendo = []
studenti_associati = []

while len(voti) != 0:
    valore_da_printare = min(voti)
    crescendo.append(valore_da_printare)
    for valore in voti:
        if valore == valore_da_printare:
            voti.remove(valore_da_printare)

persone_da_printare = []

for numero in crescendo:
    print("voto :", numero)
    for persona in valutazioni:
        if valutazioni[persona] == numero:
            persone_da_printare.append(persona)
    print("coloro che hanno preso tale voto sono:", persone_da_printare)
    print()
    persone_da_printare = []

#prof sò che la consegna diceva di inserire i voti di 30 studenti,
#ma mi sembrava un po' eccessivo quindi ho lasciato scegliere all'utente il numero di voti da inserire

#inoltre hodeciso di unire il 2° e il 3° punto della consegna per essere più comodo 
#ed ho anche fatto printare i nomi di coloro che hanno preso i voti per non lasciare inutilizzato il dizionario altrimenti inutile
