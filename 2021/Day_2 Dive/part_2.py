with open("input.txt", "r") as f:
    instructions = f.readlines()

horizontal, depth, aim = 0, 0, 0

for instruction in instructions:
    way, x = instruction.split()
    match way:
        case "forward":
            horizontal += int(x)
            depth += (aim*int(x))

        case "down":
            aim += int(x)

        case "up":
            aim -= int(x)

print(horizontal*depth)
