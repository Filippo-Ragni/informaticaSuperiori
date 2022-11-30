#si chiede all'utente quante coppie di chiavi vuole inserire nel dictionary
print("inserire il numero di conti che sono stati aperti: ")
numero_conti = int(input())
print()

#si crea il dictionary e si inseriscono in esso le chiavi con i rispettivi valori
conti = {}
numeri_conto = []
for conto in range(numero_conti):
    print("inserire il numero del conto: ")
    numero_conto = int(input())
    print("inserire il saldo del conto n°", numero_conto, "in euro")
    saldo_conto = float(input())
    print()
    conti[numero_conto] = saldo_conto
    numeri_conto.append(numero_conto)

#si dicono all'utente le chiavi e si chiede all'utente di quale di esse vuole conoscere il valore
print("i numeri dei vari conti sono: ")
for numero in numeri_conto:
    print(numero)
print()
print("inserire il numero del conto del quale si vuole conoscere il saldo: ")
richiesta = int(input())
if richiesta in numeri_conto:
    print("il saldo del conto n°", richiesta, "è", conti[richiesta], "euro")
else:
    print("siamo spiacenti ma il numero inserito non appartiene a nessun conto registrato")
