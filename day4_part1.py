with open("day4_input.txt") as file:
    lines = file.read()

passports = lines.split("\n\n")
valid_passports = 0
for passport in passports:
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    fields = passport.split()
    for field in fields:
        field_name = field.split(":")[0]
        if field_name == "byr":
            byr = True
        if field_name == "iyr":
            iyr = True
        if field_name == "eyr":
            eyr = True
        if field_name == "hgt":
            hgt = True
        if field_name == "hcl":
            hcl = True
        if field_name == "ecl":
            ecl = True
        if field_name == "pid":
            pid = True
    if (byr and iyr and eyr and hgt and hcl and ecl and pid):
        valid_passports += 1

print(f"Valid Passports: {valid_passports}")
        
