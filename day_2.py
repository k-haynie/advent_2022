file = open("adv2.txt", "r")

data = file.read()

rounds = data.split("\n")
score = 0

value = {"X": 1, "Y": 2, "Z": 3}

# RPC
tie = {"A": "X", "B": "Y", "C": "Z"}
lose = {"A": "Z", "C": "Y", "B": "X"}
win = {"A": "Y", "B": "Z", "C": "X"}

for i in rounds:
    x = i.split(" ")
    if len(x) > 1:
        opponent = x[0]
        self_c = x[1]
        if self_c == "X":
            self_c = lose[opponent]
        elif self_c == "Y":
            self_c = tie[opponent]
        else:
            self_c = win[opponent]

        if tie[opponent] == self_c:
            outcome = 3
        elif lose[opponent] == self_c:
            outcome = 0
        else:
            outcome = 6

        score += outcome + value[self_c]

print(score)


