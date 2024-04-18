#Otwiera plik do wczytania
han = open("mbox-short.txt")

#Usuwa znaki końcowe takie jak spacje oraz przedstawia wyrazy w formie listy
for line in han:
    line = line.rstrip()
    wds = line.split()
    #Ustala warunek wczytania wyrazu. Poniżej jest to długość i wyraz poprzedzający
    if len(wds) < 3 or wds[0] != "From" :
        continue
    #Drukuje poszukiwaną wartość
    print(wds[2])