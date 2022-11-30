import math
tentativi = 0
while True:
    print("digita il numero della figura di cui vuoi calcolare l'area?")
    print("(se digiti per tre volte un numero diverso da quelli indicati il programma finirà)")
    print("1. di un quadrato")
    print("2. di un rettangolo")
    print("3. di un triangolo")
    print("4. di un cerchio")
    figura = int(input())
    if figura == 1:
        print("quanto è lungo un lato del quadrato in metri? ")
        lato = float(input())
        area = lato*lato
        print("l'area del quadrato è di", area, "metri quadrati")
        break
    if figura == 2:
        print("quanto è lungo un lato del rettangolo in metri? ")
        lato = float(input())
        print("quanto è lungo un lato del rettangolo perpendicolare al precedente in metri? ")
        latop = float(input())
        area = lato*latop
        print("l'area del rettangolo è di", area, "metri quadrati")
        break
    if figura == 3:
        print("quanto è lungo un lato del triangolo in metri? ")
        lato = float(input())
        print("quanto è lunga l'altezza ad esso associata in metri? ")
        altezza = float(input())
        area = (lato*altezza)/2
        print("l'area del triangolo è di", area, "metri quadrati")
        break
    if figura == 4:
        print("quanto è lungo il raggio del cerchio in metri? ")
        raggio = float(input())
        area = (raggio*raggio)*math.pi
        print("l'area del quadrato è di", area, "metri quadrati")
        break
    else:
        tentativi += 1
        if tentativi == 3:
            break
