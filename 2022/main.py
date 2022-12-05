with open("./inputs/day5.txt") as f:
    temp_crates = []
    for i in f:
        if i == "\n":
            break
        temp_crates.append(i[:-1])

    moves = []      # [n crates, from, to]
    for move in f:
        _, crates, _, from_stack, _, to_stack = move.strip().split()
        moves.append([int(crates), int(from_stack), int(to_stack)])

temp_crates.pop()

# replacing empty crate slots with 0
for i in range(len(temp_crates)):
    temp_crates[i] = temp_crates[i].replace(' '*4, " 0 ").split()

temp_crates.append(None) if len(temp_crates) < len(temp_crates[0]) else ...

# arranging all crates in their stacks
stacks = {}
stack_no = 1
for i in range(len(temp_crates[i])):
    for j in range(len(temp_crates)-1, -1, -1):
        stacks.setdefault(stack_no, [])
        if temp_crates[j] is None:
            continue
        if temp_crates[j][i]=='0':
            continue
        stacks[stack_no].append(temp_crates[j][i][1])
    stack_no += 1

# Part 1:
for move in moves:
    crates, from_stack, to_stack = move
    for n in range(crates):
        stacks[to_stack].append(stacks[from_stack].pop())

top_stacks = ''.join(stacks[i][-1] for i in stacks)
print(top_stacks)


for move in moves:
    crates, from_stack, to_stack = move
    ordered_crates = []
    for n in range(crates):
        ordered_crates.append(stacks[from_stack].pop())
    stacks[to_stack].extend(ordered_crates[::-1])

top_stacks = ''.join(stacks[i][-1] for i in stacks)
print(top_stacks)