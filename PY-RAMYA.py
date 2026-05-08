name = "RAMYA"

for char in name:
    print(f"--- {char} ---")
    for row in range(0, 7):
        for col in range(0, 5):
            # R: A vertical line, a curved top, and a diagonal leg
            if char == 'R':
                if col == 0 or (row == 0 or row == 3) and (col < 4) or \
                   (col == 4 and row in (1, 2)) or (row == col + 2 and row > 3):
                    print('*', end=" ")
                else: print(' ', end=" ")
            
            # A: Left and right sides, top cap, and middle bar
            elif char == 'A':
                if (row == 0 and 0 < col < 4) or (row > 0 and (col == 0 or col == 4)) or row == 3:
                    print('*', end=" ")
                else: print(' ', end=" ")

            # M: Two sides and a "V" shape in the middle
            elif char == 'M':
                if col == 0 or col == 4 or (row == col and row < 3) or (row + col == 4 and row < 3):
                    print('*', end=" ")
                else: print(' ', end=" ")

            # Y: A "V" shape that meets at the center and a vertical stem
            elif char == 'Y':
                if (row == col and row < 3) or (row + col == 4 and row < 3) or (col == 2 and row >= 3):
                    print('*', end=" ")
                else: print(' ', end=" ")
                
        print()
    print()
