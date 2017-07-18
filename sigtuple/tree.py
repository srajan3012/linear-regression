class Node:
	def __init__(self,key):
		self.right = None
		self.left = None
		self.val = key


root = Node(1)
root.right = Node(2)
root.left = Node(3)

root.left.left = Node(4)

x = ''' 1
	  3   2
	4  \    '''

root1 = root

while root != None:
	print(root.val)
	root = root.left

# while root != None:
# 	print(root.val)
# 	root = root.left