"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    y_count = sum(row.count(O) for row in board)
    return X if x_count == y_count else O 

  

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set() 
    
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i,j))
    return possible_moves 

    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action!!!")

    b2 = copy.deepcopy(board)
    b2[action[0]][action[1]] = player(board)
    
    return b2



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
     
    
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != EMPTY:
            return row[0]

    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != EMPTY:
            return check[0]   
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]and board[0][2] != EMPTY:
        return board[0][2] 
    
    
    return None 
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or not actions(board)
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1 
    elif winner(board) == O:
        return -1 
    else:
        return 0 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None, utility(board)
    is_x = player(board) == X
    
    best_value = float('-inf') if is_x else float('inf')
    best_move = None 
    
    for move in actions(board):
        _, value = minimax(result(board,move))
        if is_x:
            if value > best_value:
                best_value = value 
                best_move = move
        else:
            if value < best_value:
                best_value = value 
                best_move = move 
        if best_value == 1 if is_x else best_value == -1:
            break 
    return best_move 
    
