file = open("adv6.txt", "r")
data = file.read().split("\n")
found = False

for i in range(0, len(data[0])):
    if len(list({x for x in data[0][i:i+14]})) == len([x for x in data[0][i:i+14]]) and found != True:
        print(data[0][i:i+14])
        print(i+14)
        found = True