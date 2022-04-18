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

    def remove(self,pieces):
        for piece in pieces:
            self.board[piece.row][piece.column]=0



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

    def get_valid_moves(self,piece):
        moves={}
        left=piece.column-1
        right=piece.column+1
        row=piece.row
        if piece.color==black or piece.king:
            #row-1 because as black we go up, so to the previous row
            #max is how far do we look up to, up to two tiles away
            moves.update(self._go_left_diagonal(row-1,max(row-3,-1),-1,piece.color,left))
            moves.update(self._go_right_diagonal(row - 1, max(row - 3, -1),-1, piece.color, right))
        if piece.color==white or piece.king:
            moves.update(self._go_left_diagonal(row + 1, min(row + 3, rows),1, piece.color, left))
            moves.update(self._go_right_diagonal(row + 1, min(row + 3, rows),1, piece.color, right))

        return moves

    def _go_left_diagonal(self,start,stop,step,color,left,skipped=[]):
        moves={}
        last=[]
        for r in  range(start, stop, step):
            if left<0:
                break
            curr=self.board[r][left]
            if curr == 0:
                if skipped and not last:
                    #if we skipped and we didnt find anything to skip over again
                    break
                elif skipped:
                    moves[(r,left)]=last+skipped
                else:
                    moves[(r,left)]=last
                if last:
                    if step==1:
                        row=max(r-3,0)
                    else:
                        row=min(r+3,rows)
                    moves.update(self._go_left_diagonal(r+step,row,step,color,left-1,skipped=last))
                    moves.update(self._go_left_diagonal(r + step, row, step, color, left +1, skipped=last))
                break

            elif curr.color==color:
                break
            else:
                last=[curr]

            left -=1
        return moves

    def _go_right_diagonal(self,start,stop,step,color,right,skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= columns:
                break
            curr = self.board[r][right]
            if curr == 0:
                if skipped and not last:
                    # if we skipped and we didnt find anything to skip over again
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    if step == 1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, rows)
                    moves.update(self._go_left_diagonal(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._go_left_diagonal(r + step, row, step, color, right + 1, skipped=last))
                break

            elif curr.color == color:
                break
            else:
                last = [curr]

            right += 1
        return moves