def main():
    grid_size = int(input("How large do you want the grid to be: "))
    start_position = input("Enter the start position of Grid (TL, TR, BR, BL): ")

    if start_position not in ['TL', 'TR', 'BR', 'BL']:
        print("Invalid input")
        exit()

    stop = int(input("Enter stop point: "))
    outer_list = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    row, col = 0, 0

    if start_position == 'TR':
        col = grid_size - 1
    elif start_position == 'BL':
        row = grid_size - 1
    elif start_position == 'BR':
        row = grid_size - 1
        col = grid_size - 1

    element = 1
    for _ in range(stop):
        outer_list[row][col] = element
        if row == 0 and col % 2 == 0:
            col += 1
        elif row == grid_size - 1 and col % 2 != 0:
            col += 1
        elif col == 0 and row % 2 != 0:
            row += 1
        elif col == grid_size - 1 and row % 2 == 0:
            row += 1
        elif row % 2 != 0:
            col -= 1
            row += 1
        else:
            col += 1
            row -= 1
        element += 1

    for lst in outer_list:
        print(lst)

if __name__ == "__main__":
    main()
