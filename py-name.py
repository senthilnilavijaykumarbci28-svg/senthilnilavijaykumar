name = "SENTHILNILA"

for char in name:
    print(f"--- {char} ---")
    for row in range(0, 7):
        for col in range(0, 5):
            if char == 'S':
                if (row == 0 or row == 3 or row == 6) and (col > 0 and col < 4): print('*', end=" ")
                elif (row == 1 or row == 2) and col == 0: print('*', end=" ")
                elif (row == 4 or row == 5) and col == 4: print('*', end=" ")
                else: print(' ', end=" ")
            
            elif char == 'E':
                if (row == 0 or row == 3 or row == 6) or (col == 0): print('*', end=" ")
                else: print(' ', end=" ")
            
            elif char == 'N':
                if col == 0 or col == 4 or (row == col and col > 0 and col < 4): print('*', end=" ")
                else: print(' ', end=" ")
            
            elif char == 'T':
                if row == 0 or col == 2: print('*', end=" ")
                else: print(' ', end=" ")
                
            elif char == 'H':
                if col == 0 or col == 4 or row == 3: print('*', end=" ")
                else: print(' ', end=" ")
                
            elif char == 'I':
                if row == 0 or row == 6 or col == 2: print('*', end=" ")
                else: print(' ', end=" ")
                
            elif char == 'L':
                if col == 0 or row == 6: print('*', end=" ")
                else: print(' ', end=" ")

            elif char == 'A':
                if (row == 0 and 0 < col < 4) or (row > 0 and (col == 0 or col == 4)) or (row == 3): print('*', end=" ")
                else: print(' ', end=" ")
        print()
    print() # Space between letters
