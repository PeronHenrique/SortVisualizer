from typing import List

def mergeSort(lst: List[int], ascending: bool, originalLst: List[int] = None, lowIndex: int = 0):
    if originalLst is None: originalLst = lst
    if (len(lst) < 2): return

    midPoint: int = len(lst) // 2
    leftList = lst[:midPoint]
    rightList = lst[midPoint:]
    
    yield from mergeSort(leftList, ascending, originalLst, lowIndex)
    yield from mergeSort(rightList, ascending, originalLst, lowIndex+midPoint)

    leftPointer: int = 0
    rightPointer: int = 0
    lstPointer: int = 0

    while leftPointer < len(leftList) and rightPointer < len(rightList):
        leftAscendingCondition = leftList[leftPointer] < rightList[rightPointer] and ascending
        leftDescendingCondition = leftList[leftPointer] > rightList[rightPointer] and not ascending
 
        if (leftAscendingCondition or leftDescendingCondition):
            index1 = lowIndex+leftPointer
            index2 = lowIndex+lstPointer
            if (index1 != index2):
                originalLst[index2] = leftList[leftPointer]
                yield ([index1, index2], False)
            lst[lstPointer] = leftList[leftPointer]
            leftPointer = leftPointer + 1
            lstPointer = lstPointer + 1
        else:
            index1 = lowIndex+midPoint+rightPointer
            index2 = lowIndex+lstPointer
            if (index1 != index2):
                originalLst[index2] = rightList[rightPointer]
                ([index1, index2], False)
            lst[lstPointer] = rightList[rightPointer]
            rightPointer = rightPointer + 1
            lstPointer = lstPointer + 1

    while(leftPointer < len(leftList)):
        index1 = lowIndex+leftPointer
        index2 = lowIndex+lstPointer
        if (index1 != index2):
            originalLst[index2] = leftList[leftPointer]
            yield ([index1, index2], False)
        lst[lstPointer] = leftList[leftPointer]
        leftPointer = leftPointer + 1
        lstPointer = lstPointer + 1

    while(rightPointer < len(rightList)):
        index1 = lowIndex+midPoint+rightPointer
        index2 = lowIndex+lstPointer
        if (index1 != index2):
            originalLst[index2] = rightList[rightPointer]
            ([index1, index2], False)
        lst[lstPointer] = rightList[rightPointer]
        rightPointer = rightPointer + 1
        lstPointer = lstPointer + 1

