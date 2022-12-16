class sol:
    # parse input and find the occupied spaces for the given row
    def run():
        data = open("adv15.txt", "r").read().split("\n")
        data.pop()

        coord_pairs = []
        row_of_interest = 2000000

        for i in data:
            xs = [j.split(",") for j in i.split("x=")]
            ys = [j.split(":") for j in i.split("y=")]
            sensor = (int(xs[1][0]), int(ys[1][0]))
            beacon = (int(xs[2][0]), int(ys[2][0]))
            coord_pairs.append([sensor[0], sensor[1], beacon[0], beacon[1]])
            
        occupado = set()

        # add occupied spaces to a set of indices - unoptimized compared to my later code, but it works
        for x in coord_pairs:
            manhattan = abs(x[0]-x[2]) + abs(x[1]-x[3])
            if (x[1] < row_of_interest and x[1]+manhattan >= row_of_interest) or (x[1] > row_of_interest and x[1]-manhattan <= row_of_interest):
                for i in range(x[0]-((manhattan-abs(row_of_interest-x[1]))), x[0]+((manhattan-abs(row_of_interest-x[1])))+1):
                    occupado.add((i, row_of_interest))

        # remove beacons from occupado set if there are in row_of_interest
        for x in coord_pairs:
            if x[3] == row_of_interest:
                try:
                    occupado.remove((x[2], x[3]))
                except:
                    pass
        
        # print the answer
        print(len(occupado))

    def run_two():
        data = open("adv15.txt", "r").read().split("\n")
        data.pop()

        coord_pairs = []

        for i in data:
            xs = [j.split(",") for j in i.split("x=")]
            ys = [j.split(":") for j in i.split("y=")]
            sensor = (int(xs[1][0]), int(ys[1][0]))
            beacon = (int(xs[2][0]), int(ys[2][0]))
            coord_pairs.append([sensor[0], sensor[1], beacon[0], beacon[1]])


        for row_of_interest in range(4000001):
            # proof of progress
            if row_of_interest in [500000, 1000000, 2000000, 3000000]:
                print(row_of_interest)

            row_spans = []

            # for each row, find the start and end indices of each sensor's covered territory
            for x in coord_pairs:
                manhattan = abs(x[0]-x[2]) + abs(x[1]-x[3])
                start = x[0]-((manhattan-abs(row_of_interest-x[1])))
                end = x[0]+((manhattan-abs(row_of_interest-x[1])))
                
                if start <= end:
                    row_spans.append([start, end])

            row_spans.sort()

            concat = [row_spans.pop(0)]

            # join adjacent spans to find a missing piece
            while row_spans:
                working = row_spans.pop(0)
                if concat and concat[-1][1]+1 >= working[0] and concat[-1][1] < working[1]:
                    old = concat.pop()
                    concat.append([old[0], working[1]])

            # concat will end earlier than the end of the row if we have found our target index
            if concat[0][1] < 4000000:
                print(1+concat[0][1], row_of_interest)

sol.run()
sol.run_two()