nome1=input("il nome del primo candidato è: ")
nome1 = nome1.upper()
nome2=input("il nome del secondo candidato è: ")
nome2 = nome2.upper()
print(nome1, " ha preso: ")
punteggio1=int(input())
print(nome2, " ha preso: ")
punteggio2=int(input())
if nome1 > nome2:
     print(nome2, nome1)
else:
     print(nome1, nome2)
if punteggio1 > punteggio2:
    print(nome1, nome2)
else:
    print(nome2, nome1)