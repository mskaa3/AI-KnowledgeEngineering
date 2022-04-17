import pygame
from checkers.constants import width,height,squares_size
from checkers.board import Board

FPS=60
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


    while run:
        timeRate.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                #ending the game
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                row,column=get_from_mouse(position)
                piece=game_board.get_piece(row,column)
                game_board.move(piece,4,3)
                
        game_board.draw(display)
        pygame.display.update()

    pygame.quit()

