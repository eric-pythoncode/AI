import random
from colorama import init, Fore, Style
init(autoreset=True)

def displayboard(board):
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    
    print(' ' + colored(board(0)) + ' | ' + colored(board(1)) + ' | '+colored(board(2)))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board(3)) + ' | ' + colored(board(4)) + ' | '+colored(board(5)))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board(6)) + ' | ' + colored(board(7)) + ' | '+colored(board(8)))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print()

def playerchoice():
    symbol = ""
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O?" + Style.RESET_ALL).upper()
    if symbol == "X":
        return ("X", "O")
    else:
        return ("O", "X")
def playermove(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9")
    board[move - 1] = symbol

def aimove(board, aisymbol, playersymbol):
    for i in range(9):
        if board[i].isdigit():
            boardcopy = board.copy()
            boardcopy[i] = aisymbol
            if checkwin(boardcopy, aisymbol):
                board[i] = aisymbol
                return
    for i in range(9):
            if board[i].isdigit():
                boardcopy = board.copy()
                boardcopy[i] = playersymbol
                if checkwin(boardcopy, playersymbol):
                    board[i] = aisymbol
                    return
                
def checkwin(board, symbol):
    windconditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for cond in windconditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
        return False
def checkfull(board):
    return all(not spot.isdigit() for spot in board)

def tictactoe():
    print("Welcome to Tic Tac Toe")
    playername = input(Fore.GREEN + "Enter your name here: " + Style.RESET_ALL)
    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8']
        playersymbol, aisymbol = playerchoice()
        turn = 'Player'
        gameon = True

        while gameon:
            if turn == 'Player':
                playermove(board, playersymbol)
                if checkwin(board, playersymbol):
                    displayboard(board)
                    print(f"Congratulations! {playername} has won the game!")
                    gameon = False
                else:
                    if checkfull(board):
                        displayboard(board)
                        print("Tie")
                        break
                    else:
                        turn = 'Player'

        playagain = input("Do you want to play again? - yes/no").lower()
        if playagain != "yes":
            print("Thank you for playing")
            break

if __name__ == "__main__":
    tictactoe()
