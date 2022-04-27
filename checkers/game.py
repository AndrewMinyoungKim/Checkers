import pygame
from .constants import RED, SQUARE_SIZE, WHITE, BLUE
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win #store the window in here so we don't need to pass it every time

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        #have to call this function to update the display
        pygame.display.update()

    def _init(self): #putting an underscore beside it makes this function private and that you must call reset() to call _init()
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    # the name reset() is much easier to understand for the user than the name _init() even though it's the same,
    # so it provides clarity to the user, since __init__() also uses it, they both run _init()
    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False
    
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            
        else:
            return False
        
        return True

    def draw_valid_moves(self, moves):
        for move in moves: #moves is a dictionary, each key in the dictionary is a tuple
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {} #removes valid moves (blue circles) after player has moved a checker piece and finished their turn
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED