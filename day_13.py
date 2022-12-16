import ast

# NOTICE
# this code is still a work in progress. Surprisingly, aside from the modular/monkey problem, 
# this problem puzzles me. If I have free time another day I plan on debugging it further. 

def compare(x, outlier, count):
    print("comparing", x)
    print(type(x[0]), type(x[1]))


    # TWO INTS
    if type(x[0]) == int and type(x[1]) == int:
        print("ints", x[0], x[1])
        if x[0] < x[1]:
            print("Less than")
            print(f"FOUND: {x}\n")
            outlier.add(count)
            return True
        elif x[1] > x[0]:
            return False
        else:
            pass

    # two lists
    elif type(x[0]) == list and len(x[0]) >= 1 and type(x[1]) == list and len(x[1]) >= 1:

        try:
            val = False
            while x[1] and not val:
                y = x[0].pop(0)
                z = x[1].pop(0)
                val = compare((y, z), outlier, count)
                print("yzval", y, z, val)
            return val
        except IndexError:
            return True

    # INT AND LIST
    elif type(x[0])== int and type(x[1]) == list:
        x[0] = [x[0]]
        return compare((x[0], x[1]), outlier, count)
    # LIST AND INT
    elif type(x[1]) == int and type(x[0]) == list:
        x[1] = [x[1]]
        return compare((x[0], x[1]), outlier, count)

def run():
    data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split("\n\n")

    #data = open("adv_13.txt", "r").read().split("\n\n")

    packs = []
    outlier = set()

    for count, pack in enumerate(data):
        # dash represents list terminal
        x = pack.split("\n")
        formatted = (ast.literal_eval(x[0]), ast.literal_eval(x[1]))
        packs.append(formatted)
        print('\n')
        print(bool(compare(formatted, outlier, count+1)))
    
    print(outlier)

run()