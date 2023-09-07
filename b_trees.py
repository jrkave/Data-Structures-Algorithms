# B-Trees Implementation and Methods

class Node(object):
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree(object):
    def __init__(self, t):
        self.root = Node(True)
        self.t = t
    
    ''' SEARCHING '''

    # PARAMETERS
    # 'key' - key to search for
    # 'node' - allows for recursive calling on tree
    def searchBTree(self, key, node=None):
        # if node is not specified, start at root
        node = self.root if node == None else node
        
        i = 0
        # iterate through each key in the node, continuing while
        # the key we're searching for is greater than the node's keys
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        # found key at node
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
        # key is not in tree
        elif node.leaf:
            return None
        # search child node
        else:
            # 'i' helps to decide which subtree we should traverse next
            return self.searchBTree(key, node.children[i])
    
    ''' SPLITTING AND INSERTING NODES '''

    # PARAMETERS: 
    # 'x' - non-full internal node whose child at index 'i' is full
    # 'i' - index of full child
    # splits the child in two and adjusts x so that it has an additional child
    def splitChild(self, x, i):
        t = self.t # t is the min degree of the b-tree
        y = x.children[i] # y is full child to split
        z = Node(y.leaf) # make new node to hold half of keys
        x.children.insert(i+1, z) 
        x.keys.insert(i, y.keys[t-1]) # the median key of y is moved up to x

        # redistribute keys of z and y
        z.keys = y.keys[t:] 
        y.keys = y.keys[:t-1] 
        
        # check if y is a leaf node
        # if not, redistribute children
        if not y.leaf: 
            # split the children of the node y between nodes y and z
            # first half stay with y, second half go to z
            z.children = y.children[t:] 
            y.children = y.children[:t] 
    
    # PARAMETERS
    # 'k' - value to insert
    def insert(self, k):
        t = self.t # t is the min degree of the b-tree
        root = self.root # root of the b-tree
        
        # check if root is full (i.e. it has 2t-1 keys)
        if len(root.keys) == (2*t) - 1:
            newRoot = Node() # create empty node 
            self.root = newRoot # set tree's root to new node
            newRoot.children.insert(0, root) # add old root as child of new root
            self.splitChild(newRoot, 0) # split old root into two nodes
            self.insertNonFull(newRoot, k) # call insertNonFull with new root
        else:
            self.insertNonFull(root, k) # if root is not full, call insertNonFull with current root
    
    # PARAMETERS:
    # 'x' is a non-full node we're inserting into
    # 'k' is value we're inserting
    def insertNonFull(self, x, k):
        t = self.t # t is the min degree of the b-tree
        i = len(x.keys) - 1 # index of last key in node x
        
        # if x is a leaf, k is inserted directly into x.keys
        if x.leaf:
            x.keys.append(None) # add None key to end of keys as placeholder
            # move keys greater than k one position to the right
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k # insert new key at correct position
        # if x is not a leaf, k is inserted into the appropriate child of x
        else:
            # find the child that is going to have the new key
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1 # increment i to point to the appropriate child of 'x' into which k should be inserted
            # if the found child is full
            if len(x.children[i].keys) == (2*t)-1:
                self.splitChild(x, i) # split the child
                if k > x.keys[i]: # if k is greater than the new key moved up to 'x' during the split,
                    i += 1 # increment i to point to new child that should contain k
            self.insertNonFull(x.children[i], k) # call insertNonFull recursively on the child
        
    ''' PRINTING '''
    
    def _printTree(self, node, indent=0):
        # print the node keys with appropriate indentation
        print(' ' * indent, node.keys)

        # if this node isn't a leaf, print its children
        if not node.leaf:
            for child in node.children:
                self._printTree(child, indent + 4)

    def printTree(self):
        self._printTree(self.root)
    
def main():
    # Create tree
    tree = BTree(3)
    # Set properties of root
    tree.root.keys = ['G', 'M', 'P', 'X'] 
    tree.root.leaf = False 
    # Create and set properties of child nodes
    child0 = Node(True)
    child0.keys = ['A', 'C', 'D', 'E']
    child1 = Node(True)
    child1.keys = ['J', 'K']
    child2 = Node(True)
    child2.keys = ['N', 'O']
    child3 = Node(True)
    child3.keys = ['R', 'S', 'T', 'U', 'V']
    child4 = Node(True)
    child4.keys = ['Y', 'Z']
    # Set root's children
    tree.root.children = [child0, child1, child2, child3, child4]
    
    # Printing
    print("Original tree structure: ")
    print()
    tree.printTree()
    print()
    print("Tree structure after inserting 'B':")
    print()
    tree.insert('B')
    tree.printTree()
    print()
    print("Tree structure after inserting 'Q':")
    print()
    tree.insert('Q')
    tree.printTree()
    print()
    print("Tree structure after inserting 'L':")
    print()
    tree.insert('L')
    tree.printTree()
    print()
    print("Tree structure after inserting 'F':")
    print()
    tree.insert('F')
    tree.printTree()
    print()
    
if __name__ == '__main__':
    main()
    
        