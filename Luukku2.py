fname = "Inputs\luukku 2.txt"
list = []

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
# en ees muista

s = open(fname, "r")
list=s.readlines()
#avataan tää

for i in range(len(list)):
    list[i] = list[i].replace("\n","")

# poistetaan noi \n merkinnät koodista

for i in range(len(list)):
    forward = [x for x in list if "forward" in x]
    up = [x for x in list if "up" in x]
    down = [x for x in list if "down" in x]
    #Lisätään listoihin kaikki eteen, ylös ja alas komennot

def intTranslatePossible(list):
    for i in range(len(list)):
        try:
            int(list[i])
            return True
        except ValueError:
            return False
    #tarkistetaan onko jokin mahollista muuttaa int

def valueSum(list):
    value = []
    leng = len(list)
    for i in range(len(list)):
        list.extend(list[i].split())
    del list[0:leng]
    #jaetaan lista seuraavasti ["forward 4"] to ["forward", "4"]
    
    for i in range(len(list)):
        if intTranslatePossible(list[i]) == True:
            value.append(int(list[i]))
        else:
            pass
    #katotaan onko listan kohta mahollinen int. Jos on lisätään listaan ja jatketaan eteenpäin
    return sum(value)


valFor = valueSum(forward)
valUp = valueSum(up)
valDown = valueSum(down)

print(abs(valFor*(valUp-valDown))) #tulostetaan haluttu arvo

    
