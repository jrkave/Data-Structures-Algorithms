# Red Black Tree Implementation and Methods

# Review of Red Black Tree Properties:
# 0. It is a self balancing binary search tree.
# 1. Every node is either red or black
# 2. The root is always black
# 3. Every leaf, which is nil, is black
# 4. If a node is red, then its children are black
# 5. Every path from a node to any of its descendant nil node has
# the same number of black nodes (including the nil node in the count)

from enum import Enum

# Create RED BLACK Types
class Color(Enum):
    RED = 1
    BLACK = 2

# Node class
class Node(object):
    
    # Each node has attributes: key, parent, left child, right child, color
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None
        self.color = Color.RED
    
    def __str__(self):
        return str(self.key)

# Red Black Tree Class
class RedBlackTree(object):
    
    def __init__(self):
        # make nil node and set properties
        self.nil = Node(0)
        self.nil.color = Color.BLACK
        self.nil.left = None
        self.nil.right = None
        # set root to nil node
        self.root = self.nil
    
    def leftRotate(self, x):
        # y becomes new parent of x
        # x becomes y's left child
        # y's left child becomes x's right child
        # note: x's left child and y's right child do not change
        
        # set y to right child of x
        y = x.right
        # set right child of x to y's left child
        x.right = y.left
        # set y's left child to have parent x
        if y.left != self.nil:
            y.left.p = x  
        # x's parent becomes y's parent  
        y.p = x.p 
        # if x was root, y becomes root
        if x.p == self.nil:
            self.root = y
        # if x was left child, y becomes left child
        elif x == x.p.left:
            x.p.left = y
        # if x was right child, y becomes right child
        else:  
            x.p.right = y
        # y's left child becomes x
        y.left = x
        # y becomes parent of x
        x.p = y
    
    def rightRotate(self, x):
        # y becomes new parent of x
        # x becomes y's right child
        # y's right child becomes x's left child
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
    
    ''' INSERTING '''
    
    def rbInsert(self, key):
        # create new node to be inserted and set left/right children to self.nil
        z = Node(key)
        z.left = self.nil
        z.right = self.nil
        
        y = self.nil   # y used as trailing pointer
        x = self.root  # initializes x as root (used to traverse down tree)
        
        # search subtrees
        while x != self.nil:
            # keeps a record of x's previous position
            y = x
            # go down left side if key is smaller
            if z.key < x.key:
                x = x.left
            # go down right side if key is greater
            else:
                x = x.right
        
        # z's parent is set to y (y is future parent of z)   
        z.p = y
        # determines whether z is root
        if y == self.nil:
            # z becomes root if tree was empty
            self.root = z
        elif z.key < y.key:
            # y's left child becomes z
            y.left = z
        else:
            # y's right child becomes z
            y.right = z
        
        # set z's left and right child to nil and color z red
        z.left = self.nil
        z.right = self.nil
        z.color = Color.RED
        
        # rotate and recolor to fix violations
        self.rbInsertFixup(z)
    
    def rbInsertFixup(self, z):
        while z.p.color == Color.RED:
            # z's parent is a left child
            if z.p == z.p.p.left: 
                y = z.p.p.right # y = uncle
                # case 1
                if y.color == Color.RED:
                    z.p.color = Color.BLACK 
                    y.color = Color.BLACK 
                    z.p.p.color = Color.RED 
                    z = z.p.p 
                else: # uncle is black
                    # case 2 (triangle)
                    if z == z.p.right: # z is right child, parent is left child
                        z = z.p 
                        self.leftRotate(z) # requires left rotation to become line case
                    # case 3 (line) 
                    # recolor parent, grandparent, and rightRotate z's grandparent
                    z.p.color = Color.BLACK
                    z.p.p.color = Color.RED
                    self.rightRotate(z.p.p)
            # z's parent is a right child
            else:
                y = z.p.p.left # y = uncle
                # case 1: uncle is red
                if y.color == Color.RED:
                    z.p.color = Color.BLACK
                    y.color = Color.BLACK
                    z.p.p.color = Color.RED
                    z = z.p.p
                else: # uncle is black
                    # case 2: node is left child
                    if z == z.p.left: 
                        z = z.p
                        self.rightRotate(z)
                    # case 3: node is right child
                    z.p.color = Color.BLACK
                    z.p.p.color = Color.RED
                    self.leftRotate(z.p.p)

        self.root.color = Color.BLACK
    
    def treeMin(self, x):
        while x.left != self.nil:
            x = x.left
        return x
    
    # Helps us move subtrees within the tree
    # Breaks links to 'u'
    # Connects links to 'v'  
    def rbTransplant(self, u, v):
        if u.p == self.nil: # when u is root
            self.root = v # v becomes root
        elif u == u.p.left: # when u is left child
            u.p.left = v # set u's parent's left child to v
        else:               # when u is right child
            u.p.right = v # set u's parent's right child to v
        v.p = u.p # set v's parent equal to u's parent
        
        # updating v's children is the responsibility of
        # the calling function 
    
    ''' DELETING '''
    
    # Case 1: left child is NIL
        # Make note of z's original color
        # Call transplant on z (node to delete), and x (z's right child)
        # Call fixup on node x to recolor
    # Case 2: right child is NIL
        # Make note of z's original color
        # Call transplant on z (node to delete), and x (z's left child)
        # Call fixup
    # Case 3: no child is NIL
        # Find minimum in subtree (successor) and call it y
        # Two subcases: y is direct child of z, or not
        # See code below
    
    def _rbDelete(self, node, key):
        # Check if key exists
        z = self.nil
        while node != self.nil:
            if node.key == key:
                z = node
                break
            elif node.key > key:
                node = node.left
            else:
                node = node.right
        if z == self.nil:
            print("No such value in tree")
            return 
        
        # Delete key
        y = z
        yOrigColor = y.color # store original color of 'y' to determine if fixup operation is needed later
        if z.left == self.nil: # z doesn't have a left child
            x = z.right
            self.rbTransplant(z, z.right) # call transplant on z, and z's right child
        elif z.right == self.nil: # z doesn't have a right child
            x = z.left
            self.rbTransplant(z, z.left) # call transplant on z, and z's left child
        else: # z has two children
            y = self.treeMin(z.right) # find inorder successor to replace z
            yOrigColor = y.color
            x = y.right
            # if y is a direct child of z, we set x's parent to y
            if y.p == z:
                x.p = y
            # otherwise, y lies further in z's right subtree, and we have to move
            # y into z's place
            else:
                self.rbTransplant(y, y.right) # replaces y with its right child
                y.right = z.right # y's right child is set to z's right child
                y.right.p = y # parent of y's right child is set to y
            # after either sub-case...
            self.rbTransplant(z, y) # replace z with y
            y.left = z.left # y's left child set to z's left child
            y.left.p = y # parent of y's left child set to y
            y.color = z.color # y takes on color z
        if yOrigColor == Color.BLACK:
            # fixup if y had black color originally
            # since removing a black node can violate
            # the red-black tree properties
            self.rbDeleteFixup(x)
    
    def rbDelete(self, key):
        self._rbDelete(self.root, key)
    
    def rbDeleteFixup(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.p.left:
                w = x.p.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.p.color = Color.RED
                    self.leftRotate(x.p)
                    w = x.p.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.p
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.rightRotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.leftRotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.p.color = Color.RED
                    self.rightRotate(x.p)
                    w = x.p.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.p
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self.leftRotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.rightRotate(x.p)
                    x = self.root
        x.color = Color.BLACK
    
    def _printTree(self, node, level):
        if node is None:
            return
        self._printTree(node.right, level + 1)
        color = ''
        if node.color == Color.RED:
            color = '.R'
        else:
            if node.key == self.nil:
                pass
            if node != self.nil:
                color = '.B'
        if node != self.nil:
            print('    ' * level + str(node) + color)
        if node == self.nil:
            print('     ' * level)
        self._printTree(node.left, level + 1)

    def _printTreeWithNil(self, node, level):
        if node is None:
            return
        self._printTreeWithNil(node.right, level + 1)
        color = 'R' if node.color == Color.RED else 'B'
        print('    ' * level + str(node) + '-' + color)
        self._printTreeWithNil(node.left, level + 1)
    
    def printTree(self):
        self._printTree(self.root, 0)
    
    def printTreeWithNil(self):
        self._printTreeWithNil(self.root, 0)      
    
def main():
    print("Let 'R' denote a red note")
    print("Let 'B' denote a black node")
    print()
    print("Tree structure after inserting 5, 10, 2, respectively:")
    rb = RedBlackTree()
    rb.rbInsert(5)
    rb.rbInsert(10)
    rb.rbInsert(2)
    rb.printTree()
    print("Tree structure after inserting 12:")
    rb.rbInsert(12)
    rb.printTree()
    print("Tree structure after inserting 13 (left-rotate):")
    rb.rbInsert(13)
    rb.printTree()
    print("Tree structure after inserting 3:")
    rb.rbInsert(3)
    rb.printTree()
    print("Tree structure after inserting 4 (right-rotate):")
    rb.rbInsert(4)
    rb.printTree()
    print("Tree structure after deleting root:")
    rb.rbDelete(5)
    rb.printTree()
    print("Tree structure after deleting 12:")
    rb.rbDelete(12)
    rb.printTree()
    print()
    print("Trying to delete node that doesn't exist...")
    rb.rbDelete(88)
    print()
    print("Printing tree structure from textbook:")
    print("Insertion sequence: 26, 41, 17, 21, 14, 47, 30, 28, 38, 19, 23, 10, 16, 15, 20, 35, 39, 12, 7, 3")
    rb1 = RedBlackTree()
    rb1.rbInsert(26)
    rb1.rbInsert(41)
    rb1.rbInsert(17)
    rb1.rbInsert(21)
    rb1.rbInsert(14)
    rb1.rbInsert(47)
    rb1.rbInsert(30)
    rb1.rbInsert(28)
    rb1.rbInsert(38)
    rb1.rbInsert(19)
    rb1.rbInsert(23)
    rb1.rbInsert(10)
    rb1.rbInsert(16)
    rb1.rbInsert(15)
    rb1.rbInsert(20)
    rb1.rbInsert(35)
    rb1.rbInsert(39)
    rb1.rbInsert(12)
    rb1.rbInsert(7)
    rb1.rbInsert(3)
    rb1.printTree()
    
if __name__ == '__main__':
    main()
    
    
    
                
                    
                