with open("day2_input.txt") as file:
    lines = file.readlines()

num_valid = 0
for line in lines:
    raw_pos = line.split()[0]
    char = line.split()[1].split(":")[0]
    passwd = line.split()[2]
    pos1 = int(raw_pos.split("-")[0])
    pos2 = int(raw_pos.split("-")[1])

    if (passwd[pos1-1] == char) != (passwd[pos2-1] == char):
        num_valid += 1

print(f"Valid passwords: {num_valid}")