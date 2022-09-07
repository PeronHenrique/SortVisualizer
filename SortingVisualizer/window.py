import random
import pygame

pygame.init()

from sortAlgoritms.sorterFactory import SorterFactory
from sortAlgoritms.sortAlgoritm import SortAlgoritm
from config import Config
from drawer import Drawer

class WindowControl:
	def __init__ (self) -> None:
		self.clock: pygame.time.Clock = pygame.time.Clock()
		self.window: pygame.Surface = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
		pygame.display.set_caption("Sorting Algorithm Visualization")

		self.drawer: Drawer = Drawer(self.window)
		self.runing: bool = True
		self.sorting: bool = False
		self.ascending: bool = True
		
		self.newList()
		self.sorter: SortAlgoritm = SorterFactory.getSorter(self.lst, self.ascending)
		self.drawer.drawWindow(self.sorter.name, self.ascending)
		self.drawer.drawListColumns(self.lst)

	
	def run(self) -> None:

		while self.runing:
			self.clock.tick(60)
			if self.sorting:
				self.swapColunms()

			    
			pygame.display.update()
			self.handleEvents()
			
		pygame.quit()


	def swapColunms(self) -> None:
		swapIndex, shouldSwap  = self.sorter.sort()
		if len(swapIndex) != 2:
			self.sorting = False
			if(self.verifySort()):
				colors = {i: Config.GREEN for i in range(len(self.lst))}
				self.drawer.drawListColumns(self.lst, colors)
			else:
				colors = {i: Config.RED for i in range(len(self.lst))}
				self.drawer.drawListColumns(self.lst, colors)
		else:
			index1, index2 = swapIndex
			if shouldSwap:
				self.lst[index1], self.lst[index2] = self.lst[index2], self.lst[index1]
			self.drawer.drawListColumns(
				self.lst, 
				{index1: Config.GREEN, index2: Config.RED})


	def newList(self) -> None: 
		self.lst = []
		for _ in range(Config.LIST_SIZE):
			val = random.randint(Config.LIST_MIN, Config.LIST_MAX)
			self.lst.append(val)
		
		self.lstOriginal = self.lst[0:] # only used for verification


	def verifySort(self) -> bool:
		# certify that every element still is in the list
		for v in self.lstOriginal:
			if v not in self.lst:
				return False

		# verify the order of the list
		for i in range(len(self.lst) - 1):
			if self.ascending:
				if self.lst[i] > self.lst[i+1]: 
					return False
			else:
				if self.lst[i] < self.lst[i+1]: 
					return False
		return True


	def handleEvents(self) -> None: 
		for event in pygame.event.get():
			updateWindow: bool = False

			if event.type == pygame.QUIT:
				self.runing = False

			if event.type != pygame.KEYDOWN:
				continue
			
			if event.key == pygame.K_r:
				self.newList()
				self.sorter.setList(self.lst)
				self.sorting = False
				self.drawer.drawListColumns(self.lst)
				continue

			if self.sorting: continue

			if event.key == pygame.K_SPACE:
				self.sorting = True
				continue
			
			

			if event.key == pygame.K_a:
				self.ascending = True
				updateWindow = True
				self.sorter.setAscending(self.ascending)
				

			if event.key == pygame.K_d:
				self.ascending = False
				updateWindow = True
				self.sorter.setAscending(self.ascending)
					

			if event.key == pygame.K_LEFT:
				self.sorter = SorterFactory.previusSorter(self.lst, self.ascending)
				self.sorting = False
				updateWindow = True
				

			if event.key == pygame.K_RIGHT:
				self.sorter = SorterFactory.nextSorter(self.lst, self.ascending)
				self.sorting = False
				updateWindow = True
				

			if updateWindow:
				self.drawer.drawWindow(self.sorter.name, self.ascending)
				self.drawer.drawListColumns(self.lst)



