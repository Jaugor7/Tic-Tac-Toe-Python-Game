#!/usr/bin/env python
# coding: utf-8

# In[13]:


board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-",
]
gameIsStillGoing = True
winner = None
currentPlayer = 'X'
def display_board():
    print(board[0]+ "|" + board[1]+ "|" + board[2])
    print(board[3]+ "|" + board[4]+ "|" + board[5])
    print(board[6]+ "|" + board[7]+ "|" + board[8])

#play a Game of tic tac toe
def play_game():
    global winner
    display_board()
    while gameIsStillGoing:
        
        #handle turn
        handle_turn(currentPlayer)
                    
        checkIfGameOver()
        
        #Check if game is over
        flipPlayer()
        
    if winner == 'X' or winner == 'O':
        print(winner + ' WON')
    else:
        print("It's a Tie")
        
def checkIfGameOver():
    checkIfWin()
    checkIfTie()
    
def checkRows():
    global gameIsStillGoing
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    
    if row1 or row2 or row3:
        gameIsStillGoing = False
        
        
    #Return winner X or 0
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[4]
    
    return

def checkColumns():
    global gameIsStillGoing
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'
    
    if col1 or col2 or col3:
        gameIsStillGoing = False
        
        
    #Return winner X or 0
    if col1:
        return board[0]
    if col2:
        return board[3]
    if col3:
        return board[6]
    return


def checkDiagonals():
    global gameIsStillGoing
    diag1 = board[0] == board[4] == board[8] != '-'
    diag2 = board[2] == board[4] == board[6] != '-'
    
    if diag1 or diag2:
        gameIsStillGoing = False
           
    #Return winner X or 0
    if diag1:
        return board[0]
    if diag2:
        return board[2]
    return

    
def checkIfWin():
    global winner
    
#     check rows
    rowWinner = checkRows()
    
#     check column
    columnWinner = checkColumns()
    
#     check doagonal
    diagonalWinner = checkDiagonals()
    
    if rowWinner:
        winner = rowWinner
        
    elif columnWinner:
        winner = columnWinner
        
    elif diagonalWinner:
        winner = diagonalWinner
        
    return


def checkIfTie():
    global gameIsStillGoing
    
    if '-' not in board:
        gameIsStillGoing = False
        
    return

def flipPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = "O"
    elif currentPlayer == 'O':
        currentPlayer = 'X'
    return
    

def handle_turn(player):
    print(player + "'s turn.")
          
    valid = False
          
    while not valid:
        position = int(input("Choose a position from 1-9:")) - 1
        while position not in range(10):
            position = int(input("Error input no 1-9"))- 1
            
        if board[position] == '-':
            valid = True
            break
        else:
            print("Invalid Move")
            
    board[position] = player
    display_board()
    
play_game()


# In[ ]:




