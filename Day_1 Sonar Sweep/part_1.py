with open("input.txt", "r") as f:
    input = f.read().split()

measurements = [int(i) for i in input]

# Evaluating no. of times measurements are increased
increased = 0
for i in range(1, len(measurements)):
    if measurements[i] > measurements[i-1]:
        increased += 1
    
print(increased)