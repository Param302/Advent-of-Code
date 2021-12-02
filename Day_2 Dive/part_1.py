with open("input.txt", "r") as f:
    instructions = f.readlines()

horizontal, depth = 0, 0

for instruction in instructions:
    way, x = instruction.split()
    match way:
        case "forward":
            horizontal += int(x)
        case "down":
            depth += int(x)
        case "up":
            depth -= int(x)

print(horizontal*depth)
