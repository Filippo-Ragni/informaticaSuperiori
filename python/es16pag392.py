print ("")
print ("(prima di calcolare le miglia e le iarde percorse ricorda che se devi inserire un numero decimale devi mettere il punto e non la virgola)")
print ("")
pr = float(input("chilometri percorsi nella prima tappa: "))
se = float(input("chilometri percorsi nella seconda tappa: "))
te = float(input("chilometri percorsi nella terza tappa: "))
print ("")
c = pr+se+te
m = c/1.609
i = m*1760
print ("il viaggio è lungo: ", c, "chilometri/", m, "miglia/", i, "iarde")
