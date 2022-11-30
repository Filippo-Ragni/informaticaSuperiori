print("inserisci una parola o una frase(con caratteri in minuscolo): ")
p = list(input())
a = []
for lettera in p:
    if lettera == "b" or lettera == "c" or lettera == "d" or lettera == "f" or lettera == "g" or lettera == "h" or lettera == "j" or lettera == "k" or lettera == "l" or lettera == "m" or lettera == "n" or lettera == "p" or lettera == "q" or lettera == "r" or lettera == "s" or lettera == "t" or lettera == "v" or lettera == "w" or lettera == "x" or lettera == "y" or lettera == "z":
        a.append(lettera)
        a.append("o")
        a.append(lettera)
    else:
        a.append(lettera)
print(a)
a = []
while True:
    print("se vuoi inserire un'altra frase o parola premi -spazio- altrimenti digita una qualsiasi lettera")
    domanda = input()
    if domanda == "":
        print("inserisci una parola o una frase(con caratteri in minuscolo): ")
        p = list(input())
        a = []
        for lettera in p:
            if lettera == "b" or lettera == "c" or lettera == "d" or lettera == "f" or lettera == "g" or lettera == "h" or lettera == "j" or lettera == "k" or lettera == "l" or lettera == "m" or lettera == "n" or lettera == "p" or lettera == "q" or lettera == "r" or lettera == "s" or lettera == "t" or lettera == "v" or lettera == "w" or lettera == "x" or lettera == "y" or lettera == "z":
                a.append(lettera)
                a.append("o")
                a.append(lettera)
            else:
                a.append(lettera)
        print(a)
        a = []
    else:
        break
