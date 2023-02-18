import pygame as pygm
import os

WIDTH, HEIGHT = 760,760
ROWS, COLS = 8,8
SQUARE = WIDTH//ROWS

BROWN = (87,16,16)
WHITE = (255,255,255)
GREEN = (0,255,0)

PATH = "ressource\chess_images"

# Black piece

BLACK_KNIGHT = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"bKN.png")),(SQUARE,SQUARE))
BLACK_BISHOP = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"bB.png")),(SQUARE,SQUARE))
BLACK_KING = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"bQ.png")),(SQUARE,SQUARE))
BLACK_PAWN = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"bP.png")),(SQUARE,SQUARE))
BLACK_QUEEN = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"bK.png")),(SQUARE,SQUARE))
BLACK_ROOK = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"bR.png")),(SQUARE,SQUARE))

# White piece

WHITE_KNIGHT = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"wKN.png")),(SQUARE,SQUARE))
WHITE_BISHOP = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"wB.png")),(SQUARE,SQUARE))
WHITE_KING = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"wQ.png")),(SQUARE,SQUARE))
WHITE_PAWN = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"wP.png")),(SQUARE,SQUARE))
WHITE_QUEEN = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"wK.png")),(SQUARE,SQUARE))
WHITE_ROOK = pygm.transform.scale(pygm.image.load(os.path.join(PATH,"wR.png")),(SQUARE,SQUARE))