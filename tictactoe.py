
step 1 :  a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.


# from IPython.display import clear_output
def display_board(board):
#     clear_output()
    print('\n'*100)
    print('  |'+' |')
    print(' '+board[7]+'|'+board[8]+'|'+board[9])
    print('  |'+' |')
    print('- - - -')
    print('  |'+' |')
    print(' '+board[4]+'|'+board[5]+'|'+board[6])
    print('  |'+' |')
    print('- - - -')
    print('  |'+' |')
    print(' '+board[1]+'|'+board[2]+'|'+board[3])
    print('  |'+' |')



Step 2: function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def player_input():
    
    marker = ''
    while marker !='x' and marker != 'o':
        marker = input('pls select x or o ')
    if marker =='x':
        return('x','o')
    else:
        return ('o','x')



Step 3:function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position]= marker
 

 

Step 4: function that takes in a board and a mark (X or O) and then checks to see if that mark has won

def win_check(board, mark):
    return ((board[1] == mark and  board[2] ==mark and   board[3] == mark) or
             (board[4] == mark and board[5] == mark and board[6] == mark)or
            (board[7] == mark and  board[8] ==  mark and  board[9] == mark)or
            (board[7] == mark and  board[8] == mark and  board[9] == mark)or
           (board[1] == mark and   board[4] == mark and  board[7] == mark)or
           (board[2] == mark and  board[5] ==  mark and  board[8] == mark)or
           (board[3] == mark and  board[6] == mark and  board[9] == mark)or
           (board[1] == mark and  board[5] == mark and  board[9] == mark)or
           (board[3] ==  mark and  board[5] == mark and  board[7] == mark))
   
 

Step 5:function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
       
import random

def choose_first():
    if random.randint(0,1)==0:
        return 'player1'
    else:
        return 'player2'



 Step 6:function that returns a boolean indicating whether a space on the board is freely available.   
 
def space_check(board, position):
    return board[position] == ' '
 
   

Step 7:function that checks if the board is full and returns a boolean value. True if full, False otherwise.


def full_board_check(board):
    for i in range(1,10):
        if space_check(board ,i):
            return False
    return True



Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

 
def player_choice(test_board):
    position = 0
    while position not in range(1,10) or not space_check(test_board, position):
        position = int(input('pls enter number between 1 to 9 :'))
    return position    



Step 9:function that asks the player if they want to play again and returns a boolean True if they do want to play again.


def replay():
    choice = input('do you want to play the game yes or no')
    return choice == yes
 


 Step 10: Using  while loops and the functions you've made to run the game!
   
print('welcome to tic tac toe')  
while True:
    board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()  
    print(turn + 'will go first') 
    play_game= input('do you want to play the game y or n')
    if play_game == 'y':
        game_on =  True
    else:
        game_on = False

    while game_on:
        if turn == 'player1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print("player 1 has won")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("the game is a tie")
                    game_on = False
                else:
                    turn = 'player2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print("player 2 has won")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("the game is a tie")
                    game_on = False
                else:
                    turn = 'player1'
    if not replay():
        break
        
        
            
            
            
            
            
       
