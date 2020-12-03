with open("day1_input.txt") as file:
    lines = file.readlines()

for line1 in lines:
    for line2 in lines:
        if int(line1) == int(line2):
            continue
        if int(line1) + int(line2) == 2020:
            multi = int(line1) * int(line2)
            print(f"{int(line1)} * {int(line2)} = {multi}")