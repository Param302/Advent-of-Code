with open("./inputs/day3.txt") as f:
    all_rucksacks = [i.strip() for i in f]

def map_lowercase_items(item): return ord(item)-96
def map_uppercase_items(item): return ord(item) % 65 + 27

# Part 1
sump = 0
for rucksack in all_rucksacks:
    rucksack = rucksack.strip()
    n = len(rucksack)
    first, second = set(rucksack[:n//2]), set(rucksack[n//2:])  # compartments
    common_item = first.intersection(second).pop()
    # print(x)
    sump += map_lowercase_items(common_item) if common_item.islower() else map_uppercase_items(common_item)
print(sump)


# Part 2
sump = 0
for ind, rucksack in enumerate(all_rucksacks, 1):
    if ind % 3 == 0:    # get each group
        # print(f"Index: {ind}")
        first_rs = set(all_rucksacks[ind-3])
        sec_rs = set(all_rucksacks[ind-2])
        third_rs = set(all_rucksacks[ind-1])
        sec_rs.intersection_update(third_rs)
        common_item = first_rs.intersection(sec_rs).pop()
        sump += map_lowercase_items(common_item) if common_item.islower(
        ) else map_uppercase_items(common_item)
print(sump)


