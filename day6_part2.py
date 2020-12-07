with open("day6_input.txt") as file:
    lines = file.read()

questions = "abcdefghijklmnopqrstuvwxyz"
groups = lines.split("\n\n")
total_count = 0

for group in groups:
    group_count = 0
    people = group.split("\n")
    for question in questions:
        everyone = True
        for person in people:
            if question not in person:
                everyone = False
                break
        if everyone == True:
            total_count += 1

print(f"Total Count = {total_count}")