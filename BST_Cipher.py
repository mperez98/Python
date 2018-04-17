#  File: BST_Cipher.py

#  Description: Encipher a Message with Binary Trees

#  Student Name: Samuel Gutierrez

#  Student UT EID: sfg384

#  Partner Name: Mathew Perez

#  Partner UT EID: mjp3457

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: April 13, 2018

#  Date Last Modified: April 14, 2018

class Node(object):
  def __init__(self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None

    encrypt_str = self.asch_character(encrypt_str)
    for x in encrypt_str:
      self.insert(x)

  # search for a node with a key
  def search_repeats (self, key):
    current = self.root
    while (current != None) and (current.data != key):
      if (key < current.data):
        current = current.lchild
      else:
        current = current.rchild
    a = current

    if (current == None):
      return False
    else:
      return True

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    if (self.search_repeats(ch) == True):
      return 
    new_node = Node (ch)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (ch < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (ch < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, key):
    string = ''
    key = ord(key)
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lchild
        string += '<'
      else:
        current = current.rchild
        string += '>'
      
    if current == None:
      return ''
    elif current == self.root:
      return '*'
    else:
      return string

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current = self.root
    #a = st.split("!")
    
    if (current == None):
      return ""

    for i in st:

      if i == "<":
        current = current.lchild
      elif i == ">":
        current = current.rchild

    if (current == None):
      return ""
    else:
      string = chr(current.data)
    return string

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    string = ''
    st = st.lower()
    for x in st:
      if x.isalpha() or x.isspace(): 
        string += self.search(x) + '!'
    string = string[0:-1]
    return string

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    st = st.split('!')
    string = ''
    for x in st:
      string += str(self.traverse(x))
    return string
  

  def asch_character(self, message):
    enc_lst = []
    message = message.lower()
    for x in message:
      if x.isalpha() or x.isspace(): 
        enc_lst.append(ord(x))
    return enc_lst

def main():
    print()
    user_key = input("Enter encryption key: ")
    newTree = Tree(user_key)
    print()

    user_str1 = input("Enter string to be encrypted: ")
    enc_str = newTree.encrypt(user_str1)
    print("Encrypted string:", enc_str)
    print()

    user_str2 = input("Enter string to be decrypted: ")
    dec_str = newTree.decrypt(user_str2)
    print("Decrypted string:", dec_str)
    print()    
    
main()
