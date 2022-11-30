fatturato_tot = 0
fatturati = []

print("fatturato Nord in euro: ")
fatturato_n = float(input())
fatturati.append(fatturato_n)
print()

print("fatturato Centro in euro: ")
fatturato_c = float(input())
fatturati.append(fatturato_c)
print()

print("fatturato Sud in euro: ")
fatturato_s = float(input())
fatturati.append(fatturato_s)
print()

print("fatturato isole in euro: ")
fatturato_i = float(input())
fatturati.append(fatturato_i)
print()

for i in range(0,4):
    fatturato_tot = fatturato_tot + fatturati[i]
print("il fatturato totale è di:", fatturato_tot, "euro")
print()

percentuali = []
for elemento in fatturati:
    percentuale = elemento/fatturato_tot*100
    percentuali.append(percentuale)

print("il Nord ha prodotto il", percentuali[0], "% del fatturato")
print("il Centro ha prodotto il", percentuali[1], "% del fatturato")
print("il Sud ha prodotto il", percentuali[2], "% del fatturato")
print("le isole hanno prodotto il", percentuali[3], "% del fatturato")
