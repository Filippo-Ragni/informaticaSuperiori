candidato1=input("nome primo candidato: ")
candidato2=input("nome secondo candidato: ")
print("voti", candidato1, " = ")
voti1=int(input())
print("voti", candidato2, " = ")
voti2=int(input())
tot=voti1+voti2
perc1=voti1/tot*100
perc2=voti2/tot*100
if voti1>voti2:
    print("ha vinto ", candidato1)
elif voti1==voti2:
    print("è un pareggio")
else:
    print("ha vinto ", candidato2)
print("percentuale di voti ottenuti da ", candidato1, " = ", perc1)
print("percentuale di voti ottenuti da ", candidato2, " = ", perc2)