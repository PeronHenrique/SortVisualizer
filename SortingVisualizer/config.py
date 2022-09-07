import pygame

class Config:
    WINDOW_WIDTH = 1100
    WINDOW_HEIGHT = 600
    SIDE_PAD = 100
    TOP_PAD = 110
    
    LIST_SIZE = 250
    COLUNM_VAL_ZERO = 0
    LIST_MIN = 5
    LIST_MAX = WINDOW_HEIGHT - TOP_PAD

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE
    GRADIENTS = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]

    BLOCK_WIDTH = (WINDOW_WIDTH - SIDE_PAD) // LIST_SIZE
    BLOCK_UNIT_HEIGHT = (WINDOW_HEIGHT - TOP_PAD) // (LIST_MAX - COLUNM_VAL_ZERO)
    START_X = SIDE_PAD // 2

    FONT = pygame.font.SysFont('comicsans', 25)
    LARGE_FONT = pygame.font.SysFont('comicsans', 35)