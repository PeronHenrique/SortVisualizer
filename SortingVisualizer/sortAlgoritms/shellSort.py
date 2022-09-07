from typing import List
		
def shellSort(lst: List[int], ascending: bool):
	gap = len(lst) // 2

	while gap > 0:
		for i in range(gap, len(lst)):
			j = i
			while j >= gap:
				ascendingCondition = lst[j] < lst[j - gap] and ascending
				descendingCondition = lst[j] > lst[j - gap] and not ascending
				if ascendingCondition or descendingCondition:
					yield ([j, j-gap], True)
				j -= gap
		gap = gap // 2


