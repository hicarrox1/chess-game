import pygame as pygm
from .board import newBoard
from .constants import *
from copy import deepcopy

class Game:

    def __init__(self, width, height, rows, cols, square, win) -> None:
        
        self.width, self.height, self.rows, self.cols, self.square  = width, height, rows, cols, square
        self.win = win
        self.board = newBoard(width,height,rows,cols,square,win)
        self.square = square
        self.selected = None
        self.turn = "white"
        self.valid_moves = []
        self.black_pieces_left = 16
        self.white_pieces_left = 16
    
    def update_window(self):
        self.board.draw_board()
        self.board.draw_all_pieces()
        self.draw_available_moves()
        pygm.display.update()
    
    def check_game(self):
        if self.checkmate(self.board):
            if self.turn == "white":
                print("black win")
            else:
                print("white win")
            return True
        return False

    def color_moves(self,board,color):
        moves_liste = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != 0:
                    if board[r][c].color == color and board[r][c].type != "King":
                        moves = board[r][c].get_available_moves(r, c, board)
                        for move in moves:
                            moves_liste.append(move)
        return moves_liste
    
    def get_king_pos(self,board):
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != 0:
                    if board[r][c].type == "King" and board[r][c].color == self.turn:
                        return (r,c)

    def inverse_color(self,color):
        if color == "white":
            return "black"
        else:
            return "white"

    def simulate_move(self, piece, row, col):
        piece_row, piece_col = piece.row, piece.col
        save_piece = self.board.board[row][col]

        if self.board.board[row][col] != 0:
            self.board.board[row][col] = 0

        self.board.board[piece_row][piece_col], self.board.board[row][col] = self.board.board[row][col], self.board.board[piece_row][piece_col]

        if self.get_king_pos(self.board.board) in self.color_moves(self.board.board, self.inverse_color(self.turn)):
            piece.row, piece.col = piece_row, piece_col
            self.board.board[piece_row][piece_col] = piece
            self.board.board[row][col] = save_piece
            return False
        piece.row, piece.col = piece_row, piece_col
        self.board.board[piece_row][piece_col] = piece
        self.board.board[row][col] = save_piece
        return True
    
    def checkmate(self, board):
        king_pos = self.get_king_pos(board.board)
        get_king = board.get_piece(king_pos[0],king_pos[1])

        king_available_moves = set(get_king.get_available_moves(king_pos[0],king_pos[1],board.board))
        enemies_move_set = set(self.color_moves(board.board, self.inverse_color(self.turn)))
        king_moves = king_available_moves - enemies_move_set
        set1 = king_available_moves.intersection(enemies_move_set)
        possible_move_to_def = set1.intersection(self.color_moves(board.board, self.turn))

        if len(king_moves) == 0 and len(king_available_moves) != 0 and possible_move_to_def ==0:
            return True

        return False

    def reset(self):
        self.board = newBoard(self.width,self.height,self.rows,self.cols,self.square,self.win)
        self.selected = None
        self.turn = "white"
        self.black_pieces_left, self.white_pieces_left = 16,16
        self.valid_moves = []
    
    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        elif self.turn == "black":
            self.turn = "white"
    
    def select(self, row, col):

        if self.selected:
            move = self._move(row,col)

            if not move:
                self.selected = None
                self.select(row,col)
        else:        
            piece = self.board.get_piece(row,col)
            if piece != 0:
                if self.turn == piece.color:
                    self.selected = piece

                    self.valid_moves = piece.get_available_moves(row,col, self.board.board)
                    print(piece, self.valid_moves)
    
    def _move(self,row, col):
        piece = self.board.get_piece(row,col)

        if self.selected and (row,col) in self.valid_moves:
            if piece == 0 or piece.color != self.selected.color:
                if self.simulate_move(self.selected, row, col):
                    self.remove(self.selected, row, col)

                    self.board.move(self.selected, row, col)
                    self.change_turn()
                    self.valid_moves = []
                    self.selected = None
                    return True
                return True
        return False
    
    def remove(self, piece, row, col):
        if piece !=0:
            self.board.board[row][col] = 0
            if piece.color == "white":
                self.white_pieces_left -= 1
            else:
                self.black_pieces_left -= 1

    def draw_available_moves(self):
        if len(self.valid_moves) > 0:
            for row,col in self.valid_moves:
                pygm.draw.circle(self.win,GREEN, (col*self.square+self.square//2,row*self.square+self.square//2),self.square//8)