from os import path


path = "D:\AdventOfCode\Code\Inputs\Luukku3.txt"
res = []
with open(path, "r") as file:
    for line in file:
        res.append(line.strip())
lists = res

def part1(lists):
    gamma = ""
    epsilon = ""
    for e in range(len(lists[0])):
        data = []
        count = 0
        for i in range(len(lists)):
            data.append(lists[i][e])
        for i in range(len(data)):
            if data[i] == '1':
                count += 1
        if count > len(data) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            epsilon += "1"
            gamma += "0"
    return int(gamma, 2) * int(epsilon, 2)

print(part1(lists))