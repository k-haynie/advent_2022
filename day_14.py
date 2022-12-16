class sol:
    def setup(self):
        file = open("day_14.txt", "r").read()
        data = [i.split(" -> ") for i in file.split("\n")]
        #data = [i.split(" -> ") for i in """498,4 -> 498,6 -> 496,6
#503,4 -> 502,4 -> 502,9 -> 494,9""".split("\n")]

        # parse the input into a list of index pairs
        scans = []

        for line in data:
            temp = []
            for x in range(0, len(line)-1):
                left = line[x].split(",")
                right = line[x+1].split(",")
                temp.append([int(left[0]), int(left[1]), int(right[0]), int(right[1])])
            [scans.append(i) for i in temp]

        # establish values for grid initialization
        # for part 2 - adjusted values
        self.min_x = min(min(scans, key=lambda x: x[2])[2], sorted(scans)[0][0])
        self.max_x = max(max(scans, key=lambda x: x[2])[2], sorted(scans, reverse=True)[0][0])
        self.max_y = max(max(scans, key=lambda x: x[3])[3], sorted(scans, reverse=True)[0][1]) + 2
        print(self.min_x, self.max_x, self.max_y)

        # initialize an empty grid
        self.board = []

        # for part 2 - changed to self.max_y+2
        for i in range(0, self.max_y):
            temp = []
            for j in range(0, self.max_x-self.min_x+1):
                temp.append(".")
            self.board.append(temp)

        # add rocks from input  
        for val in scans:
            # down
            if val[0] == val[2] and val[1] > val[3]:
                for i in range(val[3], val[1]+1):
                    self.board[i][val[0]-self.min_x] = "#"
            # up
            elif val[0] == val[2] and val[1] < val[3]:
                for i in range(val[1], val[3]+1):
                    self.board[i][val[0]-self.min_x] = "#"
            # right
            elif val[1] == val[3] and val[0] > val[2]:
                for i in range(val[2]-self.min_x, val[0]+1-self.min_x):
                    self.board[val[1]][i] = "#"
            # left
            else:
                for i in range(val[0]-self.min_x, val[2]+1-self.min_x):
                    self.board[val[1]][i] = "#"

        self.pad = 0
        # part 2 - pad sides to make room for a triangle
        for i in range(0, 500-self.min_x):
            self.pad += 1
            for line in self.board:
                line.insert(0, ".")
        for i in range(0, self.max_y+3-(self.max_x-500)):
            for line in self.board:
                line.append(".")

        # for part 2 - added floor
        self.board.append(["#" for i in range(0, len(self.board[0]))])
        self.max_y += 2

        #self.run()
        self.run(False)
        self.visualize()

    # count up until it overflows
    def run(self, first=True):
        self.overflow = False
        itr = -1
        fall = 500-self.min_x+self.pad
 
        while self.overflow == False:
            itr += 1
            self.fall((fall, 0), first)
            
        self.visualize()
        print(itr)

    # print a board
    def visualize(self):
        print("".join([" " for i in range(500-self.min_x-1)]), "+")
        [print("".join([x for x in i])) for i in self.board]

    # recursively drop a piece lower, then left, then right until an end is reached
    def fall(self, coord, first=True):
        col,row = coord[0], coord[1]

        if row < self.max_y and self.board[row+1][col] == ".":
            self.fall((col, row+1))
        elif row < self.max_y and col > 0 and self.board[row+1][col-1] == ".":
            self.fall((col-1, row+1))
        elif row < self.max_y and col < self.max_x and self.board[row+1][col+1] == ".":
            self.fall((col+1, row+1))
        elif not first and coord[1] == 0:
            self.overflow = True
        elif col-1 == -1 and first:
            self.overflow = True
        else:
            self.board[row][col] = "o"

sol().setup()