def make_grid(size, position, stop):
    #  initialize the grid with zeros
    list = [[0 for j in range(size)] for i in range(size)]

    #  Handling the condition for when it's Top-left
    if position == 1:
        for i in range(size):
            element = 1 + i
            for j in range(size):
                if element > stop:
                    list[i][j] = 0
                else:
                    list[i][j] = element
                element += 1
    #  Handling the condition for when it's Top-right
    elif position == 2:
        for i in range(size):
            element = size + i
            for j in range(size):
                #  check for stop target
                if element > stop:
                    list[i][j] = 0
                else:
                    list[i][j] = element
                element -= 1
    #  Handling the condition for when it's Bottom-right
    elif position == 3:
        for i in range(size):
            element = stop - i
            for j in range(size):
                #  check for stop target
                if element > 0:
                    list[i][j] = element
                else:
                    list[i][j] = 0
                element -= 1
    #  Handling the condition for when it's Bottom-left
    elif position == 4:
        for i in range(size):
            element = size - i
            for j in range(size):
                #  check for stop target
                if element > stop:
                    list[i][j] = 0
                else:
                    list[i][j] = element
                element += 1
    return list


def main():
    grid_size = int(input("How large do you want the grid to be: "))
    start_position = int(input("Enter the start position of Grid \n"
                               "(1)-> top-left\n"
                               "(2)-> top-right\n"
                               "(3)-> bottom-right\n"
                               "(4)-> bottom-left: "))
    if 1 < start_position > 4:
        print("Invalid input")
        exit()
    stop = int(input("Enter stop point: "))
    grid = make_grid(grid_size, start_position, stop)
    for row in grid:
        print(row)


if __name__ == "__main__":
    main()
