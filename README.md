Lazy deletion treee program

# Roles:

@ Nhat Nam, Nguyen:
  - member(): using the breadth-first-traversal to search for the existence of the provided node. At first, I have to check whether the root exists or not to proceed, and then check for the node's value itself as well as its children, hence using recursion technique.
  - breadth_first_traversal(): using the principle of queue, I store all visited nodes into it. After that, when traversing to all children of the immediate root, I'll pop the queue, printing out the current node as repeating these steps to the end of the tree.
  - insert(): using the BST principle, I keep going deep down by comparing the current node with the add_node. When reaching the end of the tree, the add_node will be appended to the right or left of the current node depending on its value.
  - erase(): using the same technique as the member function, but when found the node, it will check whether that node is already marked as erased or not to process correspondingly.
  - clear(): traversing through the tree until reaching its end, then stepback to the immediate parent to detach itself with the visited child. The function will continue repeating the same for the other child.

@ Kin NG:
- empty(): empty checks the member variable of the LazyTree class "nonerased" to determine if the tree is empty or it has elements added to it. Returns a Boolean variable that confirms the state.
- size(): Returns the number of nodes that are considered to be non-erased within the tree by making use of the "nonerased" member variable of the LazyTree class.
- height(): This functions makes use of a breadth first traversal to register the level of deepthness of the tree. The traversal works with the principle of the queue and traverses each parent node adding its children, if any, into the queue, after all children are enqueued, then we increase the height variable which signifies the next level within our tree, effectively running in O(N) where N represents the number of nodes
- front(): The front function uses an inorder traversal to find the maximum non-erased node within the BST. The inorder traversal works in 3 steps, it first traverses the left subtree, after it visits the root, and lastly it proceeds to visit the right subtree. To accomplish our objective, we push every single node to the right of root onto the stack and proceed to pull from the stack while doing the inorder traversal. The first element found to have an "isErased" property of False will be our maximum element.
- back(): The back function ses an inorder traversal to find the maximum non-erased node within the BST. The inorder traversal works in 3 steps, it first traverses the left subtree, after it visits the root, and lastly it proceeds to visit the right subtree. To accomplish our objective, we push every single node to the left of root onto the stack and proceed to pull from the stack while doing the inorder traversal. The first element found to have an "isErased" property of False will be our minimum element.
- clean():The function makes use of BFS to find all the erased nodes within the tree. After that it performs a binary search for each node to be erased and analyzes the 3 cases for deletion by taking into account the position of the node with respect to the tree it updates the tree and returns. In general it would take O(N^2).