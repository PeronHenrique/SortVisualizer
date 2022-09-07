from typing import List

class TreeNode:
	def __init__(self, key) -> None:
		self.key = key
		self.left: TreeNode = None
		self.right: TreeNode = None

	def getValue(self) -> int:
		return self.key[1]

	def getIndex(self) -> int:
		return self.key[0]

	def setValue(self, value: int) -> None:
		self.key = (self.key[0], value)

	def setIndex(self, index: int) -> None:
		self.key =  (index, self.key[1])


class Tree:
	def __init__(self) -> None:
		self.root: TreeNode = None

	

	def insertValue(self, key, ascending: bool):
		self.root = self.insertValueRec(key, ascending, self.root)

	def insertValueRec(self, key, ascending: bool, node: TreeNode) -> TreeNode:
		if node == None:
			return TreeNode(key)


		value = key[1]
		if ((node.getValue() < value and ascending) or 
			(node.getValue() > value and not ascending)): 
			node.left = self.insertValueRec(key, ascending, node.left)
		else:
			node.right = self.insertValueRec(key, ascending, node.right)
		
		return node


	def retrieveValue(self):
		yield from self.retrieveValueRec(self.root)


	def retrieveValueRec(self, node: TreeNode):
		if node == None:
			return

		if node.right != None:
			yield from self.retrieveValueRec(node.right)

		yield node.key
		
		if node.left != None:
			yield from self.retrieveValueRec(node.left)


	def swapIndex(self, index1: int, index2: int) -> None:
		if self.root!= None:
			self.swapIndexRec(self.root, index1, index2)

	def swapIndexRec(self, node: TreeNode, index1: int, index2: int) -> None:
		if node.left != None:
			self.swapIndexRec(node.left, index1, index2)
		
		if node.right != None:
			self.swapIndexRec(node.right, index1, index2)

		if node.getIndex() == index1:
			node.setIndex(index2)
			return

		if node.getIndex() == index2:
			node.setIndex(index1)
			return
		

def treeSort(lst: List[int], ascending: bool):	
	tree = Tree()

	for i,v in enumerate(lst):
		yield ([0, i], False)
		tree.insertValue((i,v), ascending)

	lstPointer = 0
	keysGenerator = tree.retrieveValue()
	while True:
		try:
			index = next(keysGenerator)[0]
		except StopIteration:
			break
		
		yield ([lstPointer, index], True)
		tree.swapIndex(index, lstPointer)
		lstPointer = lstPointer + 1