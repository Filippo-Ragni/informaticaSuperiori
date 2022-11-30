limiti = [15000.0, 28000.0, 55000.0, 75000.0, 1000000000000.0]
aliquota = [23, 27, 38, 41, 43]
dizionario ={}
for elemento in range(0,5):
    dizionario[limiti[elemento]] = (aliquota[elemento])

imposte_max = []
imposta_max_limite_1 = limiti[0]*aliquota[0]/100
imposte_max.append(imposta_max_limite_1)
imposta_max_limite_2 = imposta_max_limite_1 + (limiti[1] - limiti[0])*aliquota[1]/100
imposte_max.append(imposta_max_limite_2)
imposta_max_limite_3 = imposta_max_limite_2 + (limiti[2] - limiti[1])*aliquota[2]/100
imposte_max.append(imposta_max_limite_3)
imposta_max_limite_4 = imposta_max_limite_3 + (limiti[3] - limiti[2])*aliquota[3]/100
imposte_max.append(imposta_max_limite_4)

print("inserire il reddito in euro: ")
print("il limite minimo consentito è di: 0 euro")
print("il limite massimo consentito è di: 1000000000000.0 euro")
reddito = float(input())
print()

if reddito < 0:
    while reddito < 0:
        print("il reddito non può essere inferiore a 0 euro")
        print("inserire il reddito in euro: ")
        print("il limite minimo consentito è di: 0 euro")
        print("il limite massimo consentito è di: 1000000000000.0 euro")
        reddito = float(input())
    print()

if reddito > 1000000000000.0:
    while reddito > 1000000000000.0:
        print("il reddito non può essere superiore a 1000000000000.0 euro")
        print("inserire il reddito in euro: ")
        print("il limite massimo consentito è di: 1000000000000.0 euro")
        reddito = float(input())
    print()

if reddito <= limiti[0]:
    imposta = reddito*aliquota[0]/100
elif reddito <= limiti[1]:
    imposta = imposte_max[0] + (reddito - limiti[0])*aliquota[1]/100
elif reddito <= limiti[2]:
    imposta = imposte_max[1] + (reddito - limiti[1])*aliquota[2]/100
elif reddito <= limiti[3]:
    imposta = imposte_max[2] + (reddito - limiti[2])*aliquota[3]/100
else:
    imposta = imposte_max[3] + (reddito - limiti[3])*aliquota[4]/100

print("la tua imposta è di:", imposta, "euro")
print("la tassazione media è del:", imposta/reddito*100, "%")
