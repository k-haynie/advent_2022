file = open("adv_!.txt", "r")

max_vals = []
temp_val = []
double = False
triple = 0

data = file.read().split("\n\n")
data = data
for i in data:
    line = i.split("\n")
    if line[-1] == "":
        line.pop()
    
    
    max_vals.append(sum([int(i) for i in line]))
    
for i in range(3):
    triple += max(max_vals)
    max_vals.remove(max(max_vals))
print(triple)

# print("Max vals", max_vals)