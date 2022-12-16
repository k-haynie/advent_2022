# not gonna lie - I got pretty stuck on this one.
# after spending a day or two puzzling over it in my free time, 
# I suspected that the modulus and remainders were significant, 
# but had to turn to reddit for the clues on what modulus to use and where. 

class Monkey():
    def __init__(self, items, op, test_num, left=None, right=None, mod=None,):
        self.items = items
        self.op = op # parse output to calcs - direct call to self.operation
        self.test_num = test_num
        self.left = left
        self.right = right
        self.inspected = 0
        self.mod = 0

    def inspect(self, first):
        for i in range(0, len(self.items)):
            self.inspected += 1

            gift = self.items.pop(0)
            return_gift = 0

            x = self.op.split(" ")
            if x[2] == "old":
                return_gift = gift**2 % self.mod
            elif x[1] == "+":
                return_gift = gift + int(x[2])
            elif x[1] == "*":
                return_gift = gift * int(x[2])
            
            if first:
                return_gift = return_gift // 3

            if return_gift % self.test_num == 0:
                self.left.items.append(return_gift)
            else:
                self.right.items.append(return_gift)

class solution:
    def run(first=True):
        data = open("adv11.txt", "r").read().split("Monkey")
        data.pop(0)
        print(len(data))
        troop = []

        # generate monkeys with appropriate info
        for monkey in data:
            x = monkey.split("\n")
            items = [int(i) for i in x[1].split(": ")[1].split(", ")]
            operation = x[2].split("= ")[1]
            test_num = int(x[3].split("divisible by ")[1])
            left = int(x[4].split("monkey ")[1])
            right = int(x[5].split("monkey ")[1])
            print(left, right)

            troop.append(Monkey(items, operation, test_num, left, right))

        modulus = 1
        for monkey in troop:
            modulus *= monkey.test_num

        # link appropriate monkeys to their throw-potential objects
        for monkey in troop:
            print(monkey.left, monkey.right)
            monkey.left = troop[monkey.left]
            monkey.right = troop[monkey.right]
            monkey.mod = modulus

        # simulate 20 rounds
        rounds = 20 if first else 10000

        for i in range(rounds):
            if i % 500 == 0 or i == 19 or i == 20 or i == 1:
                print("ROUND: ", i)
                [print(monkey.inspected) for monkey in troop]
            for monkey in troop:
                monkey.inspect(first)
        
        inspect_nums = [monkey.inspected for monkey in troop]
        max_1 = max(inspect_nums)
        inspect_nums.remove(max_1)
        max_2 = max(inspect_nums)
        print(max_1, max_2)
        print(max_1 * max_2)

# solution.run()
solution.run(False)