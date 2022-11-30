print("se mi dai i valori dei parametri a e b")
print("e ti dirò il risultato dell'equazione: ax + b = 0")
print("valore di a: ")
a = float(input())
print("valore di b: ")
b = float(input())
print("")
if a == 0 and b != 0:
    print("l'equazione è impossibile")
elif a == 0 and b == 0:
    print("l'equazione è indeterminata")
elif a != 0 and b == 0:
    print("x = 0")
else:
    print("x =", -(b/a))
