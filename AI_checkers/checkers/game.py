import pygame
from checkers.board import Board
from .constants import white,black,red,squares_size

class Game:
    def __init__(self,display):
        self._init()
        self.display=display

    def update(self):
        self.board.draw(self.display)
        self.draw_possible_moves(self.valid_movement)
        pygame.display.update()


    def _init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = white
        self.valid_movement = {}

    def reset(self):
       self._init()

    def select(self,row,column):
        if(self.selected_piece):
            result=self._move(row,column)
            if not result:
                self.selected_piece=None
                self.select(row,column)

        piece = self.board.get_piece(row, column)
        if piece!=0 and piece.color ==self.turn:
            self.selected_piece=piece
            self.valid_movement=self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self,row,column):
        piece=self.board.get_piece(row,column)
        #making sure that we chose a valid movement
        if self.selected_piece and piece==0 and (row,column) in self.valid_movement:
           self.board.move(self.selected_piece,row,column)
           skipped=self.valid_movement[(row,column)]
           if skipped:
               self.board.remove(skipped)
           self.change_turns()

        else:
            return False
        return True

    def winner(self):
        return self.board.winner()

    def change_turns(self):
        self.valid_movement = {}
        if self.turn==white:
            self.turn=black
        else:
            self.turn=white

    def draw_possible_moves(self,moves):
        for move in moves:
            row,column=move
            pygame.draw.circle(self.display,red,(column*squares_size+squares_size//2,row*squares_size+squares_size//2),10)
