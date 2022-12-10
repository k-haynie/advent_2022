class Solution():
    def main(self):
        rows = open("adv8.txt", "r").read().split("\n")
        rows.pop()

        cols = []
        rows_dupe = []

        for i in range(len(rows)):
            temp = ""
            for j in rows:
                temp += str(j[i])
            cols.append(temp)

        self.limit = len(rows) - 1

        self.vbix = set()

        for row in range(self.limit+1):
            new_row = []
            for tree in range(self.limit+1):
                tree_val = rows[row][tree]

                left = self.calc(rows[row][:tree+1][::-1], tree_val)
                right = self.calc(rows[row][tree:], tree_val)
                up = self.calc(cols[tree][:row+1][::-1], tree_val)
                down = self.calc(cols[tree][row:], tree_val)
                new_row.append(left * right * up * down)
                
            rows_dupe.append(new_row)

        print(max([max(i) for i in rows_dupe]))

    def calc(self, data, tree_val):
        for i in range(1, len(data)):
            if data[i] >= tree_val:
                return i
        return len(data)-1 if len(data) > 1 else 1

Solution().main()