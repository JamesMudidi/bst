def find(node,value):

    # To search a given value in BST,
    # we have to first compare it with root,
    # if the given value is present at root, we return root.
    # If the given value is greater than root’s value,
    # we go to the right subtree of root node.
    # Otherwise we go to the left subtree.

    # Base Cases:
    # First compare the given value with root to check
    # if given value is present at root
    if node is None or node.value == value:
        return node
  
    # if given value is greater than node's value
    if node.value < value:
        return find(node.rightChild,value)
    
    # if given value is smaller than node's value
    return find(node.leftChild,value)
