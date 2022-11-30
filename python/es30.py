print("da quante cifre è composto il numero binario?")
cifre = int(input())

binario = []

n = 1

for cifra in range(0,cifre):
    print("qual è il valore della", n, "° cifra da destra?")
    cifra = int(input())
    binario.append(cifra)

c = 0
m = 1

decimale = 0

for valore in range(0,cifre):
    valore = binario[c] * m
    decimale += valore
    c += 1
    m = m * 2

b = []
i = -1

for numero in range(0,cifre):
    numero = binario[i]
    b.append(numero)
    i -= 1

print("il numero binario", b, "equivale a", decimale, "in cifre decimali")
