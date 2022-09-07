import random
from typing import List
		
def bogoSort(lst: List[int], ascending: bool):
	n = len(lst)
	while not lstSorted(lst, ascending):
		for i in range(n-1):
			yield ([i, i+1], False)
		yield from shuffle(lst)


def shuffle(lst: List[int]):
	n = len(lst)
	for i in range (n):
		index = random.randint(0, n-1)
		yield ([i, index], True)


def lstSorted(lst: List[int], ascending: bool) -> bool:
	for i in range(len(lst) - 1):
		if ascending:
			if lst[i] > lst[i+1]: 
				return False
		else:
			if lst[i] < lst[i+1]: 
				return False
	return True


