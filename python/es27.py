veicoli=[]
n=0
while True:
     n=int(input("numero veicoli transitati: "))
     veicoli.append(n)
     if n == 0:
          break
somma=sum(veicoli)
print(somma)