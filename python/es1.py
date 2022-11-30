print("scrivi una parola: ")
parola = list(input())
palindromo = []
for lettera in parola:
    palindromo.append(lettera)
palindromo.reverse()
print
if parola == palindromo:
    print("questa parola è un palindromo")
else:
    print("questa parola non è un palindromo")
