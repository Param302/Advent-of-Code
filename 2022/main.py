with open("./inputs/day1.txt") as f:
    raw_data = f.readlines()
# adding extra newline to include last calorie
raw_data.append("\n")

data = []
s = 0
for i in raw_data:
    if i!="\n":
        s += int(i[:-1])
    else:
        data.append(s)
        s = 0

data.sort(reverse=True)

# 1st part: Highest no. of calories carried by an Elf
print(f"1st part solution - {data[0]}")

# 2nd part: Total calories carried by top 3 Elves
print(f"2nd part solution - {sum(data[:3])}")