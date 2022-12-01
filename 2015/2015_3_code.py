def part_1():
    with open("./2015_3_input.txt", "r") as f:
        input = f.read()

    x, y = 0, 0
    houses = set()

    for pole in input:
        match pole:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1
        houses.add((x, y))

    print(len(houses))


def part_2():
    with open("./2015_3_input.txt", "r") as f:
        input = f.read()
    # input = "^v^v^v^v^v"
    sx, sy, rx, ry = 0, 0, 0, 0
    houses = set()
    for i, pole in enumerate(input):
        if i%2:     # odd
            match pole:
                case "^":
                    sy -= 1
                case "v":
                    sy += 1
                case ">":
                    sx += 1            
                case "<":
                    sx -= 1
            houses.add((sx, sy))          
        else:
            match pole:
                case "^":
                    ry -= 1
                case "v":
                    ry += 1
                case ">":
                    rx += 1            
                case "<":
                    rx -= 1
            houses.add((rx, ry))
    print(len(houses))

    
part_2()