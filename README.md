Lazy deletion treee program

# Roles:

@ Nhat Nam, Nguyen:
  - member(): using the breadth-first-traversal to search for the existence of the provided node. At first, I have to check whether the root exists or not to proceed, and then check for the node's value itself as well as its children, hence using recursion technique.
  - breadth_first_traversal(): using the principle of queue, I store all visited nodes into it. After that, when traversing to all children of the immediate root, I'll pop the queue, printing out the current node as repeating these steps to the end of the tree.
  - insert(): using the BST principle, I keep going deep down by comparing the current node with the add_node. When reaching the end of the tree, the add_node will be appended to the right or left of the current node depending on its value.
  - erase(): using the same technique as the member function, but when found the node, it will check whether that node is already marked as erased or not to process correspondingly.
  - clear(): traversing through the tree until reaching its end, then stepback to the immediate parent to detach itself with the visited child. The function will continue repeating the same for the other child.
