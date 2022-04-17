import pygame.draw
import pygame
from .constants import black,white,squares_size,red,crown

class Piece:
    padding=15
    outline=2


    def __init__(self,row,column,color):
        self.row=row
        self.column=column
        self.color=color
        self.king=False
        if self.color==black:
            #blacks are going up
             self.direction=-1
        else:
            #whites are going down
            self.direction=1
        self.x=0
        self.y=0
        self.piece_position()

    def piece_position(self):
        #recalculating position
        self.x=squares_size*self.column+squares_size//2
        self.y=squares_size*self.row+squares_size//2

    def change_to_king(self):
        self.king=True

    def draw(self,display):
        radius=squares_size//2-self.padding
        pygame.draw.circle(display, (105,105,105), (self.x, self.y), radius + self.outline)
        pygame.draw.circle(display,self.color,(self.x,self.y),radius)
        if self.king:
            display.blit(crown,(self.x-crown.get_width()//2,self.y-crown.get_height()//2))

    def move(self,row,column):
        self.row=row
        self.column=column
        self.piece_position()

    def __repr__(self):
        return  str(self.color)