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
            return self.member(root.left, node)
        else:
            return self.member(root.right, node)

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
                # pop the leftmost node
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
                # pop the rightmost node
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

    # insert funcion (to add a new node into a correct location)
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

    # erase function (to mark a specific node as erased)
    def erase(self, root, erase_node):
        if root is None:
            return False
        elif root.value == erase_node.value:
            if root.isErased is True:
                return False
            else:
                root.isErased = True
                return True
        elif erase_node.value < root.value:
            if root.left is None:
                return False
            else:
                return self.erase(root.left, erase_node)
        else:
            if root.right is None:
                return False
            else:
                return self.erase(root.right, erase_node)


    def find_successor(self, current_node):

        while current_node.left:
            current_node = current_node.left
        return current_node

    def delete_node(self, del_node):

        # parent of the iterated node
        parent = None

        # start from root
        current = self.root
        # traverse the tree using binary search
        while current and current.value != del_node:
            parent = current
            # if the node is less than the current value we move to the left
            if del_node < current.value:
                current = current.left
            # otherwise, we move to the right
            else:
                current = current.right

        # If we don't find the value in the tree, we just return the root
        if current == None:
            return self.root

        # 1st case: The node to be deleted does not have child nodes
        if current.left == None and current.right == None:
            # if the node to be deleted is not the root
            if current != self.root:
                # check if it was a left child and we set it to None
                if parent.left == current:
                    parent.left = None
                # otherwise, it was a right child and we set it to None
                else:
                    parent.right = None
            # Otherwise, it is the root so we set the root to None
            else:
                self.root = None

        # 2nd case: Node to be deleted has two children
        if current.left and current.right:
            # find successor node
            successor = self.find_successor(current.right)
            # get the value of the successor
            value = successor.value
            # delete the succsor recursively ( sub case: successor has a right child)
            self.delete_node(value)

            # copy the value of the successor to the current node
            current.value = value
 
        # 3rd case: Node to be deleted has one child only
        else:
            # if the child node is in the left
            if current.left:
                child = current.left
            # otherwise, is in the right
            else:
                child = current.right
            # check if the node to be deleted is not the root of the tree
            if current != self.root:
                # set the parent to be the child depending on if it is to the left or right
                if current == parent.left:
                    parent.left =  child
                else:
                    parent.right = child
            # otherwise it is the root and so we set the child to be the root
            else:
                self.root = child

        return self.root

    def clean(self):
        erased_nodes = []
        # if our root is zero we don't have any deepthness
        if self.root.isErased == True:
            erased_nodes.append(self.root)
        # create a queue using STL
        nodes = []

        # start from the root, since we know we have more levels
        nodes.append(self.root)


        while len(nodes) != 0:

            # move to the next level of deepthness
            numNodes = len(nodes)

            # iterate each node
            while(numNodes > 0):
                # get the front element
                node = nodes[0]
                nodes.pop(0)
                if(node.isErased == True):
                    erased_nodes.append(node)

                # if we find that we have another level to the right or to the left we insert into the queue
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)

                # we reduce the number of nodes visited
                numNodes -= 1
        # iterate each deleted node
        for del_node in erased_nodes:
            self.delete_node(del_node.value)

def main():

    # testing

    root = LazyNode(22)

    tree = LazyTree()
    tree.root = root
    tree.root.isErased = False

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
    root.right.left.isErased = True
    root.right.right = LazyNode(38)
    root.right.right.isErased = False
    #4th level 
    root.left.left.left = LazyNode(4)
    root.left.left.left.isErased = False
    root.left.left.right= LazyNode(8)
    root.left.left.right.isErased = True
    root.left.right.left = LazyNode(14)
    root.left.right.left.isErased = False
    root.left.right.right = LazyNode(20)
    root.left.right.right.isErased = False
    root.right.left.right = LazyNode(28)
    root.right.left.right.isErased = False
    root.right.right.left = LazyNode(34)
    root.right.right.left.isErased = True
    root.right.right.right = LazyNode(42)
    root.right.right.right.isErased = True
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
    root.right.right.right.left.isErased = True






    num = tree.size()
    num2 = tree.height()

    j = tree.empty()
    tree.breadth_first_traversal()
    print()
    tree.clean()
    print('\nAfter clean()')
    tree.breadth_first_traversal()


    minimum_element = tree.front()
    max_element = tree.back()
    print('\n\n','minimum element:', minimum_element.value, '\n', 'maximum element:', max_element.value, '\n')

    # tree = LazyTree()
    # num = int(input("Enter a number to add to the binary search tree: "))


    # j = tree.empty()

    # while num != -1:
    #     node = LazyNode(num)


    #     tree.insert(tree.root, node)
    #     num = int(input("Enter a number to add to the binary search tree: "))

    # tree.breadth_first_traversal()

    # print('\n\n', 'after deletion', '\n\n')

    # #1st test
    # root.left.left.right.isErased = True
    # root.right.left.isErased = True
    # root.right.right.left.isErased = True
    # root.right.right.right.isErased = True
    # root.right.right.right.left.isErased = True

    # tree.breadth_first_traversal()

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


    # tree.breadth_first_traversal()


    # minimum_element = tree.front()
    # max_element = tree.back()

    # print('\n\n','minimum element:', minimum_element.value, '\n', 'maximum element:', max_element.value, '\n')

    # root.left.left.right.isErased = False
    # root.right.left.isErased = False
    # root.right.right.right.isErased = False
    # root.right.right.right.left.isErased = False

    # #2nd test
    # root.left.isErased = True
    # root.left.right.isErased = True
    # root.left.right.left.isErased = True
    # root.left.right.right.isErased = True
    # root.left.right.right.left.isErased = True

    # print("True" if tree.erase(tree.root, LazyNode(8)) else "False")

    # tree = LazyTree()
    # num = int(input("Enter a number to add to the binary search tree: "))

    # j = tree.empty()
    # minimum_element = tree.front()
    # max_element = tree.back()

    # print(minimum_element.value, max_element.value, '\n\n')

    # while num != -1:
    #     node = LazyNode(num)


    #     tree.insert(tree.root, node)
    #     num = int(input("Enter a number to add to the binary search tree: "))


main()
