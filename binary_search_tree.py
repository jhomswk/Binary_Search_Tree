class Node(object):
    """
    Tree node data structure.
    """

    def __init__(self, key):
        """
        Generates a binary search tree node.
        """
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
    

    def min(self):
        """
        Returns a node containing the smallest
        key in self's binary search sub-tree.
        """
        min = self
        while min.left:
            min = min.left
        return min


    def max(self):
        """
        Returns a node containing the largest
        key in self's binary search sub-tree.
        """
        max = self
        while max.right:
            max = max.right
        return max


    def find(self, key):
        """
        Returns a node containing key in self's 
        binary search sub-tree if such node exists,
        and None otherwise.
        """
        if key == self.key:
            return self
        if key < self.key:
                return self.left and self.left.find(key)
        if key > self.key:
                return self.right and self.right.find(key)


    def find_iterative(self, key):
        """
        Returns a node containing key in self's 
        binary search sub-tree if such node exists,
        and None otherwise.
        """
        candidate = self
        while candidate:
            if key < candidate.key:
                candidate = candidate.left
            elif key > candidate.key:
                candidate = candidate.right
            else:
                return candidate
        return None


    def successor(self):
        """
        Returns a node containing the key that succeeds 
        self's key in self's binary search sub-tree.
        """
        if self.right:
            return self.right.min()
        candidate = self
        while candidate.parent and candidate is candidate.parent.right:
            candidate = candidate.parent
        return candidate.parent 


    def predecessor(self):
        """
        Returns a node containing the key that precedes 
        self's key in self's binary search sub-tree.
        """
        if self.left:
            return self.left.max()
        candidate = self
        while candidate and candidate is candidate.parent.left:
            candidate = candidate.parent
        return candidate.parent


    def inorder(self):
        """
        Walks the tree in non-decreasing key ordering.
        """
        if self.left:
            self.left.inorder()
        print self.key
        if self.right:
            self.right.inorder()


    def inorder_iterative(self):
        """
        Walks the tree in non-decreasing key ordering
        """
        min = self 
        stack = []
        while min or stack:
            while min:
                stack.append(min)
                min = min.left
            min = stack.pop()
            print min.key
            min = min.right


    def insert(self, node):
        """
        Inserts node into self's binary search sub-tree
        and restores the binary search property.
        """
        if not node:
            return

        if node.key < self.key:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node 
                node.parent = self
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
                node.parent = self
    

    def delete(self):
        """
        Deletes self from the binary search sub-tree
        and restores the binary search property.
        """
        if not self.left or not self.right:
            child = self.left or self.right
            if self.parent:
                if self is self.parent.left:
                    self.parent.left = child
                else:
                    self.parent.right = child
            if child:
                child.parent = self.parent
            return self
        else:
            successor = self.right.min()
            self.key = successor.key
            return successor.delete()


    def RI(self):
        """
        Verifies the binary search property in self's
        binary search sub-tree.
        """
        if self.left:
            if self.key < self.left.key:
                raise RuntimeError("BST property violation")
            if self.left.parent is not self:
                raise RuntimeError("parent <-> child violation")
            self.left.RI()

        if self.right:
            if self.key > self.right.key:
                raise RuntimeError("BST property violation")
            if self.right.parent is not self:
                raise RuntimeError("parent <-> child violation")
            self.right.RI()


    def _str(self):
        """
        Computes self's binary search sub-tree representation.
        """
        label = str(self.key)

        left_lines, left_pos, left_width = ([], 1, 1) if self.left is None else self.left._str()
        right_lines, right_pos, right_width = ([], 1, 1) if self.right is None else self.right._str()

        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos

        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)

        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)

        if (middle - len(label)) % 2 == 1\
            and self.parent is not None\
            and self is self.parent.left\
            and len(label) < middle:
                label += '.'

        label = label.center(middle, '.')

        if label[0] == '.':
            label = ' ' + label[1:]
        if label[-1] == '.':
            label = label[:-1] + ' '

        lines =  [' '*left_pos + label + ' '*(right_width - right_pos),
                  ' '*left_pos + '/' + ' '*(middle-2) +
                  '\\' + ' '*(right_width - right_pos)]

        lines += [left_line + ' '*(width - left_width - right_width) + right_line
                       for (left_line, right_line) in zip(left_lines, right_lines)]

        return lines, pos, width


    def __str__(self):
        """
        Returns self's binary search sub-tree representation.
        """
        return '\n'.join(self._str()[0])



class Binary_Search_Tree(object):
    """
    Binary search tree data structure.
    """


    def __init__(self, key):
        """
        Returns a binary search tree initialized with the given key.
        """
        self.root = Node(key)


    def min(self):
        """
        Returns a node containing the smallest key in the binary
        search tree.
        """
        return self.root and self.root.min()


    def max(self):
        """
        Returns a node containing the largest key in the binary
        search tree.
        """
        return self.root and self.root.max()


    def find(self, key):
        """
        Returns a node containing key in the binary search tree
        if such node exists, and None otherwise.
        """
        return self.root and self.root.find(key)


    def find_iterative(self, key):
        """
        Returns a node containing key in the binary search tree
        if such node exists, and None otherwise.
        """
        return self.root and self.root.find_iterative(key)


    def successor(self, key):
        """
        Returns a node containing the key that succeeds 
        key in the binary search tree.
        """
        node = self.find(key)
        return node and node.successor()


    def predecessor(self, key):
        """
        Returns a node containing the key that precedes 
        key in the binary search tree.
        """
        node = self.find(key)
        return node and node.predecessor()


    def inorder(self):
        """
        Walks the BST in non-decreasing key ordering.
        """
        if self.root:
            self.root.inorder()


    def inorder_iterative(self):
        """
        Walks the BST in non-decreasing key ordering.
        """
        if self.root:
            self.root.inorder_iterative()

    
    def insert(self, key):
        """
        Inserts a node containing key into the binary
        search tree.
        """
        node = Node(key)
        if self.root:
            self.root.insert(node)
        else:
            self.root = node 
#       self.RI()
        return node


    def delete(self, key):
        """
        Deletes a node containing key from the binary 
        search tree.
        """
        node = self.root and self.root.find(key)
        if not node:
            return None
        if node is self.root and (not node.left or not node.right):
            self.root = node.left or node.right 
        node = node.delete()
#       self.RI()
        return node


    def RI(self):
        """
        Verifies the binary search property.
        """
        if self.root:
            if self.root.parent:
                raise RuntimeError("parent <-> child violation")
            self.root.RI()


    def __str__(self):
        """
        Returns a string representing the binary search tree.
        """
        if self.root is None: return '<empty tree>'
        return str(self.root)

    def __repr__(self):
        """
        Represents the binary search tree.
        """
        return str(self)

