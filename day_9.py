data = open("adv9.txt", "r").read().split("\n")
data.pop()

t_visit = set((0, 0))

pos = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

for move in data:
    direction = move[0]
    times = int(move[2:])

    for i in range(times):
        if direction == "R":
            pos[0] = (pos[0][0], pos[0][1]+1) # right is positive
        elif direction == "L":
            pos[0] = (pos[0][0], pos[0][1]-1) # left is negative
        elif direction == "U":
            pos[0] = (pos[0][0]+1, pos[0][1]) # up is positive
        elif direction == "D":
            pos[0] = (pos[0][0]-1, pos[0][1]) # down is negative
        
        for i in range(9):
            if abs(pos[i+1][0]-pos[i][0]) > 1 or abs(pos[i+1][1]-pos[i][1]) > 1:

                    # UL, U, or UR
                    if pos[i][1] > pos[i+1][1]:
                        if pos[i][0] < pos[i+1][0]:
                            pos[i+1] = (pos[i+1][0]-1, pos[i+1][1]+1)
                        elif pos[i][0] > pos[i+1][0]:
                            pos[i+1] = (pos[i+1][0]+1, pos[i+1][1]+1)
                        else:
                            pos[i+1] = (pos[i+1][0], pos[i+1][1]+1)

                    # DR, D, or DL
                    elif pos[i][1] < pos[i+1][1]:
                        if pos[i][0] < pos[i+1][0]:
                            pos[i+1] = (pos[i+1][0]-1, pos[i+1][1]-1)
                        elif pos[i][0] > pos[i+1][0]:
                            pos[i+1] = (pos[i+1][0]+1, pos[i+1][1]-1)
                        else:
                            pos[i+1] = (pos[i+1][0], pos[i+1][1]-1)

                    # L or R
                    else:
                        if pos[i][0] < pos[i+1][0]:
                            pos[i+1] = (pos[i+1][0]-1, pos[i+1][1])
                        else:
                            pos[i+1] = (pos[i+1][0]+1, pos[i+1][1])

                    if i == 8:
                        t_visit.add(pos[i+1])

print(len(list(t_visit)))