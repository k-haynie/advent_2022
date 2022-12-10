file = open("adv_3.txt", "r")

data = file.read().split("\n")

sum = 0

for i in range(0, len(data), 3):
    x = data[i:i+3]
    
    try:
        recur = ord(list(set.intersection(set(x[0]), set(x[1]), set(x[2])))[0])
        if recur < 97 and recur > 65:
            sum += recur - 38
        elif recur > 96:
            sum += recur - 96
    except:
        pass

print(sum)



