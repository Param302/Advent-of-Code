with open("input.txt", "r") as f:
    instructions = f.readlines()

horizontal, depth, aim = 0, 0, 0

for instruction in instructions:
    way, x = instruction.split()
    if way == "forward":
        horizontal += int(x)
        depth += (aim*int(x))

    elif way == "down":
        aim += int(x)

    else:
        aim -= int(x)

print(horizontal*depth)