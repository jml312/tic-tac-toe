import unittest

from tictactoe.tictactoe import TicTacToe

X = TicTacToe.X
O = TicTacToe.O
BLANK = TicTacToe.BLANK

class TestTicTacToe(unittest.TestCase):
  def setUp(self):
    self.tic_tac_toe = TicTacToe()
    
    
  def test_check_winner(self):
    # test no winner
    self.assertIsNone(self.tic_tac_toe.check_winner())
    
    # test vertical win
    self.tic_tac_toe.board = [
      [X, BLANK, O, O],
      [X, BLANK, X, O],
      [X, BLANK, BLANK, O],
      [X, BLANK, O, X]
    ]
    self.assertEqual(self.tic_tac_toe.check_winner(), X)
    
    # test horizontal win
    self.tic_tac_toe.board = [
      [X, X, X, X],
      [O, O, X, O],
      [O, X, O, BLANK],
      [X, O, O, BLANK]
    ]
    self.assertEqual(self.tic_tac_toe.check_winner(), X)
    
    # test diagonal win
    self.tic_tac_toe.board = [
      [X, BLANK, O, BLANK],
      [O, X, O, O],
      [BLANK, BLANK, X, BLANK],
      [BLANK, BLANK, BLANK, X]
    ]
    self.assertEqual(self.tic_tac_toe.check_winner(), X)
    
    # test all four corners win
    self.tic_tac_toe.board = [
      [X, O, O, X],
      [O, X, X, O],
      [O, BLANK, BLANK, O],
      [X, BLANK, BLANK, X]
    ]
    self.assertEqual(self.tic_tac_toe.check_winner(), X)
    
    # test 2x2 box win
    self.tic_tac_toe.board = [
      [BLANK, O, O, BLANK],
      [O, X, X, O],
      [BLANK, X, X, O],
      [BLANK, BLANK, BLANK, X]
    ]
    self.assertEqual(self.tic_tac_toe.check_winner(), X)  
    
    # test tie
    self.tic_tac_toe.board = [
      [O, O, X, X],
      [O, X, O, X],
      [X, O, X, O],
      [O, X, O, X]
    ]
    self.assertIsNone(self.tic_tac_toe.check_winner())
  
  
  def test_any_moves_left(self):
    # test empty board
    self.assertTrue(self.tic_tac_toe.any_moves_left())
    
    # test no moves left
    self.tic_tac_toe.board = [
      [X, O, X, X],
      [O, X, O, X],
      [X, O, X, O],
      [O, X, O, O]
    ]
    self.assertFalse(self.tic_tac_toe.any_moves_left())
    
    # test some moves left
    self.tic_tac_toe.board = [
      [X, O, X, BLANK],
      [O, X, O, X],
      [X, O, X, O],
      [O, X, O, BLANK]
    ]
    self.assertTrue(self.tic_tac_toe.any_moves_left())    
    
    
  def test_is_game_over(self):
    # test empty board
    self.assertFalse(self.tic_tac_toe.is_game_over())
    
    # test game over from win
    self.tic_tac_toe.board = [
      [X, O, X, O],
      [O, X, O, X],
      [X, O, X, O],
      [O, X, O, X]
    ]
    self.assertTrue(self.tic_tac_toe.is_game_over())
    
    # test game over from no moves left
    self.tic_tac_toe.board = [
      [O, O, X, X],
      [O, X, O, X],
      [X, O, X, O],
      [O, X, O, X]
    ]
    self.assertTrue(self.tic_tac_toe.is_game_over())