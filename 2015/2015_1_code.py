def part_1():
    with open("2015_1_input.txt") as f:
        input = f.read()
    # input = "()())"
    # input = ")"
    floor = 0
    for i in range(len(input)):
        if input[i]=="(":
            floor += 1
        else:
            floor -= 1
            
    print(floor)

def part_2():
    with open("2015_1_input.txt") as f:
        input = f.read()
    # input = "()())"
    # input = ")"
    floor = 0
    for i in range(len(input)):
        if input[i]=="(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print(input.index(input[i], i)+1)
            break