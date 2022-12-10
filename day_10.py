class sol():
    def __init__(self):
        self.data = open("adv10.txt").read().split("\n")
        self.data.pop() # whenever I read the given files, there's always an empty newline at the very end.

        # vars for part 1
        self.register = 1
        self.cycle = 0
        self.return_val = 0     
        self.vals = [20, 60, 100, 140, 180, 220]   

        # new vars for part 2
        self.temp_line = ""
        self.print_val = []

    # iterate over instructions, call check_cycle
    def first(self):
        for i in range(len(self.data)):
            cmd = self.data[i].strip().split(" ")

            for j in range(len(cmd)):
                self.check_cycle()

                if j == 1:
                    self.register += int(cmd[1])

        print(self.return_val)

    # adds the cycle, adds up return_val if it's every 40th number from 20
    def check_cycle(self):
        self.cycle += 1
        if self.cycle in self.vals:
            self.return_val += (self.cycle * self.register)

    # paraphrasing function first, iterate over commands, update register, call print_cycle
    def second(self):
        for i in range(len(self.data)):
            cmd = self.data[i].strip().split(" ")

            for i in range(len(cmd)):
                self.print_cycle()
                if i == 1:
                    self.register += int(cmd[1])

        [print(i) for i in self.print_val] # ez-pz printing process

    # add new characters to be printed
    def print_cycle(self):
        self.cycle += 1
        
        if len(self.temp_line) in [self.register-1, self.register, self.register+1]:
            self.temp_line += "#"
        else:
            self.temp_line += "."
        
        if self.cycle in [i+20 for i in self.vals]:
            self.print_val.append(self.temp_line)
            self.temp_line = ""

sol().first()
sol().second()