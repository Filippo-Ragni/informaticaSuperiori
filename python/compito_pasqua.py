from random import randint
nome = input ("come ti chiami?")
print ("ciao", nome)
n = int(input("inserisci il numero della tabellina nella quale ti vuoi esercitare: "))

tentativi = 0
voto = 10
giuste= 0

while tentativi < 10 and giuste < 3:
    tentativi += 1
    voto -= 1
    a = randint(1,99)
    b = randint(1,99)
    c = randint(1,99)
    print ("quanto fa:", n, "moltiplicato per", a)
    r1 = int(input())
    if r1 == a*n:
        giuste += 1
    else:
        print ("")
    print ("quanto fa:", n, "moltiplicato per", b)
    r2 = int(input())
    if r2 == b*n:
        giuste += 1
    else:
        print ("")
    print ("quanto fa:", n, "moltiplicato per", c)
    r3 = int(input())
    if r3 == c*n:
        giuste += 1
    else:
        print ("")
    if r1 == a*n and r2 == b*n and r3 == c*n :
        voto += 1
    else:
        print ("")

print ("")

if voto == 10:
    print ("bravo", nome, "le hai azzeccate tutte al primo colpo")
    print ("hai preso", voto)
elif voto == 9:
    print ("risultato eccellente, mi raccomando continua così", nome)
    print ("hai preso", voto)
elif voto == 8:
    print ("hai ottenuto un buon risultato, continua così", nome)
    print ("hai preso", voto)
elif voto == 7:
    print ("risultato discreto")
    print ("hai preso", voto)
elif voto == 6:
    print ("risultato sufficiente, ma si può ancora migliorare")
    print ("hai preso", voto)
elif voto == 5:
    print ("risultato insufficiente ma non difficilmente recuperabile")
    print ("hai preso", voto)
elif voto == 4:
    print ("se ti metti subito a studiare potresti recuperarlo, anche se non ne sono sicuro")
    print ("hai preso", voto)
elif voto == 3:
    print ("è meglio che niente, ma è comunque un risultato pessimo")
    print ("hai preso", voto)
elif voto == 2:
    print ("è meglio che niente, ma è comunque un risultato pessimo")
    print ("hai preso", voto)
elif voto == 1:
    print ("è meglio che niente, ma è comunque un risultato pessimo")
    print ("hai preso", voto)
else:
    print ("asino!")
    print ("hai preso", voto)
    print ("fila a studiare!")

print ("nel caso ti debba esercitare con le tabelline puoi utilizzare questo programma")
print ("arrivederci", nome)
quit ("")
