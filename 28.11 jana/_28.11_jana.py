#arv=input("arv")
#try:
#    arv=int(arv)
#    print("int")
#except:
#    try:
#        arv=float(arv)
#        print("float")
#    except:
#        print("tekst")

##task1
#from math import* 
#print("Tere! Olen sinu uus sõber - Python!")
#nimi=input("Mis sinu nimi on?")
#print("oi kui ilus nimi!")
#i=input(" Kas leian Sinu keha indeksi?")
#if (i=="0"):
#    print("Aitah!")
#if(i=="1"):
#    p=int(input("pikkus:"))
#    m=int(input("mass:"))
#    print(" Sinu keha indeks on:")
#    i=round(m/(0.01*p)**2,1)
#    print(i)
#    if(i<=16):
#        print("Tervisele ohtlik alakaal")
#    elif(i>16 and i<=19):
#        print("Alakaal")
#    elif(i>19 and i<=25):
#        print("Normaalkaal")
#    elif(i>25 and i<=30):
#        print("Ülekaal")
#    elif(i>30 and i<=35):
#        print("Rasvumine")
#    elif(i>35 and i<=40):
#        print("Tugev rasvumine")
#    elif(i>40):
#        print("Tervisele ohtlik rasvumine")
#print("")
#print("Kahju! See on väga kasulik info!")
#print("")
#print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

from math import*
print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis sinu nimi on?")
print("oi kui ilus nimi!")
a=input(" Kas leian Sinu keha indeksi?")
if a=="1":
    while True:
        try:
            pikkus=int(input("pikkus:"))
            if pikkus>0 and pikkus<273: break
        except:
            print("error")
    mass=-1
    while mass<0 or mass>400:
        try:
            mass=int(input("mass:"))
        except:
            print("error")
    try:
        index=mass/pikkus
        if index<16:
            pass
        elif index>=16 and index<19:
            pass
    except:
        print("error")
