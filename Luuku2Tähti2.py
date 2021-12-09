fname = "Code\Inputs\Luukku 2 Tähti 2.txt"
list = []

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

s = open(fname, "r")
list=s.readlines()

for i in range(len(list)):
    list[i] = list[i].replace("\n","")

def aimCalc(list):
    forward = []
    up = []
    down = []
    pos = int()
    aim = int()
    for i in range(len(list)):
        if "forward" in list[i]:
            forward.append(int(list[i][-1])) 
        elif "up" in list[i]:
            up.append(int(list[i][-1]))
            aim = aim - up[-1]
        elif "down" in list[i]:
            down.append(int(list[i][-1]))
            aim = aim + down[-1]
        pos = aim * forward[-1]
    return pos * sum(forward)

    #forward = [x for x in list if "forward" in x]

def intTranslatePossible(list):
    for i in range(len(list)):
        try:
            int(list[i])
            return True
        except ValueError:
            return False

def valueSum(list):
    value = []
    leng = len(list)
    for i in range(len(list)):
        list.extend(list[i].split())
    del list[0:leng]
    
    for i in range(len(list)):
        if intTranslatePossible(list[i]) == True:
            value.append(int(list[i]))
        else:
            value.append(list[i])
    return value

print(aimCalc(list))
#valFor = valueSum(forward)
#valUp = valueSum(up)
#valDown = valueSum(down)

#print(valFor)
#print(valUp)
#print(valDown)

#print(aimCalc(valFor, valUp))
    
