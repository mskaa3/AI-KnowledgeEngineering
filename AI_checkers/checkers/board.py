import pygame
from .constants import grey, white, rows, squares_size, columns, black,whitegrey
from .piece import Piece


class Board:
    def __init__(self):
        # two dimnension list storage
        self.board = []
        self.white_onboard = self.black_onboard = 20
        self.white_kings = self.black_kings = 0
        self.create_board()


    def draw_tiles(self, display):
        display.fill(grey)
        for row in range(rows):
            for column in range(row % 2, rows, 2):
                pygame.draw.rect(display, whitegrey,
                                 (row * squares_size, column * squares_size, squares_size, squares_size))

    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for column in range(columns):
                # thats for drawing the pieces on the board ina  proper order according to the row they're in
                if column % 2 == ((row + 1) % 2):
                    if row < 4:
                        self.board[row].append(Piece(row, column, white))
                    elif row > 5:
                        self.board[row].append(Piece(row, column, black))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, display):
        self.draw_tiles(display)
        for row in range(rows):
            for column in range(columns):
                piece = self.board[row][column]
                if piece != 0:
                    piece.draw(display)

    def move(self,piece,row,column):
        #swapping values
        self.board[piece.row][piece.column],self.board[row][column]=self.board[row][column],self.board[piece.row][piece.column]
        piece.move(row,column)
        if row==rows or row==0:
            piece.change_to_king()
            if piece.color==white:
                self.white_kings+=1
            else:
                self.black_kings+=1

    def get_piece(self,row,column):
        return self.board[row][column]