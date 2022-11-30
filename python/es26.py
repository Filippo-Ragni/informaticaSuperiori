stipendi=[]
stipendio=0
while stipendio != -1:
    stipendio = float(input("stipendio = "))
    stipendi.append(stipendio)
somma=sum(stipendi)
ns=len(stipendi)
media=somma/ns
print(media)