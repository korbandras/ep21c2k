valaszok=[]
valasz=[]
def kiir(ssz,feladat):
    print('\n%d feladat, %s' %(ssz,feladat))
def f1():
    kiir(1,"file beolvasása")
    be=open("valaszok.txt",'r')
    global megoldas
    megoldas=be.readline().strip()
    for sor in be:
        sor=sor.strip().split()
        valaszok.append(sor)
        valasz.append(sor[1])
    #print(valaszok)
    print("A beolvasás megtörtént")
    #print(valasz)
def f2():
    kiir(2,"versenyzők száma")
    global v
    v=0
    for i in valaszok:
        v+=1
    print("%d versenyző volt a versenyen" %v)
def f3_4():
    kiir(3,'kódhoz tartozóválaszok')
    kod=input("Kérem a versenyző kódját: ")
    ver=0
    for i in valaszok:
        if  i[0]==kod:
            print("%s válaszai: %s" %(kod,i[1]))
        else:
            ver+=1
            if ver==len(valaszok):
                print("Nincs ilyen kódú versenyző")
    kiir(4,"helyes megoldas")
    print("A helyes emegoldás: %s" %megoldas)
    for i in valaszok:
        if i[0]==kod:
            for n in range(len(i[1])):
                if i[1][n]==megoldas[n]:
                    print("+",end='')
                else:
                    print(" ",end='')
def f5():
    kiir(5, 'egy adott feladatra adott helyes válaszok aránya')
    szorszam=int(input("Kérem egy feladat sorszámát (1-14): "))
    szamlalo=0
    if szorszam<1 or szorszam>14:
        print("1 és 14 közti számot kellett megadni")
    else:
        for i in valaszok:
            if i[1][szorszam]==megoldas[szorszam]:
                szamlalo+=1
    arany=szamlalo/v
    print(f'A feladatra {szamlalo} fő, a versenyzők {arany * 100:.2f}%-a adott helyes választ.')
def f6():
    kiir(6,"pontok")
    ki = open("pont.txt", 'w')
    pont=[3,3,3,3,3,4,4,4,4,4,5,5,5,6]
    pontszam=0
    for i in valaszok:
        for j in range(len(megoldas)):
            if i[1][j]==megoldas[j]:
                pontszam+=pont[j]
                j+=1
                if j==14:
                    ki.write("%d %s\n" %(pontszam,i[0]))
                    pontszam=0
    ki.close()
    print("Fileba kirás megtörtént")
def f7():
    kiir(7,"dobogó")
    list=[]
    be=open("pont.txt",'r')
    for sor in be:
        sor=sor.strip().split()
        list.append(sor)
    list2=sorted(list)
    for i in range(3):
        print("%s. helyen végzett %s, %s ponttal" %(i+1,list2[i][1],list2[i][0]))

#-----------------------------
f1()
f2()
f3_4()
f5()
f6()
f7()