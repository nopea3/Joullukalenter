file = open("Code\Inputs\Luukku3.txt", "r")
lists=file.readlines()

def oneline(lists, section, s):
    data = []
    Zdata = []
    Odata = []
    for i in range(len(lists)):
        data.append(lists[i][section])
    for i in range(len(data)):
        if data[i] == "0":
            Zdata.append(data[i])
        else:
            Odata.append(data[i])
    if len(Zdata) > len(Odata):
        if s == True:
            return 0
        elif s == False:
            return 1
    else:
        if s == True:
            return 1
        elif s == False:
            return 0

def allLines(list):
    datas = []
    data = ""
    for i in range(len(list[0])):
        datas.append(oneline(list, i, True))
    for i in range(len(datas)):
        data += str(datas[i])
    return data

def invertLines(lists):
    datas = []
    data = ""
    for i in range(len(lists[0])):
        datas.append(oneline(lists, i, False))
    for i in range(len(datas)):
        data += str(datas[i])
    return data

a = int(allLines(lists),2)
b = int(invertLines(lists),2)
print(a * b)