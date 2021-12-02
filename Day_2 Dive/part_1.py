with open("input.txt", "r") as f:
    instructions = f.readlines()

horizontal, depth = 0, 0

for instruction in instructions:
    way, x = instruction.split()
    if way == "forward":
        horizontal += int(x)
    elif way == "down":
        depth += int(x)
    else:
        depth -= int(x)

print(horizontal*depth)