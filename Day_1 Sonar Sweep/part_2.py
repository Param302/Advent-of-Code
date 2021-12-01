with open("input.txt", "r") as f:
    input = f.read().split()

measurements = []

# Adding sum of 3 measurements
for i in range(2, len(input)):
    sums = int(input[i]) + int(input[i-1]) + int(input[i-2])
    measurements.append(sums)

# Evaluating no. of times measurements are increased
increased = 0
for i in range(1, len(measurements)):
    if measurements[i] > measurements[i-1]:
        increased += 1

print(increased)