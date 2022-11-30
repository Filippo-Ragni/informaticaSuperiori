nvoti = 0
somma = 0

print ("quando inserisci il voto tieni a mente che:")
print ("i mezzi voti sono: x.5 ;")
print ("mentre i quarti di voto sono: x.25/x.75 .")
print ("quando hai finito di inserire i voti inserisci: 00")

print ()

voti = []
voto = float(input("inserisci un voto: "))
voti.append (voto)
nvoti += 1
somma += voto

print ()

if voto != 00:
    for voto in voti :
        voto = float(input("inserisci un altro voto: "))
        if voto == (00):
            break
        else:
            voti.append (voto)
            nvoti += 1
            somma += voto
            print ()

    media = somma/nvoti
    
    print ()
    print ("la media dei tuoi voti è", media)
