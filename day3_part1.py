with open("day3_input.txt") as file:
    lines = file.readlines()

def check_slope(slope_x, slope_y, lines=lines):
    x = slope_x
    y = slope_y
    trees_hit = 0

    num_lines = len(lines)
    width = len(lines[0]) - 1
    x_max = width - 1

    while y < num_lines:
        if lines[y][x] == "#":
            trees_hit += 1
        x += slope_x
        y += slope_y
        if x > x_max:
            x = -1 + (x - x_max)
    
    return trees_hit

print(f"Trees hit: {check_slope(slope_x=3, slope_y=1, lines=lines)}")