def create_diamond_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("* " * i)
    
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        print("* " * i)

# Usage example
diamond_rows = 5
create_diamond_pattern(diamond_rows)