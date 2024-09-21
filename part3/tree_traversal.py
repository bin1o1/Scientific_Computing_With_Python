'''Program to construct BST and perform an in-order traversal.'''

class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

class BinarySearchTree:

    def __init__(self):
        self.root = None            #when the object BinarySearchTree is created, root node is assigned to None.

    def _insert(self, node, key):           
        if node is None:            #if the given node is empty, then makes a TreeNode object in that node with the key provided.
            return TreeNode(key)

        if key < node.key:          #if the present node has key greater than the node that needs to be inserted, then we try to insert the key into the left sub node, and use recursion till the suitable node is found.
            node.left = self._insert(node.left, key)

        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node         #if the key is equal to the key of an already existing node, then that node is returned.

    def insert(self, key):          #takes a number to insert, then inserts the number into the required node.
        self.root = self._insert(self.root, key)
        
    def _search(self, node, key):
        if node is None or node.key == key:         #if there's no node or if the node key matches the required key we return the node
            return node
        if key < node.key:      #if the required key is smaller than the node key then we search to the left sub node, otherwise the right subnode.
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def search(self, key):      #function to search the required node with the given key 
        return self._search(self.root, key)

    def _delete(self, node, key):
        if node is None:            #if there's no node then we return the None
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)      #functions to find the right node
        else:           #if the key matches the node key
            if node.left is None:       #if the subnode to the left is none, we return the right node
                return node.right
            elif node.right is None:        #elif the subnode to the right is none, we return the left node.
                return node.left   
            
            node.key = self._min_value(node.right)          #finds the node key with the minimum value through the right node and assigns it the present node
            node.right = self._delete(node.right, node.key)         #eletes the node with the minimum value that we just copied 
        
        return node

    def delete(self, key):          #function to delete the node with the given key
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key         #returns the node key with the minimum value for a given branch

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80, 30]

for node in nodes:
    bst.insert(node)

print('Search for 80:', bst.search(80))

print("Inorder traversal:", bst.inorder_traversal())

bst.delete(40)

print("Search for 40:", bst.search(40))
print('Inorder traversal after deleting 40:', bst.inorder_traversal())