def part_1():
    with open("2015_2_input.txt") as f:
        input = f.read()

    dimensions = input.split()
    total = 0
    for dimension in dimensions:
        l, w, h = [int(i) for i in dimension.split('x')]
        area = (2*l*w) + (2*w*h) + (2*h*l)
        small = min(l*w, w*h, h*l)
        total += area + small
    print(total)


def part_2():
    with open("2015_2_input.txt") as f:
        input = f.read()

    dimensions = input.split()
    total_ribbon = 0
    for dimension in dimensions:
        sides = [int(i) for i in dimension.split('x')]
        l, w, h = sides

        # a & b are smallest sides
        a = min(sides)
        sides.remove(a)
        b = min(sides)
        small_peri = 2*(a+b)
        
        ribbon_size = small_peri + (l*w*h)
        total_ribbon += ribbon_size
    print(total_ribbon)

part_2()