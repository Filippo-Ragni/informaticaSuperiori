lista = []
print("quanti multipli di 10 vuoi inserire nella lista? ")
n = int(input())
fattore = 1
for multiplo in range(n):
    multiplo = 10 * fattore
    fattore += 1
    lista.append(multiplo)
indici = range(n)
lista_con_indici = []
for elemento in zip(lista, indici):
    lista_con_indici.append(elemento)
print(lista_con_indici)
indice = 0
for elemento in lista:
    if elemento > 30:
        lista[indice] = elemento / 2
    indice += 1
print(lista)
