partecipanti=int(input("quanti studenti ci sono? "))
valori=[]
for partecipanti in range(0,partecipanti):
    partecipanti-= 1
    print ("quanto ha lanciato? ")
    lancio = int(input())
    valori.append(lancio)
vincitore = max(valori)
print("il laancio vincente è stato di: ", vincitore, "m")
