Classes:

Game
Die
Player
Computer

Game Class:

    Responsibilities -
        1. Determine turn order
        2. Keep score
        3. Play rounds for player 1 and computer
        4. Run until score hits 100
        5. Ask user if they want to play again

    Collaborators - 
        1. Die
        2. Player
        3. Computer

Die Class:

    Responsibilities -
        1. Roll die (Give each player random number between 1-6)

    Collaborators - 
        1. Game

Player Class:

    Responsibilities - 
        1. Choose to roll or hold
        2. Keep turn score
        3. Keep overall score

    Collaborators - 
        1. Game

Computer:
 
    Responsibilities - 
        1. Hold until 20
        2. Always roll after 20
        3. Keep turn score
        4. Keep overall score

    Collaborators - 
        1. Game

Miscellaneous 
-Need import random
                    