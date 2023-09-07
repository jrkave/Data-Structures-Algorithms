# Binary Search Tree Implementation and Methods

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        # Check if current node's data is not 'None'
        if self.value:
            # If value is less than current node, it goes to the left
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    # Recursively insert on node.left
                    self.left.insert(value)
            # If value is greater than current node, it goes to the right 
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    # Recursively insert on node.right
                    self.right.insert(value)  
        # If current node's data is 'None', assign it with the value
        else:
            self.value = value
        
    def isBST(self):
        # Check if BST is empty
        if self.value:
            # Check properties of current node's children
            if self.left and self.left.value > self.value:
                print(f"Error found where value = {self.left.value}.")
                return False
            if self.right and self.right.value < self.value:
                print(f"Error found where value = {self.right.value}.")
                return False

            # Recursive check on children's nodes
            if self.left and not self.left.isBST():
                return False
            if self.right and not self.right.isBST():
                return False
        
        return True

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def insert(self, value):
        self.root.insert(value)
    
    def checkBST(self):
        if self.root is None:
            return True
        return self.root.isBST()
    
    # Print from right, to root, to left
    def _printTree(self, node, level):
        # Base case
        if node is None:
            return
        self._printTree(node.right, level + 1)
        print('    ' * level + str(node.value))
        self._printTree(node.left, level + 1)
    
    def printTree(self):
        self._printTree(self.root, 0)
    
def main():
    
    # Create Example 1 Tree (see beginning of file)
    bt1 = BinaryTree(16)
    bt1.insert(4)
    bt1.insert(3)
    bt1.insert(5)
    bt1.insert(18)
    bt1.insert(17)
    bt1.insert(20)

    # Create Example 2 Tree (see beginning of file)
    bt2 = BinaryTree(16)
    bt2.root.left = Node(4)
    bt2.root.left.left = Node(3)
    bt2.root.left.right = Node(2)
    bt2.root.right = Node(18)
    bt2.root.right.left = Node(17)
    bt2.root.right.right = Node(20)
   
    # Printing trees / results
    
    print()
    print("==== Example 1 Tree ====")
    print()
    print("Checking for BST validity...")
    if bt1.checkBST():
        print("No errors found.")
    print(f"Validity check output: {bt1.checkBST()}")
    print()
    print("Tree structure:")
    print()
    bt1.printTree()
    print()

    print("==== Example 2 Tree ====")
    print()
    print("Checking for BST validity...")
    print(f"Validity check output: {bt2.checkBST()}")
    print()
    print("Tree structure:")
    print()
    bt2.printTree()
    print()

if __name__ == '__main__':
    main()




