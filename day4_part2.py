import string

with open("day4_input.txt") as file:
    lines = file.read()

passports = lines.split("\n\n")
valid_passports = 0
passport_index = 0
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
        field_val = field.split(":")[1]
        #print(f"{field_name} = {field_val}")
        if field_name == "byr":
            if (len(field_val) == 4) and (int(field_val) >= 1920) and (int(field_val) <= 2002):
                byr = True
        if field_name == "iyr":
            if (len(field_val) == 4) and (int(field_val) >= 2010) and (int(field_val) <= 2020):
                iyr = True
        if field_name == "eyr":
            if (len(field_val) == 4) and (int(field_val) >= 2020) and (int(field_val) <= 2030):
                eyr = True
        if field_name == "hgt":
            if field_val[-2:] == "in":
                if (int(field_val[:-2]) >= 59) and (int(field_val[:-2]) <= 76):
                    hgt = True
            if field_val[-2:] == "cm":
                if (int(field_val[:-2]) >= 150) and (int(field_val[:-2]) <= 193):
                    hgt = True
        if field_name == "hcl":
            if (len(field_val) == 7) and all(char in string.hexdigits for char in field_val[1:]):
                hcl = True
        if field_name == "ecl":
            if field_val in "amb blu brn gry grn hzl oth":
                ecl = True
        if field_name == "pid":
            if (len(field_val) == 9) and field_val.isdecimal():
                pid = True
    if (byr and iyr and eyr and hgt and hcl and ecl and pid):
        print(passport_index)
        valid_passports += 1
    passport_index += 1

print(f"Valid Passports: {valid_passports}")