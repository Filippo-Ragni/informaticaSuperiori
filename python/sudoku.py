from random import randint
from random import randrange

riga1 = [0,0,6,0,0,0,9,0,0]
riga2 = [2,9,0,0,5,6,0,0,0]
riga3 = [0,1,0,2,0,7,3,0,0]
riga4 = [0,0,0,0,0,0,6,9,7]
riga5 = [0,4,0,0,0,0,0,1,0]
riga6 = [6,2,9,0,0,0,0,0,0]
riga7 = [0,0,4,3,0,9,0,2,0]
riga8 = [0,0,0,6,4,0,0,8,5]
riga9 = [0,0,7,0,0,0,4,0,0]

print ("sia righe che colonne sono enumerate dalla 0 alla 8; da tenere a mente per il completamento del sudoku")
inizio = input("se vuoi iniziare il sudoku premi -invio-")

errori = 0

if inizio == "":
    print ("da questo momento in poi ricorda che se fai 3 errori o se inserirai -invio-, il gioco si interromperà")
    while True:
        print ()

        print (riga1)
        print (riga2)
        print (riga3)
        print (riga4)
        print (riga5)
        print (riga6)
        print (riga7)
        print (riga8)
        print (riga9)

        print ()

        x = int(input("inserisci il numero della colonna in cui vuoi inserire il numero: "))
        if x < 0 or x > 8:
            while x < 0 or x > 8:
                x = int(input("inserisci il numero della colonna nella quale vuoi inserire il numero: "))

        y = int(input("inserisci il numero della riga in cui vuoi inserire il numero: "))
        if y < 0 or y > 8:
            while y < 0 or y > 8:
                y = int(input("inserisci il numero della riga nella quale vuoi inserire il numero: "))
        else:
            if x == 0 and y == 1:
                print ("non puoi cambiare un numero predefinito")
            elif x == 0 and y == 5:
                print ("non puoi cambiare un numero predefinito")
            elif x == 1 and y == 1:
                print ("non puoi cambiare un numero predefinito")
            elif x == 1 and y == 2:
                print ("non puoi cambiare un numero predefinito")
            elif x == 1 and y == 4:
                print ("non puoi cambiare un numero predefinito")
            elif x == 1 and y == 5:
                print ("non puoi cambiare un numero predefinito")
            elif x == 2 and y == 0:
                print ("non puoi cambiare un numero predefinito")
            elif x == 2 and y == 5:
                print ("non puoi cambiare un numero predefinito")
            elif x == 2 and y == 6:
                print ("non puoi cambiare un numero predefinito")
            elif x == 2 and y == 8:
                print ("non puoi cambiare un numero predefinito")
            elif x == 3 and y == 2:
                print ("non puoi cambiare un numero predefinito")
            elif x == 3 and y == 6:
                print ("non puoi cambiare un numero predefinito")
            elif x == 3 and y == 7:
                print ("non puoi cambiare un numero predefinito")
            elif x == 4 and y == 1:
                print ("non puoi cambiare un numero predefinito")
            elif x == 4 and y == 7:
                print ("non puoi cambiare un numero predefinito")
            elif x == 5 and y == 2:
                print ("non puoi cambiare un numero predefinito")
            elif x == 5 and y == 6:
                print ("non puoi cambiare un numero predefinito")
            elif x == 5 and y == 1:
                print ("non puoi cambiare un numero predefinito")
            elif x == 6 and y == 2:
                print ("non puoi cambiare un numero predefinito")
            elif x == 6 and y == 3:
                print ("non puoi cambiare un numero predefinito")
            elif x == 6 and y == 8:
                print ("non puoi cambiare un numero predefinito")
            elif x == 6 and y == 0:
                print ("non puoi cambiare un numero predefinito")
            elif x == 7 and y == 4:
                print ("non puoi cambiare un numero predefinito")
            elif x == 7 and y == 6:
                print ("non puoi cambiare un numero predefinito")
            elif x == 7 and y == 7:
                print ("non puoi cambiare un numero predefinito")
            elif x == 7 and y == 3:
                print ("non puoi cambiare un numero predefinito")
            elif x == 8 and y == 3:
                print ("non puoi cambiare un numero predefinito")
            elif x == 8 and y == 7:
                print ("non puoi cambiare un numero predefinito")
            else:
                numero = int(input("che numero vuoi inserire?  "))
                if numero < 1 or numero > 9:
                    while numero < 1 or numero > 9:
                        numero = int(input("che numero vuoi inserire?  "))
                if y == 0 and x == 0 and numero == 4:
                    riga1[x] = 4
                elif y == 0 and x == 1 and numero == 7:
                    riga1[x] = 7
                elif y == 0 and x == 3 and numero == 1:
                    riga1[x] = 1
                elif y == 0 and x == 4 and numero == 3:
                    riga1[x] = 3
                elif y == 0 and x == 5 and numero == 8:
                    riga1[x] = 8
                elif y == 0 and x == 7 and numero == 5:
                    riga1[x] = 5
                elif y == 0 and x == 8 and numero == 2:
                    riga1[x] = 2
                elif y == 1 and x == 2 and numero == 3:
                    riga2[x] = 3
                elif y == 1 and x == 3 and numero == 4:
                    riga2[x] = 4
                elif y == 1 and x == 6 and numero == 8:
                    riga2[x] = 8
                elif y == 1 and x == 7 and numero == 7:
                    riga2[x] = 7
                elif y == 1 and x == 8 and numero == 1:
                    riga2[x] = 1
                elif y == 2 and x == 0 and numero == 8:
                    riga3[x] = 8
                elif y == 2 and x == 2 and numero == 5:
                    riga3[x] = 5
                elif y == 2 and x == 4 and numero == 9:
                    riga3[x] = 9
                elif y == 2 and x == 7 and numero == 6:
                    riga3[x] = 6
                elif y == 2 and x == 8 and numero == 4:
                    riga3[x] = 4
                elif y == 3 and x == 0 and numero == 3:
                    riga4[x] = 3
                elif y == 3 and x == 1 and numero == 5:
                    riga4[x] = 5
                elif y == 3 and x == 2 and numero == 1:
                    riga4[x] = 1
                elif y == 3 and x == 3 and numero == 8:
                    riga4[x] = 8
                elif y == 3 and x == 4 and numero == 2:
                    riga4[x] = 2
                elif y == 3 and x == 5 and numero == 4:
                    riga4[x] = 4
                elif y == 4 and x == 0 and numero == 7:
                    riga5[x] = 7
                elif y == 4 and x == 2 and numero == 8:
                    riga5[x] = 8
                elif y == 4 and x == 3 and numero == 9:
                    riga5[x] = 9
                elif y == 4 and x == 4 and numero == 6:
                    riga5[x] = 6
                elif y == 4 and x == 5 and numero == 5:
                    riga5[x] = 5
                elif y == 4 and x == 6 and numero == 2:
                    riga5[x] = 2
                elif y == 4 and x == 8 and numero == 3:
                    riga5[x] = 3
                elif y == 5 and x == 3 and numero == 7:
                    riga6[x] = 7
                elif y == 5 and x == 4 and numero == 1:
                    riga6[x] = 1
                elif y == 5 and x == 5 and numero == 3:
                    riga6[x] = 3
                elif y == 5 and x == 6 and numero == 5:
                    riga6[x] = 5
                elif y == 5 and x == 7 and numero == 4:
                    riga6[x] = 4
                elif y == 5 and x == 8 and numero == 8:
                    riga6[x] = 8
                elif y == 6 and x == 0 and numero == 5:
                    riga7[x] = 5
                elif y == 6 and x == 1 and numero == 8:
                    riga7[x] = 8
                elif y == 6 and x == 4 and numero == 7:
                    riga7[x] = 7
                elif y == 6 and x == 6 and numero == 1:
                    riga7[x] = 1
                elif y == 6 and x == 8 and numero == 6:
                    riga7[x] = 6
                elif y == 7 and x == 0 and numero == 9:
                    riga8[x] = 9
                elif y == 7 and x == 1 and numero == 3:
                    riga8[x] = 3
                elif y == 7 and x == 2 and numero == 2:
                    riga8[x] = 2
                elif y == 7 and x == 5 and numero == 1:
                    riga8[x] = 1
                elif y == 7 and x == 6 and numero == 7:
                    riga8[x] = 7
                elif y == 8 and x == 0 and numero == 1:
                    riga9[x] = 1
                elif y == 8 and x == 1 and numero == 6:
                    riga9[x] = 6
                elif y == 8 and x == 3 and numero == 5:
                    riga9[x] = 5
                elif y == 8 and x == 4 and numero == 8:
                    riga9[x] = 8
                elif y == 8 and x == 5 and numero == 2:
                    riga9[x] = 2
                elif y == 8 and x == 7 and numero == 3:
                    riga9[x] = 3
                elif y == 8 and x == 8 and numero == 9:
                    riga9[x] = 9
                else:
                    errori += 1
                    print ("hai sbagliato")

        if errori >= 3:
            print ("HAI PERSO, HAI COMMESSO TROPPI ERRORI!!")
            break

        if riga1[0] == 4 and riga1[1] == 7 and riga1[2] == 6 and riga1[3] == 1 and riga1[4] == 3 and riga1[5] == 8 and riga1[6] == 9 and riga1[7] == 5 and riga1[8] == 2 and riga2[0] == 2 and riga2[1] == 9 and riga2[2] == 3 and riga2[3] == 4 and riga2[4] == 5 and riga2[5] == 6 and riga2[6] == 8 and riga2[7] == 7 and riga2[8] == 1 and riga3[0] == 8 and riga3[1] == 1 and riga3[2] == 5 and riga3[3] == 2 and riga3[4] == 9 and riga3[5] == 7 and riga3[6] == 3 and riga3[7] == 6 and riga3[8] == 4 and riga4[0] == 3 and riga4[1] == 5 and riga4[2] == 1 and riga4[3] == 8 and riga4[4] == 2 and riga4[5] == 4 and riga4[6] == 6 and riga4[7] == 9 and riga4[8] == 7 and riga5[0] == 7 and riga5[1] == 4 and riga5[2] == 8 and riga5[3] == 9 and riga5[4] == 6 and riga5[5] == 5 and riga5[6] == 2 and riga5[7] == 1 and riga5[8] == 3 and riga6[0] == 6 and riga6[1] == 2 and riga6[2] == 9 and riga6[3] == 7 and riga6[4] == 1 and riga6[5] == 3 and riga6[6] == 5 and riga6[7] == 4 and riga6[8] == 8 and riga7[0] == 5 and riga7[1] == 8 and riga7[2] == 4 and riga7[3] == 3 and riga7[4] == 7 and riga7[5] == 9 and riga7[6] == 1 and riga7[7] == 2 and riga7[8] == 6 and riga8[0] == 9 and riga8[1] == 3 and riga8[2] == 2 and riga8[3] == 6 and riga8[4] == 4 and riga8[5] == 1 and riga8[6] == 7 and riga8[7] == 8 and riga8[8] == 5 and riga9[0] == 1 and riga9[1] == 6 and riga9[2] == 7 and riga9[3] == 5 and riga9[4] == 8 and riga9[5] == 2 and riga9[6] == 4 and riga9[7] == 3 and riga9[8] == 9:
            print ("COMPLIMENTI HAI VINTO!!!")
            break
