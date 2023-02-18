import pygame as pygm
from .pieces import *
from .constants import * 

class newBoard:

    def __init__(self, width, height, rows, cols, square, win) -> None:
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.square = square
        self.win = win
        self.board = []
        self.create_board()

    def create_board(self):

        for row in range(self.rows): 
            self.board.append([0 for _ in range(self.cols)])

            for col in range(self.cols):
                if row == 1:
                    self.board[row][col] = Pawn(self.square,BLACK_PAWN,"black", "Pawn",row,col)
                elif row == 6:
                    self.board[row][col] = Pawn(self.square,WHITE_PAWN,"white", "Pawn",row,col)
                elif row == 0:
                    if col == 0 or col == 7:
                        self.board[row][col] = Rook(self.square,BLACK_ROOK,"black", "Rook",row,col)
                    elif col == 1 or col == 6:
                        self.board[row][col] = Knight(self.square,BLACK_KNIGHT,"black", "Knight",row,col)
                    elif col == 2 or col == 5:
                        self.board[row][col] = Bishop(self.square,BLACK_BISHOP,"black", "Bishop",row,col)
                    elif col == 3:
                        self.board[row][col] = Queen(self.square,BLACK_QUEEN,"black", "Queen",row,col)
                    elif col == 4:
                        self.board[row][col] = King(self.square,BLACK_KING,"black", "King",row,col)
                elif row == 7:
                    if col == 0 or col == 7:
                        self.board[row][col] = Rook(self.square,WHITE_ROOK,"white", "Rook",row,col)
                    elif col == 1 or col == 6:
                        self.board[row][col] = Knight(self.square,WHITE_KNIGHT,"white", "Knight",row,col)
                    elif col == 2 or col == 5:
                        self.board[row][col] = Bishop(self.square,WHITE_BISHOP,"white", "Bishop",row,col)
                    elif col == 3:
                        self.board[row][col] = Queen(self.square,WHITE_QUEEN,"white", "Queen",row,col)
                    elif col == 4:
                        self.board[row][col] = King(self.square,WHITE_KING,"white", "King",row,col)

    def get_piece(self,row,col):
        return self.board[row][col]

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]      

        piece.piece_move(row,col)

        if piece.type == "Pawn":
            if piece.first_move:
                piece.first_move = False
    
    def draw_board(self):
        self.win.fill(BROWN)

        for row in range(self.rows):
            for col in range(row%2,self.cols,2):
                pygm.draw.rect(self.win,WHITE, (SQUARE*row,SQUARE*col,SQUARE,SQUARE))


    def draw_piece(self, piece, win):

        win.blit(piece.image,(piece.x,piece.y))
    
    def draw_all_pieces(self):

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != 0:
                    self.draw_piece(self.board[row][col],self.win)
        