pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
with open("input.txt", "r") as f:
    pos = [int(i) for i in f.read().split(',')]

# Dictionary holding fuel for each , total fuel
fuels = {}
for i in range(len(pos)):
    fuel = 0
    for p in pos:
        if p < i:
            f = i - p
        else:
            f = p - i

        fuel += f

    fuels[i] = fuel

# minimum fuel
a = min(fuels, key=lambda x : fuels[x])
print(a, fuels[a])