from operator import indexOf
from typing import List

def selectionSort(lst: List[int], ascending: bool):	
    lstPointer: int = 0
    while lstPointer < len(lst):
        unsortedLst = lst[lstPointer:]
        if ascending:
            selectedIndex = indexOf(unsortedLst, min(unsortedLst)) + lstPointer
        else:
            selectedIndex = indexOf(unsortedLst, max(unsortedLst)) + lstPointer
            
        yield ([lstPointer, selectedIndex], True)
        
        lstPointer = lstPointer + 1