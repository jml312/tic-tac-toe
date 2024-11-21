from typing import Optional, List

class TicTacToe:
  """
  A class to determine the winner of a Tic-Tac-Toe game given a 4x4 board.
  """
  X = 'X'
  O = 'O'
  BLANK = ' '
  VALID_CELLS = [X, O, BLANK]
  
  def __init__(self, board: Optional[List[List[str]]] = None):
    if board:
      # validate board length 
      if len(board) != 4 or any([len(row) != 4 for row in board]):
        raise ValueError('Board must be 4x4')
      # validate board cells
      if any([cell for row in board for cell in row if cell not in self.VALID_CELLS]):
        raise ValueError('Invalid cell in board')
    self.board = board or [[self.BLANK for _ in range(4)] for _ in range(4)]


  def check_winner(self) -> Optional[str]:
    """
    Check if there is a winner in the game. Return 'X' if player X wins, 'O' if player O wins, and None if there is no winner.

    can win in five ways:
    1. vertical
    2. horizontal
    3. diagonal
    4. all four corners
    5. 2x2 box
    """
    
    return self.__check_vertical() or self.__check_horizontal() or self.__check_diagonal() or self.__check_corners() or self.__check_2x2_box()
  
  
  def __check_vertical(self) -> Optional[str]:
    """Check for a vertical win. Returns the winning player if there is a vertical win, None otherwise."""
    for col in range(4):
      if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.board[3][col] and self.board[0][col] != self.BLANK:
        return self.board[0][col]
    return None
  
  
  def __check_horizontal(self) -> Optional[str]:
    """Check for a horizontal win. Returns the winning player if there is a horizontal win, None otherwise."""
    for row in range(4):
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.board[row][3] and self.board[row][0] != self.BLANK:
            return self.board[row][0]
    return None
  
  
  def __check_diagonal(self) -> Optional[str]:
    """Check for a diagonal win. Returns the winning player if there is a diagonal win, None otherwise."""
    if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] and self.board[0][0] != self.BLANK:
      return self.board[0][0]
    if self.board[0][3] == self.board[1][2] == self.board[2][1] == self.board[3][0] and self.board[0][3] != self.BLANK:
      return self.board[0][3]
    return None
  
  
  def __check_corners(self) -> Optional[str]:
    """Check if all four corners are occupied by the same player. Returns the winning player if all four corners are occupied by the same player, None otherwise."""
    if self.board[0][0] == self.board[0][3] == self.board[3][0] == self.board[3][3] and self.board[0][0] != self.BLANK:
      return self.board[0][0]
    return None
  
  
  def __check_2x2_box(self) -> Optional[str]:
    """Check if a 2x2 box is occupied by the same player. Returns the winning player if there is a 2x2 box win, None otherwise."""
    for row in range(3):
      for col in range(3):
        if self.board[row][col] == self.board[row][col + 1] == self.board[row + 1][col] == self.board[row + 1][col + 1] and self.board[row][col] != self.BLANK:
          return self.board[row][col]
    return None
  
  
  def any_moves_left(self) -> bool:
    """
    Check if there are any moves left in the game (there are still blank cells). Return True if there are moves left, False otherwise.
    """
    return any(cell == self.BLANK for row in self.board for cell in row)
  
  def is_game_over(self) -> bool:
    """
    Check if the game is over (there is a winner or no moves left). Return True if the game is over, False otherwise.
    """
    return self.check_winner() or not self.any_moves_left()
  
  def __str__(self) -> str:
    winner = self.check_winner()
    moves_left = self.any_moves_left()
    game_over = self.is_game_over()
    
    board = ''
    for row in self.board:
      board += '-----------------\n'
      board += '| ' + ' | '.join(row) + ' |\n'
    board += '-----------------'
    
    return (
        f"Winner: {winner or 'None'}\n"
        f"Game Over: {'Yes' if game_over else 'No'}\n" 
        f"Moves Left: {'Yes' if moves_left else 'No'}\n"
        f"{board}"
    )  