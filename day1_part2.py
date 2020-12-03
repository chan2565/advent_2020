with open("day1_input.txt") as file:
    lines = file.readlines()

for line1 in lines:
    for line2 in lines:
        for line3 in lines:
            if (int(line1) == int(line2)) or (int(line1) == int(line3) or (int(line2) == int(line3))):
                continue
            if int(line1) + int(line2) + int(line3)== 2020:
                multi = int(line1) * int(line2) * int(line3)
                print(f"{int(line1)} * {int(line2)} * {int(line3)} = {multi}")