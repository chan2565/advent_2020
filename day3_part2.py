from day3_part1 import check_slope

with open("day3_input.txt") as file:
    lines = file.readlines()

trees_hit1 = check_slope(slope_x=1, slope_y=1, lines=lines)
trees_hit2 = check_slope(slope_x=3, slope_y=1, lines=lines)
trees_hit3 = check_slope(slope_x=5, slope_y=1, lines=lines)
trees_hit4 = check_slope(slope_x=7, slope_y=1, lines=lines)
trees_hit5 = check_slope(slope_x=1, slope_y=2, lines=lines)

mult_totals = trees_hit1 * trees_hit2 * trees_hit3 * trees_hit4 * trees_hit5

print(f"{trees_hit1} * {trees_hit2} * {trees_hit3} * {trees_hit4} * {trees_hit5} = {mult_totals}")