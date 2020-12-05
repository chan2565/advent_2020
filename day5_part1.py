with open("day5_input.txt") as file:
    lines = file.readlines()

def parse_row(row_str):
    row_split = 128
    row_range = [0, 127]
    for char in row_str:
        # Lower half
        if char == "F":
            row_split = row_split >> 1
            row_range = [row_range[0], row_range[1] - row_split]
            #print(f"Char: {char} Range: {row_range}  Row Split: {row_split}")
        # Upper half
        if char == "B":
            row_split = row_split >> 1
            row_range = [row_range[0] + row_split, row_range[1]]
            #print(f"Char: {char} Range: {row_range}  Row Split: {row_split}")
    return row_range[0]

def parse_col(col_str):
    col_split = 8
    col_range = [0, 7]
    for char in col_str:
        # Lower half
        if char == "L":
            col_split = col_split >> 1
            col_range = [col_range[0], col_range[1] - col_split]
            #print(f"Char: {char} Range: {col_range}  Col Split: {col_split}")
        # Upper half
        if char == "R":
            col_split = col_split >> 1
            col_range = [col_range[0] + col_split, col_range[1]]
            #print(f"Char: {char} Range: {col_range}  Col Split: {col_split}")
    return col_range[0]

def main():
    high_id = 0
    for line in lines:
        row_str = line[:7]
        col_str = line[7:10]
        row = parse_row(row_str=row_str)
        col = parse_col(col_str=col_str)
        #print(f"Row = {row} Col = {col}")
        id = row * 8 + col
        if id > high_id:
            high_id = id
    print(f"Highest ID = {high_id}")

if __name__ == "__main__":
    main()