# Lazy Deletion Tree #

import queue

# Node class for the lazy deletion tree


class LazyNode:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None
        self.isErased = False

# class for the lazy deletetion tree


class LazyTree:
    # constructor for deletion tree
    def __init__(self, nonErased=0):
        self.nonErased = nonErased
        self.root = None

    #--------------- Accesors ---------------#

    # checks if the tree is empty
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
        if self.root.value is None:
            return 0

        # create a queue using STL
        nodes = queue.Queue()

        # start from the root, since we know we have more levels
        nodes.put(self.root)
        height = 0

        while nodes.qsize() != 0:

            # move to the next level of deepthness
            height += 1
            numNodes = nodes.qsize()

            # iterate each node
            while(numNodes > 0):
                # get the front element
                node = nodes.get()

                # if we find that we have another level to the right or to the left we insert into the queue
                if node.left is not None:
                    nodes.put(node.left)
                if node.right is not None:
                    nodes.put(node.right)

                # we reduce the number of nodes visited
                numNodes -= 1

        return height

    # serach function to find if the given node is in the tree and not tagged as erased
    def search(self, root, node):
        if root is None:
            return False
        elif node.value == root.value:
            return True
        elif node.value < root.value:
            return self.search(root.left, node)
        else:
            return self.search(root.right, node)

    # breadth_first_traversal function
    def breadth_first_traversal(self):
        if self.root is None:
            print(" ")
        else:
            nodes = queue.Queue()
            nodes.put(self.root)

            while nodes.qsize() != 0:
                numNodes = nodes.qsize()

                # Iterate each node
                while(numNodes > 0):
                    # Get the front element
                    node = nodes.get()
                    print(node.value, "x " if node.isErased ==
                          True else " ", end="")

                    # Add child node into queue if existing
                    if node.left is not None:
                        nodes.put(node.left)
                    if node.right is not None:
                        nodes.put(node.right)

                    numNodes -= 1

    #--------------- Mutators ---------------#

    # insert funcion ( to add a new node into a correct location)
    def insert(self, root, node):
        if root is None:
            self.root = node
            self.nonErased += 1
        elif node.value < root.value:
            if root.left is None:
                root.left = node
                self.nonErased += 1
            else:
                self.insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
                self.nonErased += 1
            else:
                self.insert(root.right, node)


def main():

    # testing
    # root = LazyNode(22)
    # tree = LazyTree(1)
    # tree.root = root

    # root.right = LazyNode(32)
    # root.left = LazyNode(12)
    # root.left.left = LazyNode(6)
    # root.left.left.left = LazyNode(4)
    # root.left.left.right = LazyNode(8)

    # num = tree.size()
    # num2 = tree.height()

    # j = tree.empty()

    # print(tree.root.left.left.value, tree.nonErased, j, num2, "\n\n")

    # tree.breadth_first_traversal()

    # print(tree.search(tree.root, LazyNode(8)))

    tree = LazyTree()
    num = int(input("Enter a number to add to the binary search tree: "))

    while num != -1:
        node = LazyNode(num)

        tree.insert(tree.root, node)
        num = int(input("Enter a number to add to the binary search tree: "))

    tree.breadth_first_traversal()


main()
