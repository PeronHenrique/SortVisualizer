from typing import List

def pigeonholeSort(lst: List[int], ascending: bool):
	minLst = min(lst)
	maxLst = max(lst)
	lstRange = maxLst - minLst + 1

	holles = [0]*lstRange

	for i,v in enumerate(lst):
		holles[v-minLst] += 1
		yield ([0, i], False)
	
	if not ascending:
		holles.reverse()

	lstPoiter = 0
	for i, v in enumerate(holles):
		for _ in range(v):
			if ascending:
				lst[lstPoiter] = i + minLst
				yield ([0, lstPoiter], False)
			else:
				lst[lstPoiter] = maxLst - i
				yield ([0, lstPoiter], False)
			lstPoiter += 1

