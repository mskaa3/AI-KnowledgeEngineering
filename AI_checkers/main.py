import pygame
from checkers.constants import width,height
from checkers.board import Board

FPS=60
display=pygame.display.set_mode((width,height))
pygame.display.set_caption('AI_Chekers')

if __name__ == '__main__':
    run=True
    timeRate=pygame.time.Clock()
    game_board=Board()


    while run:
        timeRate.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                #ending the game
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                pass
        game_board.draw(display)
        pygame.display.update()

    pygame.quit()

