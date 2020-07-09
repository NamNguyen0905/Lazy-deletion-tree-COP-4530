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

    # member function to search if the given node is in the tree and not tagged as erased
    def member(self, root, node):
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

    def front(self):

        # start from the root
        current = self.root
        # create a stack
        stack = []

        while(True):

            # push every node to the left onto the stack, until the node visited is None
            if current != None:

                stack.append(current)
                current = current.left
            # Now we iterate our stack
            elif(stack):
                #pop the leftmost node
                current = stack.pop()
                # check if the node is not erased. Return if it is not erased
                if(current.isErased == False):
                    return current
                # Otherwise, set current node to be the right node
                current = current.right
            # If our stack is empty that means that our tree is completely erased, so we return an empty node
            else:
                return LazyNode()

    def back(self):

        # start from the root 
        current = self.root
        stack = []

        while(True):
            # push every node to the right onto the stack, until the node visited is None
            if current != None:

                stack.append(current)
                current = current.right
            # Now we iterate our stack
            elif(stack):
                #pop the rightmost node
                current = stack.pop()
                # check if the node is not erased. Return if it is not erased
                if(current.isErased == False):
                    return current
                # Otherwise, set our current node to be the left node
                current = current.left
            # If our stack is empty that means that our tree is completely erased, so we return an empty node
            else:
                return LazyNode()

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

    root = LazyNode(22)
    tree = LazyTree()
    tree.root = root

    # left side pdf example
    # 2nd level
    root.left = LazyNode(12)
    root.left.isErased = False
    root.right = LazyNode(32)
    root.right.isErased = False
    # 3rd level
    root.left.left = LazyNode(6)
    root.left.left.isErased = False
    root.left.right = LazyNode(16)
    root.left.right.isErased = False
    root.right.left = LazyNode(24)
    root.right.left.isErased = False
    root.right.right = LazyNode(38)
    root.right.right.isErased = False
    #4th level 
    root.left.left.left = LazyNode(4)
    root.left.left.left.isErased = False
    root.left.left.right= LazyNode(8)
    root.left.left.right.isErased = False
    root.left.right.left = LazyNode(14)
    root.left.right.left.isErased = False
    root.left.right.right = LazyNode(20)
    root.left.right.right.isErased = False
    root.right.left.right = LazyNode(28)
    root.right.left.right.isErased = False
    root.right.right.left = LazyNode(34)
    root.right.right.left.isErased = False
    root.right.right.right = LazyNode(42)
    root.right.right.right.isErased = False
    #5th level
    root.left.left.left.left = LazyNode(2)
    root.left.left.left.isErased = False
    root.left.left.right.right = LazyNode(10)
    root.left.left.right.right.isErased = False
    root.left.right.right.left = LazyNode(18)
    root.left.right.right.left.isErased = False
    root.right.left.right.left = LazyNode(26)
    root.right.left.right.left.isErased = False
    root.right.left.right.right = LazyNode(30)
    root.right.left.right.right.isErased = False
    root.right.right.left.right = LazyNode(36)
    root.right.right.left.right.isErased = False
    root.right.right.right.left = LazyNode(40)
    root.right.right.right.left.isErased = False






    num = tree.size()
    num2 = tree.height()

    j = tree.empty()

    # tree = LazyTree()
    # num = int(input("Enter a number to add to the binary search tree: "))


    # j = tree.empty()

    # while num != -1:
    #     node = LazyNode(num)


    #     tree.insert(tree.root, node)
    #     num = int(input("Enter a number to add to the binary search tree: "))

    tree.breadth_first_traversal()

    print('\n\n', 'after deletion', '\n\n')

    #1st test
    root.left.left.right.isErased = True
    root.right.left.isErased = True
    root.right.right.left.isErased = True
    root.right.right.right.isErased = True
    root.right.right.right.left.isErased = True

    tree.breadth_first_traversal()


    minimum_element = tree.front()
    max_element = tree.back()

    print('\n\n','minimum element:', minimum_element.value, '\n', 'maximum element:', max_element.value, '\n')

     root.left.left.right.isErased = False
    root.right.left.isErased = False
    root.right.right.right.isErased = False
    root.right.right.right.left.isErased = False

    #2nd test
    root.left.isErased = True
    root.left.right.isErased = True
    root.left.right.left.isErased = True
    root.left.right.right.isErased = True
    root.left.right.right.left.isErased = True

    tree.breadth_first_traversal()

    minimum_element = tree.front()
    max_element = tree.back()

    print('\n\n','minimum element:', minimum_element.value, '\n', 'maximum element:', max_element.value, '\n')

main()
