from typing import List
		
def countingSort(lst: List[int], ascending: bool):
	lstMax = max(lst)

	countLst = [0 for _ in range(lstMax + 1)]
	for i, v in enumerate(lst):
		yield ([0, i], False)
		countLst[v] += 1

	if not ascending:
		countLst.reverse()

	for i, v in enumerate(countLst):
		if i == 0:
			continue
		countLst[i] += countLst[i - 1]  
	
	countLst.insert(0,0)
	countLst.pop()

	if not ascending:
		countLst.reverse()		

	originalLst = lst[0:]
	for i,v in enumerate(originalLst):
		lst[countLst[v]] = v
		yield ([i, countLst[v]], False)
		countLst[v] += 1

	

