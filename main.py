import pygame
import sys
from ship import Ship

from settings import Settings

class AlienWorld:

	def __init__(self):
		pygame.init()
		self.my_settings = Settings()

		self.error = False
		self.screen = pygame.display.set_mode([self.my_settings.window_width, self.my_settings.window_height])
		self.title = pygame.display.set_caption("Game Alien")
		self.bg_color = self.my_settings.bg_color

		self.my_ship = Ship(self)

	def run_game(self):
		while not self.error:
			self.check_event()
			self.screen.fill(self.bg_color)
			self.my_ship.blit_ship()

			pygame.display.flip()

	def check_event(self):
		for event in pygame.event.get():
				if event.type ==pygame.QUIT:
					#sys.exit()
					self.error = True

Game_Alien = AlienWorld()
Game_Alien.run_game()