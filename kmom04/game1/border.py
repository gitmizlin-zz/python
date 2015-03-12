#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testing out the curses lib.
"""

import curses

def main(scr):
    """
    Draw a border around the screen, move around using the cursor and leave a mark
    of the latest pressed character on the keyboard.

    Perhaps you could make a nice painting using asciart? 

    Quit using 'q'.
    """
    
    # Clear the screen of any output
    scr.clear()

    # Get screen dimensions
    y1, x1 = scr.getmaxyx()
    y1 -= 1
    x1 -= 1

    y0, x0 = 0, 0
    
    # Get center position
    yc, xc = (y1-y0)//2, (x1-x0)//2

    # Draw a border
    scr.border()

    # Move cursor to center
    scr.move(yc, xc)

    # Refresh to draw out
    scr.refresh()

    # Main loop
    x = xc
    y = yc
    ch = 'o'

    filename = 'border.txt'

    def createMatrix(y, x, filler):
        """
        Create a two-dimensional array and return it. 
        """
        return [[filler for _ in range(x)] for _ in range(y)]

    matrix = createMatrix(y1, x1, "_")    


    def printMatrix(matrix):
        """
        Print the content of the matrix. 
        """
        for row in matrix:
            print("".join(row) + '\n')


    def saveMatrix(matrix):
        """
        Save the content of the matrix to a file. Do this by joining all items in the 
        list and create a string-representing the row and write that string to the file.
        Add a newline to each row. 
        """
        with open(filename, 'w') as f:
            for row in matrix:
                f.write("".join(row) + '\n') 

    

    def loadMatrix(matrix):
        """
        Load the content of the matrix from a file. Do this by reading the lines from the file
        and splitting them into a list by characters. 
        Ignore the newline at each row. 
        """
        begin_x = x0
        begin_y = y0
        height = y1
        width = x1
        win = curses.newwin(height, width, begin_y, begin_x)

        with open(filename, 'r') as f:

            # with \n
            #content = f.readlines()
            
            # without \n
            content = f.read().splitlines()

            # Update each row of the matrix and fill it by using the file content 
            # (may need som care when file and matrix size does not match)
            for y in range(0, len(matrix)):
                matrix[y] = list(content[y])
       
        printMatrix(matrix)

    while True:
        key = scr.getkey()
        
        if key == 'q':
            break
        elif key == 'KEY_UP' and y > y0+1:
            y -= 1
        elif key == 'KEY_DOWN' and y < y1-1:
            y += 1
        elif key == 'KEY_LEFT' and x > x0+1:
            x -= 1
        elif key == 'KEY_RIGHT' and x < x1-1:
            x += 1  
        elif key == 'KEY_UP' and y <= y0+1:
            y = y 
        elif key == 'KEY_DOWN' and y >= y1-1:
            y = y
        elif key == 'KEY_LEFT' and x <= x0+1:
            x = x
        elif key == 'KEY_RIGHT' and x >= x1-1:
            x = x 
        elif key == 's':            
            saveMatrix(matrix)
        elif key == 'o': 
            loadMatrix(matrix)
            continue
        else:
            ch = key   

        # Add the character to matrix
        matrix[y][x] = ch     

        # Draw out the char at cursor position
        scr.addstr(ch)
            
        # Move cursor to new position
        scr.move(y, x)

        # Redraw all items on the screen
        scr.refresh()

if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    input("Press enter to begin playing...")
    curses.wrapper(main)
