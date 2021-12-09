
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

old = 0
count = int()
for i in range(len(list)):
    if int(list[i]) > int(old):
        if old != 0:
            count += 1 
    old = list[i]
    
print(list)
print("len", len(list))
print("count", count)