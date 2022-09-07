import random
from typing import List


def quickSortRandom(lst: List[int], ascending: bool, lowIndex: int = -1, highIndex: int = -1):
    if (highIndex == -1 and lowIndex == -1):
        lowIndex = 0
        highIndex = len(lst) - 1

    if (highIndex <= lowIndex): return

    #choose Pivot
    pivotIndex = random.randint(lowIndex, highIndex)
    pivot = lst[pivotIndex]
    yield ([pivotIndex, highIndex], True)


    #Particioning the list
    leftPoiter = lowIndex
    rightPoiter = highIndex - 1

    while(leftPoiter < rightPoiter):

        while(((lst[leftPoiter] <= pivot and ascending) or 
                (lst[leftPoiter] >= pivot  and not ascending)) and 
                leftPoiter < rightPoiter):
            leftPoiter = leftPoiter + 1
        
        while(((lst[rightPoiter] >= pivot and ascending) or 
                (lst[rightPoiter] <= pivot  and not ascending)) and 
                leftPoiter < rightPoiter):
            rightPoiter = rightPoiter - 1

        yield ([leftPoiter, rightPoiter], True)
    
    if((lst[leftPoiter] > lst[highIndex] and ascending) or 
        (lst[leftPoiter] < lst[highIndex]  and not ascending)):
        yield ([leftPoiter, highIndex], True)
    else:
        leftPoiter = highIndex

    #recursive Call
    yield from quickSortRandom(lst, ascending, lowIndex, leftPoiter -1)
    yield from quickSortRandom(lst, ascending, leftPoiter + 1, highIndex)