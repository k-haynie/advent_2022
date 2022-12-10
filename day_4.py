file = open("adv_4.txt", "r")

data = file.read().split("\n")

count = 0

for line in data:
    x = line.split(",")

    if len(x) > 1:
        i = [x[0].split("-"), x[1].split("-")]
        i.sort(key=lambda e: int(e[0]))
        first = i[0]
        second = i[1]
    
        
        if int(first[1]) >= int(second[0]):
            count += 1
print(len(data))
print(count)

