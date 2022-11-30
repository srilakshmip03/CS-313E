#  File: BST_Cipher.py

#  Description: encryption and decryption using a bst

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID: sp49694

#  Partner Name: Rin Chiang

#  Partner UT EID: ksc2495

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 11/10/22

#  Date Last Modified: 11/11/2022

import sys

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

  def __str__ (self):
    return str(self.data)

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character, drop that character.
  def __init__ (self, encrypt_str):
    stg = clean_string(encrypt_str).lower()
    self.root = None

    # get rid of extraneous characters
    stg_lst = list(stg)
    for char in stg_lst:
      self.insert(char)

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert(self, ch):
    # create the node with data to insert
    node = Node(ch)  

    # if the tree is empty, the new node is the root
    if self.root == None:
      self.root = node
      return
    
    # if not, find spot for node to go
    else:
      current = self.root
      parent = self.root
      data = ch

      # go down tree while as long as there are nodes available
      while (current != None):
        parent = current

        # each of these check what direction to go in
        if  data == current.data:
          return 
        elif (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # insertion point found, insert node
      if (data < parent.data):
        parent.lchild = node
      else:
        parent.rchild = node

    return


  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    result = ""

    data = ch
    current = self.root

    # if character is root, return asterisk
    if self.root.data == ch:
      result = "*"
      return result

    # non-root
    else:
      # go down tree, but add directions to result
      while (current != None):
        if data < current.data:
          current = current.lchild
          result += "<"
        elif data > current.data:
          current = current.rchild
          result += ">"
        else:
          return result
      
      # final statement to catch extra cases
    return result

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
        current = self.root
        string = st
        while (len(string) > 0) and (current != None):
            if string[0] == '*':
                return current.data
            elif string[0] == '<':
                current = current.lchild
                string = string[1:]
            elif string[0] == '>':
                current = current.rchild
                string = string[1:]
        if (current == None):
            return ''
        else: 
            return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    string = st.lower()
    estring = ''
    for ch in string:
      if (ch == ' ') or (97 <= ord(ch) <= 122):
        estring += self.search(ch) + '!'
    return estring[:-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    slist = st.split('!')
    dstring = ''
    for s in slist:
        dstring += self.traverse(s)
    return dstring

# helper function to remove extraneous characters
# input is the encrypt string
# output is cleaned string
def clean_string(encrypt_str):
  temp = list(encrypt_str)
  result = []
  for char in temp:
    if (char.isalpha()) or (char == " "):
      result.append(char)

  result = "".join(result)
  return result

def main():
  # read encrypt string
  line = sys.stdin.readline()
  encrypt_str = line.strip()

  # create a Tree object
  the_tree = Tree (encrypt_str)

  # read string to be encrypted
  line = sys.stdin.readline()
  str_to_encode = line.strip()

  # print the encryption
  print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
  line = sys.stdin.readline()
  str_to_decode = line.strip()
  
  # print the decryption
  print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
  main()