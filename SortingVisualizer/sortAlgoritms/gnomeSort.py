from typing import List

def gnomeSort(lst: List[int], ascending: bool):	
	gnomePointer = 0
	while gnomePointer < len(lst):
		if gnomePointer == 0:
			gnomePointer = gnomePointer + 1
			continue

		ascendingCondicion = lst[gnomePointer] < lst[gnomePointer - 1] and ascending
		descendingCondicion = lst[gnomePointer] > lst[gnomePointer - 1] and not ascending
		if ascendingCondicion or descendingCondicion:
			yield ([gnomePointer, gnomePointer - 1], True)
			gnomePointer = gnomePointer - 1
		else:
			gnomePointer = gnomePointer + 1
		
