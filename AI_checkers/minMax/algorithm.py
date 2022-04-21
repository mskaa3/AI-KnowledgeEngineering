import math
from copy import deepcopy
import pygame

from checkers import board
from checkers.constants import black, white

def minmaxAlfaBeta(position,n,maximize,game,startingColor,alpha,beta):

    if position.winner() != None or n==0:
        return position.evaluate(), position
    #if we maximize
    if maximize:
        if startingColor is white:
            startingColor = black
        else:
            startingColor = white

        maximumValue=-math.inf
        best=None
        # if len(possible_moves(position, startingColor, game)) == 0:
        #     return maximumValue, None

        for m in possible_moves(position,startingColor,game):
            #recursively going up to the root, with false, so it will minimize stuff
            evaluate=minmaxAlfaBeta(m,n-1,False,game,startingColor,alpha,beta)[0]
            maximumValue = max(maximumValue,evaluate)
            alpha=max(alpha,evaluate)

            if maximumValue==evaluate:
                #if current move has the bigeest maximum value , than save a move
                best=m
            if beta<=alpha:
                break

        return maximumValue,best
    else:
        if startingColor is white:
            startingColor=black
        else:
            startingColor=white

        minimumValue = math.inf
        best = None

        # if len(possible_moves(position, startingColor, game)) == 0:
        #     return minimumValue, None
        for m in possible_moves(position, black, game):
            # recursively going up to the root
            evaluate = minmaxAlfaBeta(m, n - 1, True, game,startingColor,alpha,beta)[0]
            minimumValue = min(minimumValue, evaluate)
            beta=min(beta,evaluate)

            if evaluate == minimumValue:
                # if current move has the bigeest maximum value , than save a move
                best = m
            if beta <= alpha:
                break

        return minimumValue, best

def minmaxDifferentEvaluationAlfaBeta(position,n,maximize,game,startingColor,alpha,beta):
    if position.winner() != None or n==0:
        return position.evaluateDifferently(), position
    #if we maximize
    if maximize:
        if startingColor is white:
            startingColor = black
        else:
            startingColor = white

        maximumValue=float('-inf')
        best=None
        #CO JEST Z TYMI KOLORAMI, moze trzeba je rekursywnie podac zeby były przeciwko sobie
        if len(possible_moves(position,startingColor,game)) ==0:
            return maximumValue,None


        for m in possible_moves(position,startingColor,game):
            #recursively going up to the root, with false, so it will minimize stuff
            evaluate=minmaxAlfaBeta(m,n-1,False,game,startingColor,alpha,beta)[0]
            maximumValue = max(maximumValue,evaluate)
            beta = min(beta, evaluate)
            if maximumValue==evaluate:
                #if current move has the bigeest maximum value , than save a move
                best=m
            if beta<=alpha:
                break

        return maximumValue,best
    else:
        if startingColor is white:
            startingColor=black
        else:
            startingColor=white

        minimumValue = float('inf')
        best = None

        if len(possible_moves(position, startingColor, game)) == 0:
            return minimumValue, None
        for m in possible_moves(position, black, game):
            # recursively going up to the root
            evaluate = minmaxAlfaBeta(m, n - 1, True, game,startingColor)[0]
            minimumValue = min(minimumValue, evaluate)
            if evaluate == minimumValue:
                # if current move has the bigeest maximum value , than save a move
                best = m
            if beta<=alpha:
                break

        return minimumValue, best


def minmax(position,n,maximize,game,startingColor):

    if position.winner() != None or n==0:
        return position.evaluate(), position
    #if we maximize
    if maximize:
        if startingColor is white:
            startingColor = black
        else:
            startingColor = white

        maximumValue=-math.inf
        best=None
        # if len(possible_moves(position, startingColor, game)) == 0:
        #     return maximumValue, None

        for m in possible_moves(position,startingColor,game):
            #recursively going up to the root, with false, so it will minimize stuff
            evaluate=minmax(m,n-1,False,game,startingColor)[0]
            maximumValue = max(maximumValue,evaluate)

            if maximumValue==evaluate:
                #if current move has the bigeest maximum value , than save a move
                best=m


        return maximumValue,best
    else:
        if startingColor is white:
            startingColor=black
        else:
            startingColor=white

        minimumValue = math.inf
        best = None

        # if len(possible_moves(position, startingColor, game)) == 0:
        #     return minimumValue, None
        for m in possible_moves(position, black, game):
            # recursively going up to the root
            evaluate = minmax(m, n - 1, True, game,startingColor)[0]
            minimumValue = min(minimumValue, evaluate)

            if evaluate == minimumValue:
                # if current move has the bigeest maximum value , than save a move
                best = m


        return minimumValue, best

def minmaxDifferentEvaluation(position,n,maximize,game,startingColor):
    if position.winner() != None or n==0:
        return position.evaluateDifferently(), position
    #if we maximize
    if maximize:
        if startingColor is white:
            startingColor = black
        else:
            startingColor = white

        maximumValue=float('-inf')
        best=None
        #CO JEST Z TYMI KOLORAMI, moze trzeba je rekursywnie podac zeby były przeciwko sobie
        if len(possible_moves(position,startingColor,game)) ==0:
            return maximumValue,None


        for m in possible_moves(position,startingColor,game):
            #recursively going up to the root, with false, so it will minimize stuff
            evaluate=minmax(m,n-1,False,game,startingColor)[0]
            maximumValue = max(maximumValue,evaluate)

            if maximumValue==evaluate:
                #if current move has the bigeest maximum value , than save a move
                best=m


        return maximumValue,best
    else:
        if startingColor is white:
            startingColor=black
        else:
            startingColor=white

        minimumValue = float('inf')
        best = None

        if len(possible_moves(position, startingColor, game)) == 0:
            return minimumValue, None
        for m in possible_moves(position, black, game):
            # recursively going up to the root
            evaluate = minmax(m, n - 1, True, game,startingColor)[0]
            minimumValue = min(minimumValue, evaluate)
            if evaluate == minimumValue:
                # if current move has the bigeest maximum value , than save a move
                best = m


        return minimumValue, best


def possible_moves(board,color,game):
    moves=[]
    for piece in board.get_all(color):
        valid=board.get_valid_moves(piece)
        #jumping over pieces
        for move, skip in valid.items():
            #deepcopy makes an exact copy of the board, it doesnt change when we change the reference
            temporary=deepcopy(board)
            temp_piece=temporary.get_piece(piece.row,piece.column)
            new_board=simulate(temp_piece,move,temporary,game,skip)
            moves.append(new_board)


    return moves


def simulate(piece,move,board,game,skip):
    #move[0] is row, move[1] is column
    board.move(piece,move[0],move[1])
    if skip:
        board.remove(skip)

    return board


