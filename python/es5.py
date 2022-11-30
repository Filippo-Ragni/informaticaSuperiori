import random
casuali = []
print("quanti numeri vuoi inserire nella lista?")
n = int(input())
while len(casuali) < n:
    numero = random.randint(1, 30)
    if numero not in casuali:
        casuali.append(numero)
indici = range(n)
lista_con_indici = []
non_multipli = []
indice = 0
for elemento in zip(casuali, indici):
    lista_con_indici.append(elemento)
    resto = int(casuali[indice] % 3)
    if resto != 0:
        non_multipli.append(elemento)
    indice += 1
print(lista_con_indici)
nm = len(non_multipli)
print(nm)
