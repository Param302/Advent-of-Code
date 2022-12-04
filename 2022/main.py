with open("./inputs/day4.txt") as f:
    assignment_pairs = [
        [
            set(range(int(i.split('-')[0]), int(i.split('-')[1])+1))
            for i in pair.split(',')
        ] 
        for pair in f
        ]

# Part 1
n_fully_contains = 0
for i in assignment_pairs:
    pair1, pair2 = i
    if pair1.issubset(pair2) or pair2.issubset(pair1):
        n_fully_contains += 1

print(n_fully_contains)


# Part 2
def is_overlap(pair1, pair2):
    p1_in_p2 = any(i in pair2 for i in pair1)
    p2_in_p1 = any(i in pair1 for i in pair2)
    return p1_in_p2 and p2_in_p1

n_overlaps = 0
for i in assignment_pairs:
    pair1, pair2 = i
    if is_overlap(pair1, pair2):
        n_overlaps += 1
print(n_overlaps)