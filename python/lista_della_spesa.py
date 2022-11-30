print ("inserisci i nomi di tutte le cose che vuoi comprare")
print ("per fermare il programma scrivere: ok ")
print ("con caratteri minuscoli")

elementi = 1
prezzo = 0
n = input()
lista = [n]
p = len(n)
prezzo = prezzo + p

while n != ("ok") :
    elementi += 1
    n = input ()
    lista.append(n)
    p = len(n)
    prezzo = prezzo + p

print ()

elementi -= 1
lista.remove ("ok")
print ("la tua lista della spesa è composta da:")
print (elementi, "elementi")
print ("che sono:")
print (lista)

print ()

prezzo = prezzo - p
print ("la tua spesa costa:")
print (prezzo, "euro")
