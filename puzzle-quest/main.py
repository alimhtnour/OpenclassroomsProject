import pygame         # importation de module dans le programme
from costant import *
from game import *
from Pieces import *
from board import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((L_screen, l_screen))
Win = pygame.Surface((Width, Height))
arriere_plan = image1

def get_position(x,y):
	row = y//Square
	col = x//Square

	return row, col

def main():
	run = True
	FPS = 60
	game = Game(Width, Height, Rows, Cols, Square, Win)
	while run:
		clock.tick(FPS)



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quit()

		screen.blit(arriere_plan, (0, 0))
		screen.blit(Win, (200, 0))

		game.update_window()

		pygame.display.flip()
		#screen.fill((0, 0, 0))
		#Win.fill((255, 255, 225))

main()
