from collections import Counter

with open("input.txt", "r") as f:
    bits = f.read().split()

gamma_rate = ""
# iterating every bit of bits
for i in range(len(bits[0])):

    # getting common bits from all bits i'th index
    common = ""
    for bit in bits:
        common += bit[i]

    # Evaluating Gamma rate
    # Counter(common) -> Counts the no. of 0s and 1s in common
    # Counter(common).most_common(1) -> the most common byte of common bytes
    gamma_rate += Counter(common).most_common(1)[0][0]

# epsilon rate is opposite of gamma_rate
epsilon_rate = ""
for i in gamma_rate:
    if i=="1":
        epsilon_rate += "0"
    else:
        epsilon_rate += "1"

power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

print(power_consumption)