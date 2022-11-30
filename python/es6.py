import random
casuali = []
print("quanti numeri vuoi inserire nella lista?")
n = int(input())
while len(casuali) < n:
    numero = random.randint(1, 20)
    if numero not in casuali:
        casuali.append(numero)
indici = range(n)
lista_con_indici = []
numeri_primi = [1, 2, 3, 5, 7, 11, 13, 17, 19]
numeri_primi_presenti = []
for elemento in zip(casuali, indici):
    lista_con_indici.append(elemento)
for elemento in casuali:
    if elemento in numeri_primi:
        numeri_primi_presenti.append(elemento)
print(lista_con_indici)
print(numeri_primi_presenti)
