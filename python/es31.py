print("che numero decimale vuoi inserire?")
decimale = int(input())

binario = []
quoziente = decimale

while quoziente != 0:
    resto = quoziente % 2
    quoziente = quoziente // 2
    binario.append(resto)

print("il numero decimale", decimale, "in cifre binarie diventa:")

for cifra in reversed(binario):
    print(cifra)
