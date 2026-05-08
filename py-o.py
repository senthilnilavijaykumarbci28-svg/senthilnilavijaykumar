for row in range(0, 7):
    for col in range(0, 5):
        # Top and Bottom horizontal caps
        if (row == 0 or row == 6) and (col > 0 and col < 4):
            print('*', end=" ")
        # Vertical sides
        elif (row > 0 and row < 6) and (col == 0 or col == 4):
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()
