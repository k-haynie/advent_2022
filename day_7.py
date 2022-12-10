def add_up(file, map):
    sum = file.file_size
    for i in file.dirs:
        sum += add_up(map[i+"."+str(file)], map)

    file.size = sum
    return sum

def run():
    class file:
        def __init__(self, name="", parent=None):
            self.parent = parent
            self.name = name
            self.size = 0
            self.files = []
            self.file_size = 0
            self.dirs = []

    data = open("adv7.txt", "r").read().split("\n")
    data.pop()

    dirs = {}
    active_dir = ""
    listing = False

    for line in data:
        
        if line[0:4] == "$ ls":
            listing = True

        elif line[0:4] == "$ cd":
            listing = False
            files = line.split(" ")
            if files[2] == "..":
                active_dir = active_dir.parent
            else:
                active_dir = file(files[2], active_dir)
                
                name = f"{active_dir.name}.{active_dir.parent}"
                dirs[name] = active_dir

        elif listing:
            files = line.split(" ")

            if files[0] == "dir":
                active_dir.dirs.append(files[1])
            else:
                active_dir.files.append(files[1])
                active_dir.file_size += int(files[0])

    add_up(dirs["/."], dirs)

    benchmark = 30000000 - (70000000 - dirs["/."].size)
    print(sorted([(dirs[i].name, dirs[i].size) for i in dirs if dirs[i].size >= benchmark], key=lambda x: x[1]))

run()


    


