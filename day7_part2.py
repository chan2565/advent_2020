with open("day7_input.txt") as file:
    lines = file.readlines()
#with open("day7_input_xs.txt") as file:
#    lines = file.readlines()

num_bags = 0

# vibrant beige bags contain 5 plaid turquoise bags, 2 shiny gold bags, 2 clear tan bags, 1 wavy black bag.
def find_bags(super_bags):
    global lines
    global num_bags
    for super_bag in super_bags:
        new_bags = []
        for x in range(super_bag[1]):
            for line in lines:
                split = line.split(" bags contain ")
                bag = split[0]
                contents = split[1]
                if bag == super_bag[0]:
                    sub_bags = contents.split(", ")
                    for sub_bag in sub_bags:
                        sub_split = sub_bag.split()
                        num_in_bag = sub_split[0]
                        if num_in_bag != "no":
                            num_bags += int(num_in_bag)
                            new_bags.append((f"{sub_split[1]} {sub_split[2]}", int(num_in_bag)))
                #print(new_bags)
        find_bags(new_bags)

find_bags(super_bags=[("shiny gold", 1)])
print(f"Number of Bags in shiny gold bag = {num_bags}")