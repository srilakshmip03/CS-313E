#  File: TestBinaryTree.py

#  Description: A19; test different binary search tree functions

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID: sp49694

#  Partner Name: Rin Chiang

#  Partner UT EID: ksc2495

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 11/10/2022

#  Date Last Modified: 11/14/2022

import sys

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    def __init__ (self):
        self.root = None

    # Search for a node with the key
    def search (self, key):
        current = self.root
        while ((current != None) and (current.data != key)):
            if (key < current.data):
                current = current.lchild
            else:
                current = current.rchild
        return current

    # Insert a node in the tree
    def insert (self, val):
        newNode = Node (val)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (val < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            if (val < parent.data):
                parent.lchild = newNode
            else:
                parent.rchild = newNode

    # Returns true if two binary trees are similar
    def is_similar (self, pTree):
        return self.is_similar_helper(self.root, pTree.root)

    # recursive helper function for is_similar
    def is_similar_helper(self, aNode, pNode):
        # if both are empty, they're similar
        if (aNode == None) and (pNode == None):
            return True
        
        # if one is empty and one isn't they're not similar
        elif (aNode == None) or (pNode == None):
            return False

        # if the roots are the same, recurse to see if each each left and right subtree is similar.
        elif (aNode.data == pNode.data):
            return self.is_similar_helper(aNode.lchild, pNode.lchild) and self.is_similar_helper(aNode.rchild, pNode.rchild)
        
        # if the roots are different, the trees are different
        else: 
            return False

    # Returns a list of nodes at a given level from left to right
    def get_level (self, level):
        lst = []
        self.get_level_helper(self.root, level, lst)
        return lst
    
    # recursive helper for get_level
    def get_level_helper(self, node, level, lst):
        if (node != None):
            if (level == 0):
                lst.append(node)
            else: 
                self.get_level_helper(node.lchild, level - 1, lst) 
                self.get_level_helper(node.rchild, level - 1, lst)

    # Returns the height of the tree
    def get_height (self):
        return self.get_height_helper(self.root)

    # recursive helper for height
    def get_height_helper(self, node):
        if (node == None):
            return 0
        else: 
            return 1 + max(self.get_height_helper(node.lchild), self.get_height_helper(node.rchild))

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        return self.num_nodes_helper(self.root)
    
    # recursive helper for num_nodes
    def num_nodes_helper(self, node):
        if (node == None):
            return 0
        else: 
            return 1 + self.num_nodes_helper(node.lchild) + self.num_nodes_helper(node.rchild)

def main():
    # Create 3 trees, 2 are the same and 3rd is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))

    tree1 = Tree()
    for num in tree1_input:
        tree1.insert(num)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))

    tree2 = Tree()
    for num in tree2_input:
        tree2.insert(num)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))

    tree3 = Tree()
    for num in tree3_input:
        tree3.insert(num)

    # Test your method is_similar()
    print(f'Tree 1 and Tree 2 is_similar: {tree1.is_similar(tree2)}')
    print(f'Tree 1 and Tree 3 is_similar: {tree1.is_similar(tree3)}')

    # Print the various levels of two of the trees that are different
    print(f'Tree 1 level 2: {tree1.get_level(4)}')
    print(f'Tree 3 level 2: {tree3.get_level(4)}')

    # Get the height of the two trees that are different
    print(f'Tree 1 height: {tree1.get_height()}')
    print(f'Tree 3 height: {tree3.get_height()}')

    # Get the total number of nodes a binary search tree
    print(f'Tree 1 num_nodes: {tree1.num_nodes()}')
    print(f'Tree 3 num_nodes: {tree3.num_nodes()}')

if __name__ == "__main__":
  main()