
fname = "Inputs\luukku 1.txt"
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


def calc():
    count = int()
    oldAv = int()
    for i in range(len(list)):
        if i + 3 > len(list):
            return count
        av = (int(list[i]) + int(list[i+1]) + int(list[i+2]))/3
        if av > oldAv:
            if oldAv != 0:
                count += 1
        oldAv = av

print(calc())
