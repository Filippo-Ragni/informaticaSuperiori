print("quante città vuoi inserire?")
n = int(input())

nomi = []
c=0

for nome in range(0,n):
    c += 1
    print("come si chiama la ", c, "° città?")
    nome = input()
    nomi.append(nome)

max = []
min = []
v = 0

for valori in range(0,n):
    print("qual'è stata la temperatura massima raagiunta a ", nomi[v], " in °C?")
    mas = float(input())
    max.append(mas)
    print("qual'è stata la temperatura minima raagiunta a ", nomi[v], " in °C?")
    mim = float(input())
    min.append(mim)
    v+=1

esc = []
v = 0

for ex in range(0,n):
    ex = max[v] - min[v]
    esc.append(ex)
    v += 1

v = 0

for dichiarazione in range(0,n):
    print("a", nomi[v], "l'escursione termica è di", esc[v], "°C")
    v += 1

c = 0
v = 0
cambiati = []

for escursione in range(0,n):
    print("oggi qual è l'escursione termica a", nomi[v], "?")
    ex = float(input())
    if ex > esc[v]:
        esc[v] = ex
        cambiati.append(nomi[v])
        c += 1
    v += 1

if c != 0:
    print("l'escursione termica è aumentata in", c, "città; tali città sono:", cambiati)
else:
    breakpoint

print("le escursioni termiche massime raggiunte nelle città sono:")
for associazione in zip(nomi,esc):
    print(associazione)
