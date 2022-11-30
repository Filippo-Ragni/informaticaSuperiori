lista = []
print("inserisci un numero: ")
a = int(input())
print("inserisci un altro numero: ")
b = int(input())
if a > b:
    lista_con_indici = []
    indici = range(a - b + 1)
    indice = 0
    while a >= b:
        lista.append(a)
        a -= 1
    lista.reverse()
    for elemento in zip(lista, indici):
        lista_con_indici.append(elemento)
    print(lista_con_indici)
    for x in lista:
        lista[indice] = x * 2
        indice += 1
    print(lista)
    breakpoint
elif a == b:
    print(a, 0)
    print(b * 2)
    breakpoint
else:
    lista_con_indici = []
    indici = range(b - a + 1)
    indice = 0
    while b >= a:
        lista.append(b)
        b -= 1
    lista.reverse()
    for elemento in zip(lista, indici):
        lista_con_indici.append(elemento)
    print(lista_con_indici)
    for x in lista:
        lista[indice] = x * 2
        indice += 1
    print(lista)
    breakpoint
