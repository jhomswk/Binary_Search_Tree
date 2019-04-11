from binary_search_tree import Binary_Search_Tree

def height(node):
    """
    Returns the height of the AVL tree rooted at node.
    """
    return node.height if node else -1


def update_height(node):
    """
    Updates the height of the AVL tree rooted at node.
    """
    node.height = 1 + max(height(node.left), height(node.right))


class AVL_Tree(Binary_Search_Tree):
    """
    AVL-Tree data structure.
    """
   
    def rotate_left(self, node):
        """
        Left-rotates the binary search sub-tree rooted at node.
        """
        child = node.right
        child.parent = node.parent
        if not node.parent:
            self.root = child
        else:
            if node is node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        node.right = child.left
        if node.right:
            node.right.parent = node
        child.left = node
        node.parent = child
        update_height(node)
        update_height(child)

    
    def rotate_right(self, node):
        """
        Right-rotates the binary search sub-tree rooted at node.
        """
        child = node.left
        child.parent = node.parent
        if not node.parent:
            self.root = child
        else:
            if node is node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        node.left = child.right
        if node.left:
            node.left.parent = node
        child.right = node
        node.parent = child
        update_height(node)
        update_height(child)


    def balance(self, node):
        """
        Keeps the binary search tree balanced.
        """
        while node:
            update_height(node) 
            if height(node.left) - height(node.right) > 1:
                if height(node.left.left) >= height(node.left.right):
                    self.rotate_right(node)
                else:
                    self.rotate_left(node.left)
                    self.rotate_right(node)
            elif height(node.right) - height(node.left) > 1:
                if height(node.right.right) >= height(node.right.left):
                    self.rotate_left(node)
                else:
                    self.rotate_right(node.right)
                    self.rotate_left(node)
            node = node.parent
            

    def insert(self, key):
        """
        Inserts a node containing the given key.
        """
        node = super(AVL_Tree, self).insert(key)
        self.balance(node)
                    

    def delete(self, key):
        """
        Deletes a node containing the given key.
        """
        node = super(AVL_Tree, self).delete(key)
        self.balance(node.parent)

