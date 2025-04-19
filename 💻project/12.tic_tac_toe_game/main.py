
# Tic Tac Toe Game.
# This is a simple implementation of the Tic Tac Toe game in Python.
# The game is played on a 3x3 grid, where two players take turns placing their marks (X or O) in empty cells.
# The game ends when one player gets three marks in a row (horizontally, vertically, or diagonally) or when the grid is full (a draw).
# The game will prompt the players for their moves and display the board after each move.


# display borad function.
  
def my_board():
    return [[" " for a in range (3)] for b in range(3)]     # create a 3x3 board with empty spaces 
def display_board(board):
    print("  0 1 2")
    for idx, row in enumerate(board):
        print(f"{idx} {'|'.join(row)}")
        if idx < 2:
            print("  " + "-" * 5)

# === Player loop function ===

def player_move(board,player):
  while True:
      try:
          row = int(input(f"Player {player}, Enter row (0-2)"))       # get row from player
          col = int(input(f"Player {player}, Enter col (0-2)"))       # get column from player

          if board[row][col] == " ":
              board[row][col] = player        # place the player's mark on the board
              break
          else:
              print("Cell already taken. Try again.")
      except(ValueError, IndexError):
          print("Invalid Input. Enter numbers between 0 and 2.")


# === check winer funtion ===

def check_winner(board,player):
    for a in range(3):
        if all (board[a][b] == player for b in range(3)):  # check row
            return True
        if all (board[b][a] == player for b in range(3)):  # check colomn
            return True
    if all (board[a][a] == player for a in range(3)):     # check diagonal
        return True
    if all (board[a][2 - a] == player for a in range(3)):     #Anti-diagonal
        return True
    
    return False

# === board_full function ===

def board_full(board):
    return all(cell != " " for row in board for cell in row)

board = my_board()
current_player = "X"

print("Welcome to Tic Tac Toe!")
print("Player 1 is X and Player 2 is O")
while True:
    display_board(board)           # display the board
    player_move(board, current_player)               # get the player's move
    if check_winner(board, current_player):          # check if the player has won
        display_board(board)        # display the board
        print(f"Player {current_player} wins!")        # display the winner
        break
    if board_full(board):                  # check if the board is full
        display_board(board)               # display the board
        print("It's a draw!")              # display the draw message
        break
    current_player = "O" if current_player == "X" else "X"     # switch players