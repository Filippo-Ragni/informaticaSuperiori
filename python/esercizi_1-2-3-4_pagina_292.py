class athlete:

    def __init__(self, height, weight, age, name):
        self.height = height
        self.weight = weight
        self.age = age
        self.name = name
        self.medical_examination = bool()
        self.team = str("")

    def team_a(self, athlete_team):
        self.team = athlete_team
    
    def do_medical_examination(self):
        self.medical_examination = True
    
    def see_datas(self):
        print("dati atleta: ")
        print("l'atleta si chiama", self.name)
        print("l'atleta", self.name, "misura", self.height, "cm di altezza")
        print("l'atleta", self.name, "pesa", self.weight, "kg")
        print("l'atleta", self.name, "ha", self.age, "anni")
        print("l'atleta", self.name, "fa parte della squadra", self.team)
        if self.medical_examination == True:
            print("l'atleta", self.name, "ha effettuato la visita medica")
        else:
            print("l'atleta", self.name, "non ha effettuato la visita medica")

print("inserire il numero di atleti di cui si vogliono inserire i dati: ")
n_athletes = int(input())
print()

athletes = []

for r in range(n_athletes):

    na = str(input("nome: "))
    he = float(input("altezza: "))
    we = float(input("peso: "))
    ag = int(input("età: "))
    athlete_c = athlete(he, we, ag, na)
    print()

    print("inserire il nome della squadra di cui", athlete_c.name, "fa parte: ")
    te = str(input())
    athlete_c.team_a(te)
    print()

    print("per inserire se l'atleta ha effettuato la visita digita: esito")
    print("se non si vuole inserire se l'atleta ha già effettuato la visita premere: invio")
    print("(si darà per scontato che l'abbia già effettuata)")
    question = input()
    if question == "":
        athlete_c.do_medical_examination()
        print()
    else:
        print("se l'atleta ha effettuato la visita digita: si")
        print("se l'atleta non ha effettuato la visita digita: no")
        me = str(input()).lower()
        me = me.strip()
        if me == "si":
            athlete_c.medical_examination = bool(True)
        elif me == "no":
            athlete_c.medical_examination = bool(False)
        else:
            print("considererò la risposta all'ultima domanda come se ti fossi rifiutato/a di rispondere e perciò darò per scontato che la visita sia stata effettuata")
            athlete_c.do_medical_examination()
        print()

    athletes.append(athlete_c)

for a in athletes:
    a.see_datas()
    print()
