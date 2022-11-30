import statistics

dizionario = {}
occupati_annui = []

print("fino a che anno vuoi considerare gli occupati? ")
print("(secondo il metodo di datazione cristiano) ")
anno = int(input())
print()

anno_considerato = anno - 10
for occupati in range(10):
    print("inserire il numero di occupati nel", anno_considerato, "? ")
    occupati = int(input())
    if occupati < 0:
        while occupati < 0:
            print("il numero di occupati non può essere inferiore a 0")
            print("inserire il numero di occupati nel", anno_considerato, "? ")
            occupati = int(input())
    occupati_annui.append(occupati)
    dizionario[anno_considerato] = (occupati)
    anno_considerato += 1
    print()

media = statistics.mean(occupati_annui)
media_intera = int(media)
print("in media tra il", anno - 10, "e il", anno - 1, "erano occupate", media_intera, "persone ogni anno")
