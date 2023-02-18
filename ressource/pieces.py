import pygame as pygm
from .constants import *

class Piece:
    
    def __init__(self, square, image, color, type, row, col) -> None:
        self.square = square
        self.image = image
        self.color = color
        self.type = type
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.avaibles_moves = []
        self.calc_pos()

    def piece_move(self,row,col):
        self.row = row
        self.col = col
        self.calc_pos()
    
    def calc_pos(self):
        self.x = self.col * self.square
        self.y = self.row * self.square
    
    def clear_available_moves(self):
        if len(self.avaibles_moves) >= 1:
            self.avaibles_moves = []


class Pawn(Piece):

    def __init__(self, square, image, color, type, row, col) -> None:
        super().__init__(square, image, color, type, row, col)
        self.first_move = True
    
    def get_available_moves(self, row, col, board):
        self.clear_available_moves()

        if self.color == "white":
            if row-1 >=0:
                if board[row-1][col] == 0:
                    self.avaibles_moves.append((row-1,col))
                    if self.first_move:
                        if board[row-2][col] == 0:
                            self.avaibles_moves.append((row-2,col))
                if col -1 >= 0:
                    if board[row-1][col-1] != 0:
                        piece = board[row-1][col-1]
                        if piece.color != "white":
                            self.avaibles_moves.append((row-1,col-1))
                if col +1 < len(board[0]):
                    if board[row-1][col+1] != 0:
                        piece = board[row-1][col+1]
                        if piece.color != "white":
                            self.avaibles_moves.append((row-1,col+1))
                
        if self.color == "black":
            if row + 1 < len(board):
                if board[row+1][col] == 0:
                    self.avaibles_moves.append((row+1,col))

                    if self.first_move:
                        if board[row+2][col] == 0:
                            self.avaibles_moves.append((row+2,col))
                
                if col -1 >= 0:
                    if board[row+1][col-1] != 0:
                        piece = board[row+1][col-1]
                        if piece.color != "black":
                            self.avaibles_moves.append((row+1,col-1))
                if col +1 < len(board[0]):
                    if board[row+1][col+1] != 0:
                        piece = board[row+1][col+1]
                        if piece.color != "black":
                            self.avaibles_moves.append((row+1,col+1))
                
        return self.avaibles_moves

class Rook(Piece):
    
    def __init__(self, square, image, color, type, row, col) -> None:
        super().__init__(square, image, color, type, row, col)

    def get_available_moves(self, row, col, board):
        self.clear_available_moves()

        def test_rook(debut:int, arriver:int, pas:int = 1, vertical: bool = False):

            if vertical:
                for i in range(debut,arriver,pas):

                    if board[i][col] == 0:
                        self.avaibles_moves.append((i,col))
                    elif board[i][col].color != self.color:
                        self.avaibles_moves.append((i,col))
                        break
                    else:
                        break
            else:
                
                for j in range(debut,arriver,pas):

                    if board[row][j] == 0:
                        self.avaibles_moves.append((row,j))
                    elif board[row][j].color != self.color:
                        self.avaibles_moves.append((row,j))
                        break
                    else:
                        break
        
        test_rook(row+1,len(board[0]),vertical = True)
        test_rook(row-1,-1,pas=-1,vertical = True)
        test_rook(col+1,len(board[0]))
        test_rook(col-1,-1,pas=-1)
        
        return self.avaibles_moves

class Bishop(Piece):

    def __init__(self, square, image, color, type, row, col) -> None:
        super().__init__(square, image, color, type, row, col)
    
    def get_available_moves(self, row, col, board):
        self.clear_available_moves()

        def test_bishop(pas_row:int,pas_col:int):

            row_i = row + pas_row
            col_i = col + pas_col

            if pas_col > 0:
                def verif1(): return col_i < len(board[0])
            else:
                def verif1(): return col_i >= 0
            
            if pas_row > 0:
                def verif2(): return row_i < len(board)
            else:
                def verif2(): return row_i >= 0

            while verif1() and verif2():
                if board[row_i][col_i] == 0:
                    self.avaibles_moves.append((row_i,col_i))
                    row_i += pas_row
                    col_i += pas_col
                elif board[row_i][col_i].color != self.color:
                    self.avaibles_moves.append((row_i,col_i))
                    break
                else:
                    break

        test_bishop(1,1)
        test_bishop(-1,-1)
        test_bishop(1,-1)
        test_bishop(-1,1)

        return self.avaibles_moves

class Knight(Piece):

    def __init__(self, square, image, color, type, row, col) -> None:
        super().__init__(square, image, color, type, row, col)
    
    def get_available_moves(self, row, col, board):
        self.clear_available_moves()

        def test_knight(pas_row,pas_col):

            if pas_col > 0:
                def verif1(): return col+pas_col < len(board[0])
            else:
                def verif1(): return col+pas_col >= 0
            
            if pas_row > 0:
                def verif2(): return row+pas_row < len(board)
            else:
                def verif2(): return row+pas_row >= 0

            if verif1() and verif2():
                if board[row+pas_row][col+pas_col] == 0 or board[row+pas_row][col+pas_col].color != self.color:
                    self.avaibles_moves.append((row+pas_row,col+pas_col))

        test_knight(-2,1)
        test_knight(-2,-1)
        test_knight(2,1)
        test_knight(2,-1)
        test_knight(1,2)
        test_knight(-1,2)
        test_knight(1,-2)
        test_knight(-1,-2)

        return self.avaibles_moves

class Queen(Piece):

    def __init__(self, square, image, color, type, row, col) -> None:
        super().__init__(square, image, color, type, row, col)
    
    def get_available_moves(self, row, col, board):
        self.clear_available_moves()

        def test_rook(debut:int, arriver:int, pas:int = 1, vertical: bool = False):

            if vertical:
                for i in range(debut,arriver,pas):

                    if board[i][col] == 0:
                        self.avaibles_moves.append((i,col))
                    elif board[i][col].color != self.color:
                        self.avaibles_moves.append((i,col))
                        break
                    else:
                        break
            else:
                for j in range(debut,arriver,pas):

                    if board[row][j] == 0:
                        self.avaibles_moves.append((row,j))
                    elif board[row][j].color != self.color:
                        self.avaibles_moves.append((row,j))
                        break
                    else:
                        break

        def test_bishop(pas_row:int,pas_col:int):

                row_i = row + pas_row
                col_i = col + pas_col

                if pas_col > 0:
                    def verif1(): return col_i < len(board[0])
                else:
                    def verif1(): return col_i >= 0
                
                if pas_row > 0:
                    def verif2(): return row_i < len(board)
                else:
                    def verif2(): return row_i >= 0

                while verif1() and verif2():
                    if board[row_i][col_i] == 0:
                        self.avaibles_moves.append((row_i,col_i))
                        row_i += pas_row
                        col_i += pas_col
                    elif board[row_i][col_i].color != self.color:
                        self.avaibles_moves.append((row_i,col_i))
                        break
                    else:
                        break

        test_rook(row+1,len(board[0]),vertical = True)
        test_rook(row-1,-1,pas=-1,vertical = True)
        test_rook(col+1,len(board[0]))
        test_rook(col-1,-1,pas=-1)
        test_bishop(1,1)
        test_bishop(-1,-1)
        test_bishop(1,-1)
        test_bishop(-1,1)

        return self.avaibles_moves
    
class King(Piece):

    def __init__(self, square, image, color, type, row, col) -> None:
        super().__init__(square, image, color, type, row, col)
    
    def get_available_moves(self, row, col, board):
        """prend tous les coups disponible pour le roi"""
        self.clear_available_moves()
    
        def test_king(pas_row:int, pas_col:int):
            """teste si la case ou le roi peut aller et occuper par un enemi ou libre"""

            # ajuste les verification en fonction du pas
            if pas_col > 0:
                def verif1(): return col+pas_col < len(board[0])
            else:
                def verif1(): return col+pas_col >= 0
            
            if pas_row > 0:
                def verif2(): return row+pas_row < len(board)
            else:
                def verif2(): return row+pas_row >= 0

            if verif1() and verif2():
                if board[row+pas_row][col+pas_col] == 0 or board[row+pas_row][col+pas_col].color != self.color:
                    self.avaibles_moves.append((row+pas_row,col+pas_col))
        
        # les coter du roi
        test_king(1,0)
        test_king(-1,0)
        test_king(0,1)
        test_king(0,-1)
        # les diagonal du roi
        test_king(1,1)
        test_king(-1,1)
        test_king(-1,-1)
        test_king(1,-1)

        return self.avaibles_moves
    