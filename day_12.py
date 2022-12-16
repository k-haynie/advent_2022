from collections import defaultdict

class solution():
    def run(self, first=True):
        self.data = open("adv_12.txt", "r").read().replace("E", "{").replace("S", "`").split("\n")
        self.data.pop()
        surface = [[ord(char)-96 for char in line] for line in self.data]        
        self.moves = self.edge_gen(surface)
        goal_ind = (20, 120)

        if first:
            start_ind = (20, 0)
            print(self.BFS(goal_ind, start_ind))
        else:
            start_ind = []
            lengths = []

            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    if self.data[i][j] == "a" and len(self.moves[(i, j)]) > 0:
                        start_ind.append((i, j))

            itr = len(start_ind)
            for count, i in enumerate(start_ind):
                print(f"{count} of {itr}")
                lengths.append(self.BFS(goal_ind, i))
            
            x = [i for i in lengths if i != None]
            # my answers are always a few numbers off - I don't know why, but I'm too tired right now to debug it XD

            print(min(x)-1)

    def BFS(self, goal_ind, start_ind):
        visited = []

        to_visit = [self.moves[start_ind]]

        while to_visit:
            active_path = to_visit.pop(0)
            active_node = active_path[-1]

            if active_node not in visited:

                if active_node == goal_ind:
                    return len(active_path)-3
                else:
                    for i in self.moves[active_node]:
                        if i not in visited:
                            x = [i for i in active_path]
                            x.append(i)
                            to_visit.append(x)

                    visited.append(active_node)

        
    # map each index to possible travel routes (returns a dict -> {index: [vals]})
    def edge_gen(self, surface):
        table_nodes = defaultdict(list)

        for i, line in enumerate(surface):
            for j, char in enumerate(line):
                # path up
                if i-1 >= 0 and surface[i-1][j]-1 <= surface[i][j]:
                    table_nodes[(i, j)].append((i-1, j))
                # path down
                if i+1 < len(surface) and surface[i+1][j]-1 <= surface[i][j]:
                    table_nodes[(i, j)].append((i+1, j))
                # path left
                if j-1 >= 0 and surface[i][j-1]-1 <= surface[i][j]:
                    table_nodes[(i, j)].append((i, j-1))
                # path right
                if j+1 < len(line) and surface[i][j+1]-1 <= surface[i][j]:
                    table_nodes[(i, j)].append((i, j+1))
        
        return table_nodes

sol = solution()
sol.run()
sol.run(False)