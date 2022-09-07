from typing import List
from sortAlgoritms.sortAlgoritm import SortAlgoritm

from sortAlgoritms.bubbleSort import bubbleSort
from sortAlgoritms.insertionSort import insertionSort
from sortAlgoritms.mergeSort import mergeSort
from sortAlgoritms.quickSortHighIndex import quickSortHighIndex
from sortAlgoritms.quickSortRandom import quickSortRandom
from sortAlgoritms.selectionSort import selectionSort
from sortAlgoritms.heapSort import heapSort
from sortAlgoritms.treeSort import treeSort
from sortAlgoritms.gnomeSort import gnomeSort
from sortAlgoritms.countingSort import countingSort
from sortAlgoritms.shellSort import shellSort
from sortAlgoritms.combSort import combSort
from sortAlgoritms.pigeonholeSort import pigeonholeSort
from sortAlgoritms.bogoSort import bogoSort


class SorterFactory:
    SorterList = [
        ("Bubble Sort", bubbleSort),
        ("Insertion Sort", insertionSort),
        ("Merge Sort", mergeSort),
        ("Quick Sort highIndex", quickSortHighIndex),
        ("Quick Sort Random", quickSortRandom),
        ("Selection Sort", selectionSort),     
        ("Heap Sort", heapSort),         
        ("Tree Sort", treeSort),         
        ("Gnome Sort", gnomeSort), 
        ("Counting Sort", countingSort),
        ("Shell Sort", shellSort),  
        ("Comb Sort", combSort),
        ("Pigeonhole Sort", pigeonholeSort),
        ("Bogo Sort", bogoSort),
    ]

    N_SORTERS = len(SorterList)
    sorterIndex: int = 0

    def nextSorter(lst: List[int], ascending: bool) -> SortAlgoritm:
        SorterFactory.sorterIndex = (SorterFactory.sorterIndex + 1) % SorterFactory.N_SORTERS
        return SorterFactory.getSorter(lst, ascending)

    def previusSorter(lst: List[int], ascending: bool ) -> SortAlgoritm:
        SorterFactory.sorterIndex += SorterFactory.N_SORTERS - 1
        SorterFactory.sorterIndex %= SorterFactory.N_SORTERS
        return SorterFactory.getSorter(lst, ascending)

    def getSorter(lst: List[int], ascending: bool ) -> SortAlgoritm:
        sorterAlg = SortAlgoritm(lst, ascending)
        sorterName, sorterGenerator = SorterFactory.SorterList[SorterFactory.sorterIndex]
        sorterAlg.setName(sorterName)
        sorterAlg.setSorter(sorterGenerator)
        return sorterAlg
