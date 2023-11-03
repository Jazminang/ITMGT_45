def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.


def tic_tac_toe(board):
    size = len(board)

    # Check rows, columns, and diagonals for a winner
    for i in range(size):
        # Check rows
        if all(board[i][j] == board[i][0] and board[i][0] != '' for j in range(size)):
            return board[i][0]
        
        # Check columns
        if all(board[j][i] == board[0][i] and board[0][i] != '' for j in range(size)):
            return board[0][i]
    
    # Check main diagonal
    if all(board[i][i] == board[0][0] and board[0][0] != '' for i in range(size)):
        return board[0][0]

    # Check secondary diagonal
    if all(board[i][size - 1 - i] == board[0][size - 1] and board[0][size - 1] != '' for i in range(size)):
        return board[0][size - 1]

    # No winner found
    return "NO WINNER"

board1 = [
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['O', '', 'X'],
]


# Example usage
winner = tic_tac_toe(board1)
print(winner)
