# Lazy Deletion Tree #

import queue

# Node class for the lazy deletion tree
class LazyNode:
	def __init__(self, value = None):
		self.value = value
		self.right = None
		self.left = None
		self.isErased = False

# class for the lazy deletetion tree
class LazyTree:
	# constructor for deletion tree
	def __init__(self, nonErased = None):
		self.nonErased = nonErased
		self.root = None

	# Accesors

	#checks if the tree is empty
	def empty(self):
		if self.nonErased == 0:
			return True
		else:
			return False

	# size returns the number of nonerased objects in the tree
	def size(self):
		return self.nonErased

	# height calculates the deepthness of the tree by using a queue
	def height(self):

		# if our root is zero we don't have any deepthness
		if self.root.value == None:
			return 0

		# create a queue using STL
		nodes = queue.Queue()

		# start from the root, since we know we have more levels
		nodes.put(self.root)
		height = 0

		while(nodes.qsize() != 0):


			# move to the next level of deepthness
			height += 1
			numNodes = nodes.qsize()

			#iterate each node
			while(numNodes > 0):
				# get the front element 
				node = nodes.get()

				# if we find that we have another level to the right or to the left we insert into the queue
				if node.left != None:
					nodes.put(node.left)
				if node.right != None:
					nodes.put(node.right)

				# we reduce the number of nodes visited and move to the right
				numNodes -= 1

		return height

def main():

	# testing
	root = LazyNode(10)
	tree = LazyTree(1)
	tree.root = root

	root.right = LazyNode(16)
	root.left = LazyNode(20)
	root.left.left = LazyNode(15)
	root.left.left.left = LazyNode(83)
	root.left.left.left.right = LazyNode(8453)


	num = tree.size()
	num2 = tree.height()



	j = tree.empty()

	print(tree.root.left.left.value, tree.nonErased, j, num2)


main()