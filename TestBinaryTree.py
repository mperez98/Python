#  File: TestBinaryTree.py

#  Description: This program adds functionality to the Node and Tree classes for a Binary Search Tree.

#  Student Name: Mathew Perez

#  Student UT EID: mjp3457

#  Partner Name: Samuel F. Gutierrez

#  Partner UT EID: sfg384

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 04/12/2018

#  Date Last Modified: 

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None



  # determine if two binary trees are similar
  def is_similar (self, pNode):
    return self.is_similar_helper (self.root, pNode.root)
  
  # Returns true if two binary trees are similar
  def is_similar_helper (self, aNode1, aNode2):
    if (aNode1 == None) and (aNode2 == None):
      return True 

    elif (aNode1 != None) and (aNode2 != None):
      a = aNode1.data == aNode2.data
      b = self.is_similar_helper (aNode1.lchild, aNode2.lchild)
      c = self.is_similar_helper (aNode1.rchild, aNode2.rchild)

      return a and b and c

    else:
      return False
    
  # insert a node in a tree
  def insert (self, val):
    new_node = Node (val)

    if (self.root == None):
      self.root = new_node
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
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # Prints out all nodes at the given level
  def print_level (self, level): 
    if (self.root == None):
      return
    else:
      string = ''
      return self.print_real_level(self.root, level, 1, string)

  def print_real_level(self, node, level, current_level, string):
    if node == None:
      return ' '
    elif current_level == level:
      return str(node.data) + ' '
    else:
      string += str(self.print_real_level(node.lchild, level, current_level + 1, string)) + str(self.print_real_level( node.rchild, level, current_level + 1, string))
      return string

  # Returns the height of the tree
  def get_height (self):
    if self.root == None:
      return 0
    else:
      return self.get_real_height(self.root)
      
  # returns value height of the tree
  def get_real_height(self, node):
    if node == None:
      return 0
    else:
      return 1 + max(self.get_real_height(node.lchild),self.get_real_height(node.rchild))


  # calls the function that Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    if self.root == None:
      return 0
    else:
      return 1 + self.num_real_nodes(self.root.lchild) + self.num_real_nodes(self.root.rchild)
  # return the number of nodes in the subtree
  def num_real_nodes(self, node):
    if node == None:
      return 0
    else:
      return 1 + (self.num_real_nodes(node.lchild) + self.num_real_nodes(node.rchild))
    
def main():
# Create three trees - two are the same and the third is different
  tree1 = Tree()
  tree1.insert(50)
  tree1.insert(30)
  tree1.insert(70)
  tree1.insert(10)
  tree1.insert(40)
  tree1.insert(60)
  tree1.insert(80)
  tree1.insert(7)
  tree1.insert(25)
  tree1.insert(38)
  tree1.insert(47)
  tree1.insert(58)
  tree1.insert(65)
  tree1.insert(77)
  tree1.insert(96)

  tree2 = Tree()
  tree2.insert(50)
  tree2.insert(30)
  tree2.insert(70)
  tree2.insert(10)
  tree2.insert(40)
  tree2.insert(60)
  tree2.insert(80)
  tree2.insert(7)
  tree2.insert(25)
  tree2.insert(38)
  tree2.insert(47)
  tree2.insert(58)
  tree2.insert(65)
  tree2.insert(77)
  tree2.insert(96)

  tree3 = Tree()
  tree3.insert(50)
  tree3.insert(30)
  tree3.insert(70)
  tree3.insert(10)
  tree3.insert(40)
  tree3.insert(60)
  tree3.insert(80)
  tree3.insert(7)
  tree3.insert(26)
  tree3.insert(37)
  tree3.insert(47)
  tree3.insert(58)
  tree3.insert(61)

  # Test your method is_similar()
  print("Test is_similar function")
  print("Test for similar trees")
  print(tree1.is_similar(tree2))
  print("Test for different trees")
  print(tree2.is_similar(tree3))
  print()

  # Print the various levels of two of the trees that are different
  print("Test print_level function for two different trees")
  print("Test Tree 1")
  print("level 1")
  print(tree2.print_level(1))   
  print("level 2")
  print(tree2.print_level(2))
  print("level 3")
  print(tree2.print_level(3))
  print("level 4")
  print(tree2.print_level(4))

  print()
  print("Test Tree 2")
  print("level 1")
  print(tree3.print_level(1))
  print("level 2")
  print(tree3.print_level(2))
  print("level 3")
  print(tree3.print_level(3))
  print("level 4")
  print(tree3.print_level(4))

  # Get the height of the two trees that are different
  print()
  print("Test get_height for two different trees")
  print("height of tree 1")
  print(tree1.get_height())
  print("height of tree 2")
  print(tree3.get_height())
  print()

  # Get the total number of nodes a binary search tree
  print("Test num_nodes for two different sized trees")
  print("Number of nodes in tree 1")
  print(tree1.num_nodes())
  print("Number of nodes in tree 2")
  print(tree3.num_nodes())
main()
