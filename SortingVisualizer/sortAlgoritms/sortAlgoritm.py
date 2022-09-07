import string
from typing import List

def noSorter(lst: List[int], ascending: bool):
    yield [0,0]

class SortAlgoritm:
    name: string
    lst: List[int]
    ascending: bool

    def __init__(self, lst: List[int], ascending: bool):
        self.lst = lst
        self.ascending = ascending
        self.name = "No Sorter"
        self.sorterAlgoritm = noSorter
        self.sorterGeneretor = self.sorterAlgoritm(self.lst, self.ascending)


    def sort(self):
        swap = [0,0]
        while swap[0] == swap[1]:
            try:
                key = next(self.sorterGeneretor)
            except StopIteration:
                return ([], False)
            
            swap = key[0]
        
        return key
        

    def setList(self, lst: List[int]) -> None:
        self.lst = lst
        self.sorterGeneretor = self.sorterAlgoritm(self.lst, self.ascending)

    def setAscending(self, ascending: bool) -> None:
        self.ascending = ascending
        self.sorterGeneretor = self.sorterAlgoritm(self.lst, self.ascending)
        
    def setSorter(self, sorter) -> None:
        self.sorterAlgoritm = sorter
        self.sorterGeneretor = self.sorterAlgoritm(self.lst, self.ascending)

    
    def setName(self, name: string) -> None:
        self.name = name
