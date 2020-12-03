with open("day2_input.txt") as file:
    lines = file.readlines()

num_valid = 0
for line in lines:
    raw_num_alwd = line.split()[0]
    char = line.split()[1].split(":")[0]
    passwd = line.split()[2]
    min_alwd = int(raw_num_alwd.split("-")[0])
    max_alwd = int(raw_num_alwd.split("-")[1])

    if passwd.count(char) in range(min_alwd, max_alwd + 1):
        num_valid += 1

print(f"Valid passwords: {num_valid}")