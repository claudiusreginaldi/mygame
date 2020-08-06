import sys # untuk akses ke sistem operasi secara universal

import pygame # library pygame untuk membangun game

class AlienCounter:

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode([800,600])
		self.title = pygame.display.set_caption("Alien Counter Game")

	def run_game(self):
	
		while True: #infinite loop

			#memonitor kejadian / event
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			#rendering display every frame
			pygame.display.flip()

my_game = AlienCounter()
my_game.run_game()

