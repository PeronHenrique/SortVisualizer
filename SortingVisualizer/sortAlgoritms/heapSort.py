from typing import List

def heapify(lst: List[int], ascending: bool, heapSize: int, root: int):
	indexLargest = root
	leftNode = root * 2 + 1
	rigthNode = root * 2 + 2

	#left Node
	CondiscionAscending = leftNode < heapSize and lst[leftNode] > lst[indexLargest] and ascending
	CondiscionDescending = leftNode < heapSize and lst[leftNode] < lst[indexLargest] and not ascending
	if(CondiscionAscending or CondiscionDescending):
		indexLargest = leftNode

	#rigth Node
	CondiscionAscending = rigthNode < heapSize and lst[rigthNode] > lst[indexLargest] and ascending
	CondiscionDescending = rigthNode < heapSize and lst[rigthNode] < lst[indexLargest] and not ascending
	if(CondiscionAscending or CondiscionDescending):
		indexLargest = rigthNode

	if (root != indexLargest):
		yield ([root, indexLargest], True)
		yield from heapify(lst, ascending, heapSize, indexLargest)
	

def heapSort(lst: List[int], ascending: bool):	
	heapSize: int = len(lst)

	for i in reversed(range(heapSize//2)):
		yield from heapify(lst, ascending, heapSize, i)

	for i in reversed(range(heapSize)):
		yield ([0, i], True)
		yield from heapify(lst, ascending, i, 0)