"""Tic Tac Toe Program
CSE 210 - Section 6 - Shaira Silos
Brother Eric Carter
January 2022
"""

def main():
    print('Welcome to Tic Tac Toe!')
    theBoard = [' '] * 9
    create_board(theBoard)

def create_board(values):
    """Create Tic Tac Toe Board"""
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

# Call main to start this program.
if __name__ == "__main__":
    main()