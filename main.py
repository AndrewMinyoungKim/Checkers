
import pygame

#you can import this because of the __init__.py file inside the checkers folder
#it tells us that checkers folder is a python package so you can import specific things from
from checkers.constants import SQUARE_SIZE, WIDTH, HEIGHT, RED, WHITE

#from checkers.board import Board
from checkers.game import Game



FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos  #tuple
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            if(game.winner() == WHITE):
                print("Winner!: WHITE")
            else:
                print("Winner!: RED")
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        
        game.update()

    pygame.quit()

if __name__ == "__main__":
    main()