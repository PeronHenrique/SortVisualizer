import pygame
import string
from typing import List
from config import Config



class Drawer:
	window: pygame.Surface

	def __init__(self, window: pygame.Surface) -> None:
		self.window = window
		

	def drawWindow(self, algo_name: string, ascending: bool) -> None:
		self.window.fill(Config.BACKGROUND_COLOR)

		algoritmText = Config.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, Config.GREEN)
		self.window.blit(algoritmText, (Config.WINDOW_WIDTH/2 - algoritmText.get_width()/2 , 5))

		controlsText = Config.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, Config.BLACK)
		self.window.blit(controlsText, (Config.WINDOW_WIDTH/2 - controlsText.get_width()/2 , 45))

		sorting = Config.FONT.render("Rigth/Left Arrow to change sorter", 1, Config.BLACK)
		self.window.blit(sorting, (Config.WINDOW_WIDTH/2- sorting.get_width()/2 , 75))


	def drawListColumns(self, lst: List[int], color_positions = {}) -> None:

		clear_rect = (
			Config.SIDE_PAD // 2,
			Config.TOP_PAD, 
			Config.WINDOW_WIDTH - Config.SIDE_PAD,
			Config.WINDOW_HEIGHT - Config.TOP_PAD)
		
		pygame.draw.rect(self.window, Config.BACKGROUND_COLOR, clear_rect)

		for i, val in enumerate(lst):
			x = Config.START_X + i * Config.BLOCK_WIDTH
			y = Config.WINDOW_HEIGHT - (val - Config.COLUNM_VAL_ZERO) * Config.BLOCK_UNIT_HEIGHT

			color = Config.GRADIENTS[i % 3]

			if i in color_positions:
				color = color_positions[i] 

			pygame.draw.rect(self.window, color, (x, y, Config.BLOCK_WIDTH, Config.WINDOW_HEIGHT))

		pygame.display.update()
