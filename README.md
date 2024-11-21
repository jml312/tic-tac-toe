# tic-tac-toe

A Python implementation to determine the winner of a Tic-Tac-Toe game given a 4x4 board.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   ```
2. Change to the project directory:
   ```bash
   cd tic-tac-toe
   ```
    Ensure you have Python installed on your machine.
---
## File Structure

```
main.py - Main program file
input.txt - Input file for the program

tictactoe/
    tictactoe.py - Contains the TicTacToe class

tests/
    test_tictactoe.py - Tests for the TicTacToe class
```

___
## Usage

To run the program, execute the following command:
```bash
python main.py
```

The program will look for a file called `input.txt` in the same directory and should contain 4 lines of 4 characters each. The characters should be either `X`, `O`, or ` `. The program will then output the result of the game. For example, for this `input.txt` file:
```
OXXO
O XX
XOOX
OOXO 
```

The output will be:
```
Winner: O
Game Over: Yes
Moves Left: Yes
-----------------
| O | X | X | O |
-----------------
| O |   | X | X |
-----------------
| X | O | O | X |
-----------------
| O | O | X | O |
-----------------
```



---
## Testing

To run all tests, execute the following command:
```bash
python -m unittest discover -s tests
```

To run a specific test file, execute the following command:
```bash
python -m unittest tests.<test_file>
```