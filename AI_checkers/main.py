import math
import time

import pygame
from checkers.constants import width,height,squares_size,black,white
from checkers.board import Board
from checkers.game import Game
from minMax.algorithm import minmax, minmaxDifferentEvaluation, minmaxDifferentEvaluationAlfaBeta, minmaxAlfaBeta

FPS=300
display=pygame.display.set_mode((width,height))
pygame.display.set_caption('AI_Chekers')
AIsingleTurns=0
AIwhiteturns=0
AIblackturns=0
movement=0
playAgainstAI=False
BdecisionTime=0
WdecisionTime=0

def get_from_mouse(position):
    x,y=position
    row=y//squares_size
    column=x//squares_size
    return row,column


# Board implementation and movement generator taken and modified from : https://www.youtube.com/watch?v=vnd3RfeG3NM
if __name__ == '__main__':
    run=True
    timeRate=pygame.time.Clock()
    game_board=Board()
    game=Game(display)
    time.sleep(3)




    while run:
        timeRate.tick(FPS)
        movement+=1

        try:
            if game.winner() != None:
                print(game.winner())
                if game.winner() is "White":
                    print(f"Whites won in {AIwhiteturns} turns")
                else:
                    print(f"Blacks won in {AIblackturns} turns")
                run=False

            if (game.turn == white and movement%2==0) or (playAgainstAI and game.turn == white):
                start=time.time_ns()
                value, new_situation = minmaxAlfaBeta(game.take_board(), 3, white, game,black,-math.inf,math.inf)
                # value, new_situation = minmax(game.take_board(), 3, white, game, black)
                game.AI(new_situation)
                finish=time.time_ns()
                WdecisionTime=WdecisionTime+(finish-start)
                AIwhiteturns+=1
                print("Cureent average time of movement for whites")
                print(WdecisionTime / AIwhiteturns)
                #AIsingleTurns+=1


            timeRate.tick(FPS)

            if game.turn==black and movement%2==1 and playAgainstAI is False:
                start = time.time_ns()
                value, new_situation = minmaxDifferentEvaluationAlfaBeta(game.take_board(), 3, black, game,white,-math.inf,math.inf)
                # value, new_situation = minmaxDifferentEvaluation(game.take_board(), 3, black, game, white)
                game.AI(new_situation)
                finish=time.time_ns()
                BdecisionTime=BdecisionTime+(finish-start)
                AIblackturns+=1
                print("Cureent average time of movement for blacks")
                print(BdecisionTime / AIblackturns)

        except AttributeError:
            if game.turn==black:
                print("No possible movements for whites")
                print(f"Blacks won in {AIblackturns} turns")
            else:
                print("No possible movements for black")
                print(f"Whites won in {AIwhiteturns} turns")




        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                  #ending the game
                 run=False
            if playAgainstAI:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    position=pygame.mouse.get_pos()
                    row,column=get_from_mouse(position)
                    # if game.turn==black:
                    game.select(row,column)


        timeRate.tick(FPS)
        if game.board is None:
            col=""
            if game.turn==white:
                col="black"
            else:
                col="white"
            print(f"No possible movements,{col} lost")
            run=False
        else:
            game.update()



    pygame.quit()

