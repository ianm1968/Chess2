"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board):
        current_square = board.find_piece(self)

        if self.player == Player.WHITE:
            start_row = 1
            direction = 1
            max_row = 7
        else:
            start_row = 6
            direction = -1
            max_row = 0

        next_square = Square(current_square.row+direction, current_square.col)
        next_next_square = Square(current_square.row+(direction*2), current_square.col)
        next_square_left = Square(current_square.row+direction, current_square.col-direction)
        next_square_right = Square(current_square.row+direction, current_square.col+direction)
            
        if current_square.row == max_row or board.get_piece(next_square) != None:
            return []
        else:
            if current_square.row == start_row and board.get_piece(next_next_square) == None:
                return [next_square, next_next_square]
            else:
                return [next_square]



class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []