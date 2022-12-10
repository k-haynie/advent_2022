file = open("adv5.txt", "r")
data = file.read().split("\n")

stacks = [[data[line][i:i+4].strip() for i in range(0, len(data[line]), 4)] for line in range(8)]

formatted = [[] for i in stacks[0]]

for i in stacks:
    for count,j in enumerate(i):
        if j != "":
            formatted[count].insert(0, j[1])

count = 0
for i in data[10:]:
    
    if len(i) >= 18:
        count += 1
        line = i.split(" ")

        if len(line) > 1:
            num = int(line[1])
            origin = int(line[3])-1
            to = int(line[5])-1

            index = len(formatted[to])
            for j in range(num):
                formatted[to].insert(index, formatted[origin].pop())

print("".join(i.pop() for i in formatted))