from collections import Counter

with open("input.txt", "r") as f:
    bits = f.read().split()

# Evaluate binary number from bits
def rating(bits, i, value):

    # If only one number in bits, so return it
    if len(bits) == 1:
        return bits[0]

    # calculating common bits from all bits i'th index
    common_bits = ""
    for bit in bits:
        common_bits += bit[i]

    # Getting occurrences of both 0s and 1s
    commons = Counter(common_bits).most_common(2)

    # Try bcz when both there is only 1 common i.e. 0 when value is 1
    try:
        # if both counts are common
        if commons[0][1] == commons[1][1]:
            common = value
        else:
            # if value is 1, get most common
            if value == "1":
                common = commons[0][0]
            else:   # else get least common
                common = commons[1][0]

    except IndexError:
        # if two bytes having 0 as common at i'th index
        # then return the bit itself
        return bits[0]

    # Using bytes having common value at i'th index
    common_bytes = [j for j in bits if j[i]==common]
    
    # recursion comes here...
    # i+1, as index of byte increase af per filtering common_bytes
    return rating(common_bytes, i+1, value)


o2_rating = rating(bits, 0, "1")
co2_rating = rating(bits, 0, "0")
life_support_rating = int(o2_rating, 2) * int(co2_rating, 2)
print(life_support_rating)