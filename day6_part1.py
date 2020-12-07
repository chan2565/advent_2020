with open("day6_input.txt") as file:
    lines = file.read()

questions = "abcdefghijklmnopqrstuvwxyz"
groups = lines.split("\n\n")
total_count = 0

for group in groups:
    group_count = 0
    group = group.replace("\n", "")
    for question in questions:
        if question in group:
            group_count += 1
    total_count += group_count

print(f"Total Count = {total_count}")