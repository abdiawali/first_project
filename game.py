"""
project 1 game
Game: TicTacToe
by: Abdifatah A
"""
import random

#empty board list
empty_board = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"]
# global varibles
continue_the_game = True
who_won= None

# fuction for the steps of the game
def play_game():
    #calls for display function
    display_board()

    # while loop that continues till game is over
    while continue_the_game:
        # calls for players turn function
        player_turn()
        # calls for function that checks if there is winner or tie
        is_game_over()

        if not continue_the_game:
            break

        # function that gets computers random pick
        computer_turn()

        #checks if game is over
        is_game_over()

    #displays the winner if there winner or tie
    if who_won=='X' or who_won=='O':
        print(who_won, 'won the game.')
    elif who_won == None:
        print('the game is tie good luck next time.')

# displays the game board with instructions    
def display_board():
    print(f'| {empty_board[0]} | {empty_board[1]} | {empty_board[2]} |     | 1 | 2 | 3')
    print(f'| {empty_board[3]} | {empty_board[4]} | {empty_board[5]} |     | 4 | 5 | 6')
    print(f'| {empty_board[6]} | {empty_board[7]} | {empty_board[8]} |     | 7 | 8 | 9')

# gets players input 
def player_turn():
    while True:
        try:
            print("Please enter integer between 1-9: ")
            position=int(input()) -1    #stores input as position
            #displays an error message if wrong input is entered
            if position < 0 or position > 8 or empty_board[position] != "-":
                print("you have entered wrong integer or the location is not free.")
            # labels X on players choice on the board and displays the current table
            else:
                empty_board[position] = 'X'
                display_board()
                break
        except:
             print("Enter valid integer between 1-9")
#function that gets computer move
def computer_turn():
    print("Nice move!")
    # gets computer's random pick between 0 to 8
    position = random.randint(0,8)

    #if the position isn't avaliable it tries till empty position
    while empty_board[position] != "-":
        position = random.randint(0,8)    

    #labels O on the board and displays the current board
    empty_board[position] = 'O'
    display_board()

# function checks if game is over by checking is there is winner or tie
def is_game_over():
    win()
    tie()

#function that checks for win
def win():
    global who_won
    #calls for check_row function that specifically looks for 3 in row
    row_win = check_row()

    #calls for check_column function that specifically looks for 3 in same column
    column_win = check_columns()
    
    #calls for check_diagnols function that specifically looks if 3 are same diagnolly
    diagonal_win = check_diagonals()

    #if the is row win sets winner either x or O
    if row_win:
        who_won=row_win
    #if the is column win sets winner either x or O
    elif column_win:
        who_won=column_win
    #if the is diagonal win sets winner either x or O
    elif diagonal_win:
        who_won=diagonal_win
    else:
        who_won=None

# function that checks if there is row winner
def check_row():
    global continue_the_game

    row_1 = empty_board[0] == empty_board[1] and empty_board[1] == empty_board[2] and empty_board[2] != "-"
    row_2 = empty_board[3] == empty_board[4] and empty_board[4] == empty_board[5] and empty_board[5] != "-"
    row_3 = empty_board[6] == empty_board[7] and empty_board[7] == empty_board[8] and empty_board[8] != "-"
 
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        continue_the_game = False
    # Return the winner
    if row_1:
        return empty_board[0] 
    elif row_2:
        return empty_board[3] 
    elif row_3:
        return empty_board[6] 
    # Or return None if there was no winner
    else:
        return None


#function that checks if there column winner
def check_columns():

    global continue_the_game

    # Check if any of the columns have all the same value (and is not empty)
    column_1 = empty_board[0] == empty_board[3] and empty_board[3] == empty_board[6] and empty_board[6] != "-"
    column_2 = empty_board[1] == empty_board[4] and empty_board[4] == empty_board[7] and empty_board[7] != "-"
    column_3 = empty_board[2] == empty_board[5] and empty_board[5] == empty_board[8] and empty_board[8] != "-"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        continue_the_game = False
    # Return the winner
    if column_1:
        return empty_board[0] 
    elif column_2:
        return empty_board[1] 
    elif column_3:
        return empty_board[2] 
    # Or return None if there was no winner
    else:
        return None


#function that checks if there is diagnals winner
def check_diagonals():
    global continue_the_game
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = empty_board[0] == empty_board[4] and empty_board[4] == empty_board[8] and empty_board[8] != "-"
    diagonal_2 = empty_board[2] == empty_board[4] and empty_board[4] == empty_board[6] and empty_board[6] != "-"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        continue_the_game = False
    # Return the winner
    if diagonal_1:
        return empty_board[0] 
    elif diagonal_2:
        return empty_board[2]
    # Or return None if there was no winner
    else:
        return None

# function that checks if positions are all taken and there is no winner 
def tie():
    global continue_the_game
    # If board is full
    if "-" not in empty_board:
        continue_the_game = False
        return True
    # Else there is no tie
    else:
        return False

# calls for play_game function which has all the game steps
play_game()
