from typing import List

def combSort(lst: List[int], ascending: bool):
	gap: int = len(lst)
	while gap > 0:
		for i in range(len(lst) - gap):
			for j in range(len(lst) - gap - i):
				num1 = lst[j]
				num2 = lst[j + gap]

				if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
					yield ([j, j+gap], True)
		
		gap = gap // 2 