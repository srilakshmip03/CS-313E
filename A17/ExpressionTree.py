#  File: ExpressionTree.py

#  Description: A17; practice trees

#  Student Name: Rin Chiang

#  Student UT EID: ksc2495

#  Partner Name: Srilakshmi Palanikumar

#  Partner UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 11/04/2022

#  Date Last Modified: 11/07/2022

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild
    
    def __str__(self):
        if (isinstance(self.data, str)):
            return self.data
        elif (self.data % 1 == 0):
            return str(int(self.data))
        return str(self.data)

class Tree (object):
    def __init__ (self):
        self.root = Node()
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        exprlt = expr.split(' ')
        stk = Stack()
        current = self.root
        # traverse through tokens
        for token in exprlt: 
            # If the current token is a left parenthesis add a new node as the
            # left child of the current node. Push current node on the stack 
            # and make current node equal to the left child.
            if (token == '('):
                current.lChild = Node()
                stk.push(current)
                current = current.lChild
            # If the current token is an operator set the current node's data 
            # value to the operator. Push current node on the stack. Add a 
            # new node as the right child of the current node and make the 
            # current node equal to the right child.
            elif (token in operators):
                current.data = token
                stk.push(current)
                current.rChild = Node()
                current = current.rChild
            # If the current token is a right parenthesis make the current node
            # equal to the parent node by popping the stack if it is not empty.
            elif (token == ')'):
                if ( not stk.is_empty()):
                    current = stk.pop()            
            # If the current token is an operand, set the current node's data 
            # value to the operand and make the current node equal to the 
            # parent by popping the stack.
            else: 
                current.data = float(token)
                current = stk.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        token = aNode.data
        if (not aNode):
            return 0
        elif (token == '+'):
            return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
        elif (token == '-'):
            return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
        elif (token == '*'):
            return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
        elif (token == '/'):
            return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
        elif (token == '//'):
            return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
        elif (token == '%'):
            return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
        elif (token == '**'):
            return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        else: 
            return float(token)

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        string = ''
        if (aNode != None):
            string += str(aNode) + ' '
            string += self.pre_order(aNode.lChild)
            string += self.pre_order(aNode.rChild)
        return string

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        string = ''
        if (aNode != None):
            string += self.post_order(aNode.lChild)
            string += self.post_order(aNode.rChild)
            string += str(aNode) + ' '
        return string

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()