with open("day5_input.txt") as file:
    lines = file.readlines()

from day5_part1 import parse_col, parse_row

def main():
    ids = []
    for line in lines:
        row_str = line[:7]
        col_str = line[7:10]
        row = parse_row(row_str=row_str)
        col = parse_col(col_str=col_str)
        #print(f"Row = {row} Col = {col}")
        id = row * 8 + col
        ids.append(id)
    ids.sort()
    i = 1
    for id in ids:
        try:
            if not (id == (ids[i] - 1)):
                print(f"My ID = {(ids[i] - 1)}")
            i += 1
        except(IndexError):
            break


if __name__ == "__main__":
    main()