import time

import pygame
from checkers.constants import width,height,squares_size,black,white
from checkers.board import Board
from checkers.game import Game
from minMax.algorithm import minmax

FPS=200
display=pygame.display.set_mode((width,height))
pygame.display.set_caption('AI_Chekers')


def get_from_mouse(position):
    x,y=position
    row=y//squares_size
    column=x//squares_size
    return row,column

if __name__ == '__main__':
    run=True
    timeRate=pygame.time.Clock()
    game_board=Board()
    game=Game(display)




    while run:
        timeRate.tick(FPS)
        if game.turn == white:
            time.sleep(1)
            value, new_situation = minmax(game.take_board(), 3, white, game)
            game.AI(new_situation)

        if game.winner() != None:
            print(game.winner())
            run=False
            #JAKIS ŁADNY DISPLAY



        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                #ending the game
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                row,column=get_from_mouse(position)
                # if game.turn==black:
                game.select(row,column)


        game.update()

    pygame.quit()

