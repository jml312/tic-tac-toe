from tictactoe.tictactoe import TicTacToe

def main():
  board = parse_input_file()
  
  try:
    tic_tac_toe = TicTacToe(board)
  except ValueError as e:
    raise ValueError(e)
    
  print(tic_tac_toe)
  

def parse_input_file():
  with open("input.txt", "r") as f:
    return [[cell for cell in line[:4]] for line in f.readlines()]
  
  
if __name__ == "__main__":
  main()