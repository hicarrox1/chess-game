import pygame as pygm

from ressource.constants import *
from ressource.board import *
from ressource.game import *

pygm.init()

clock = pygm.time.Clock()

win = pygm.display.set_mode((WIDTH,HEIGHT))

def get_position(x,y):
    row = y//SQUARE
    col = x//SQUARE
    
    return row,col

def main():
    run = True
    FPS = 60
    game_over = False

    game = Game(WIDTH,HEIGHT,ROWS,COLS,SQUARE,win)

    while run:
        clock.tick(FPS)

        game.update_window()

        if game.check_game():
            game_over = True
        
        for event in pygm.event.get():
            
            if event.type == pygm.QUIT:
                run = False
                quit()
            if event.type == pygm.KEYDOWN:
                if event.type == pygm.K_ESCAPE and game_over:
                    game.reset()
            if event.type == pygm.MOUSEBUTTONDOWN and not game_over:
                if pygm.mouse.get_pressed()[0]:
                    location = pygm.mouse.get_pos()   
                    row,col = get_position(location[0],location[1])  
                    print(row,col)
                    game.select(row,col)


main()