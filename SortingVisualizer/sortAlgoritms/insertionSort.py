from typing import List

def insertionSort(lst: List[int], ascending: bool):	
	for i in range(1, len(lst)):
		while True:
			ascendingCondition = i > 0 and lst[i - 1] > lst[i] and ascending
			descendingCondition = i > 0 and lst[i - 1] < lst[i] and not ascending

			if not ascendingCondition and not descendingCondition:
				break

			yield ([i-1, i], True)
			i = i - 1