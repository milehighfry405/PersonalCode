Componets:
    1. Gameboard
    2. Pieces (structs)
        -Long 
        -Square
        - L-shape
        -...
    3. Main



    // Pieces: (x,y) = (width, length)  -- have to make width sizes that when combined with other pieces will not overlay with the size of the screen
        * Each Piece will have a checkMove and a checkSwitch function
        * Each Piece will have a makeMove and a makeSwitch function
        * If the checkMove & checkSwitch returns true, then call makeMove/makeSwitch to actually change that Piece's location    


        1. Long:
            - Has 1x4 coordinates
            - Switch button turns it into a 4x1

        2. Square:
            - Has 2x2 coordinates
            - Switch button does nothing (NULL)


        3. L-Shape(right)
            -Has 2x1 buttom and 1x2 that attaches to the right side of the 2x1
                Ex.   |
                      |
                     _|
            - Switch button turns it into a 2x1 top and 1x2 that attatches to the left side of the 2x1
                Ex.   _
                     |
                     |
                     |

 
       4. L-Shape(left)
            -Has 2x1 bottom and 1x2 that attaches to the left side of the 2x1
                Ex.  |
                     |
                     |_
            - Switch button turns it into a 2x1 top and 1x2 that attatches to the right side of the 2x1
                Ex.  _
                      |
                      |
                      |
   
        5.....



    // GameBoard
        
        1. Draws the basic gameboard coordinates (constructor) - size of the screen (before the while loop in main)
        ______________________________________________
        // IN THE WHILE LOOP (look at Main notes)
        - playGame function

        1. Has gameclock speed of .5 seconds?
        2. Every time clock ticks, move piece down
            - use while loop with a sleep(.5)
            - keep looping until a the piece stops while grabbing user input for switches and moves
        3. When the piece hits another and stops check for:
            - Filled in row, if there is, delete that row and increase points
            - Did that piece break the top of the screen, if so gameover
        4. If not game over...
        5. Randomly generate a new piecbased off of seeded time
        6. Whenever a piece is chosen, creates that new struct and uses its member functions
        7. Repeat this until the game is over
        8. When it reaches the top of the screen set gameOver variable to true
 
    // Main
        
        1. Create the gameboard
        2. While loop to control the game progression
        3. While(game is not over)
            - Call gameboard function playGame
            - When that piece stops break out of the Gameboard function
            - Update the gameOver variable






