with open("day7_input.txt") as file:
    lines = file.readlines()
#with open("day7_input_xs.txt") as file:
#    lines = file.readlines()

bags = set()

# vibrant beige bags contain 5 plaid turquoise bags, 2 shiny gold bags, 2 clear tan bags, 1 wavy black bag.
def find_gold(goldmembers):
    global lines
    global bags
    for goldmember in goldmembers:
        new_goldmembers = []
        for line in lines:
            split = line.split(" bags contain ")
            bag = split[0]
            contents = split[1]
            if goldmember in contents:
                bags.add(bag)
                new_goldmembers.append(bag)
        find_gold(new_goldmembers)

find_gold(goldmembers=["shiny gold bag"])
print(f"Number of Colors w/ shiny gold bag = {len(bags)}")
