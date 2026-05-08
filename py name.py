name = "SENTHIL NILA"

for char in name:
    if char == " ":
        print("\n" * 2) # Creates a vertical gap for the space
        continue
        
    print(f"--- {char} ---")
    for row in range(0, 7):
        for col in range(0, 5):
            # S: Curves with rounded corners
            if char == 'S':
                if ((row == 0 or row == 3 or row == 6) and (0 < col < 4)) or \
                   (col == 0 and (0 < row < 3)) or (col == 4 and (3 < row < 6)):
                    print('*', end=" ")
                else: print(' ', end=" ")
            
            # E: Top, middle, bottom and left side
            elif char == 'E':
                if col == 0 or row == 0 or row == 3 or row == 6: print('*', end=" ")
                else: print(' ', end=" ")
            
            # N: Two sides and a diagonal
            elif char == 'N':
                if col == 0 or col == 4 or (row == col and 0 < col < 4) or (row == 4 and col == 2) or (row == 5 and col == 3): 
                    print('*', end=" ")
                else: print(' ', end=" ")
            
            # T: Top bar and center stem
            elif char == 'T':
                if row == 0 or col == 2: print('*', end=" ")
                else: print(' ', end=" ")
                
            # H: Two sides and a middle bridge
            elif char == 'H':
                if col == 0 or col == 4 or row == 3: print('*', end=" ")
                else: print(' ', end=" ")
                
            # I: Top bar, bottom bar, and center stem
            elif char == 'I':
                if row == 0 or row == 6 or col == 2: print('*', end=" ")
                else: print(' ', end=" ")
                
            # L: Left side and bottom bar
            elif char == 'L':
                if col == 0 or row == 6: print('*', end=" ")
                else: print(' ', end=" ")

            # A: Left and right sides, top cap, and middle bar
            elif char == 'A':
                if (row == 0 and 0 < col < 4) or (row > 0 and (col == 0 or col == 4)) or row == 3:
                    print('*', end=" ")
                else: print(' ', end=" ")
        print()
    print()
