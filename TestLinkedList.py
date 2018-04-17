#  File: TestLinkedList.py

#  Description: This program modifies and adds functionality to the Linked List class.

#  Student Name: Mathew Perez

#  Student UT EID: mjp3457

#  Partner Name: Samuel F. Gutierrez

#  Partner UT EID: sfg384

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 03/26/2018

#  Date Last Modified: 03/30/2018

# create Link class
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__ (self):
    return str(self.data)

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # get number of links
  def get_num_links (self):
    linkCount = 0
    current = self.first
    if (current == None):
      return 0

    while (current != None):
      linkCount += 1
      current = current.next

    return linkCount

  # add an item at the beginning of the list
  def insert_first (self, item):
    newLink = Link(item)
    newLink.next = self.first
    self.first = newLink

  # add an item at the end of a list
  def insert_last (self, item):
    newLink = Link(item)
    current = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  # add an item in an ordered list in ascending order
  def insert_in_order (self, item):
    newLink = Link(item)
    current = self.first
    previous = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.data < item):
      previous = current
      current = current.next
      if (current == None):
        self.insert_last(item)
        return
      

    if (current == self.first):
      newLink.next = self.first
      self.first = newLink
      return
    elif (current.data >= item):
      previous.next = newLink
      newLink.next = current

  # search in an unordered list, return None if not found
  def find_unordered (self, item):
    current = self.first
    if (current == None):
      return None

    while (current.data != item):
      if (current.next == None):
        return None
      else:
        current = current.next 

    return current

  # search in an ordered list, return None if not found
  def find_ordered (self, item):
    current = self.first 
    if (current == None):
      return None

    if (item < current.data):
      return None

    while (item > current.data):
      if (current.next == None):
        return None
      else:
        current = current.next

    if (current.data != item):
      return None
    return current.data

  # delete and return link from an unordered list or None if not found
  def delete_link (self, item):
    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != item):
      if (current.next == None):
        return None
      else:
        previous = current 
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  # string representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    if (self.first == None):
      return ""
    output_str = ""
    place_count = 0
    current = self.first

    while (current != None):
      if (place_count < 10):
        output_str += str(current.data) + "  "
        place_count += 1
      elif (place_count == 10):
        output_str += "\n" + str(current.data) + "  "
        place_count = 0
        place_count += 1
      current = current.next
    return output_str

  # copy the contents of a list and return new list
  def copy_list (self):
    current = self.first
    if (current == None):
      return None
    else:
      copyLst = LinkedList()
      while (current != None):
        copyLst.insert_last (current.data)
        current = current.next
    return copyLst

  def reverse_list (self):
    current = self.first
    if (current == None):
      return None
    else:
      revLst = LinkedList()
      while (current != None):
        revLst.insert_first (current.data)
        current = current.next
    return revLst    

  def sort_list (self):
    current = self.first
    if (current == None):
      return None
    else:
      srtLst = LinkedList()
      while (current != None):
        srtLst.insert_in_order (current.data)
        current = current.next

    return srtLst

  def is_sorted (self):
    current  = self.first
    previous = self.first
    if (current == None):
      return True
    while (current != None):
      if (current.data < previous.data):
        return False
      elif (previous.data <= current.data): 
        previous = current
        current = current.next
    return True

  def is_empty (self):
    return (self.first == None)

  def merge_list (self, other):
    current1 = self.first
    current2 = other.first

    if (self.first == None):
      return other
    elif (other.first == None):
      return self
    else:
      mrgLst = LinkedList()
      while (current1 != None):
        mrgLst.insert_in_order(current1.data)
        current1 = current1.next

      while (current2 != None):
        mrgLst.insert_in_order(current2.data)
        current2 = current2.next

    return mrgLst

  def is_equal (self, other):
    current1 = self.first
    current2 = other.first
    if (self.get_num_links() != other.get_num_links()):
      return False

    while (current1 != None):
      if (current1.data != current2.data):
        return False
      current2 = current2.next
      current1 = current1.next

    return True

  def remove_duplicates (self):
    current = self.first
    if (current == None):
      return None

    nodupl = LinkedList()
    duplicates = set()
    while (current != None):
      if (current.data not in duplicates):
        nodupl.insert_last(current.data)
        duplicates.add(current.data)
      current = current.next

    return nodupl

def main():
  print()
  # Test methods insert_first() and __str__() by adding more than 10 items to a list and printing it.
  LL1 = LinkedList()
  for i in range (13):
    LL1.insert_first(i)
  print(LL1)

  # Test method insert_last()
  print()
  LL2 = LinkedList()
  for i in range (13):
    LL2.insert_last(i)
  print(LL2)

  # Test method insert_in_order()
  print()
  LL3 = LinkedList()
  for i in range (2,7):
    LL3.insert_last(i)
  LL3.insert_in_order(3)
  print(LL3)

  # Test method get_num_links()
  print()
  LL4 = LinkedList()
  for i in range (6):
    LL4.insert_last(i)
  print(LL4)
  print(LL4.get_num_links())

  # Test method find_unordered()
  # Consider two cases - item is there, item is not there
  print()
  LL5 = LinkedList()
  LL5.insert_last(6)
  LL5.insert_last(3)
  LL5.insert_last(9)
  LL5.insert_last(1)
  print(LL5)

  print(LL5.find_unordered(9))
  print(LL5.find_unordered(2))  

  # Test method find_ordered()
  # Consider two cases - item is there, item is not there
  print()
  LL6 = LinkedList()
  for i in range (2,7):
    LL6.insert_last(i)
  print(LL6)
  print(LL6.find_ordered(1))
  print(LL6.find_ordered(9))
  print(LL6.find_ordered(5))

  # Test method delete_link()
  # Consider two cases - item is there, item is not there
  print()
  print(LL2)
  print(LL2.delete_link(3))
  print(LL2)
  print(LL2.delete_link(16))

  # Test method copy_list()
  print()
  print(LL2)
  print(LL2.copy_list())

  # Test method reverse_list()
  print()
  print(LL2)
  print(LL2.reverse_list())

  # Test method sort_list()
  print()
  print(LL5)
  print(LL5.sort_list())

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  LL7 = LinkedList()
  LL7.insert_last(6)
  LL7.insert_last(1)
  LL7.insert_last(8)
  LL7.insert_last(4)

  LL8 = LinkedList()
  for i in range (5):
    LL8.insert_last(i)
  LL8.insert_in_order(4)
  
  print()
  print(LL8)
  print(LL8.is_sorted())
  print(LL7)
  print(LL7.is_sorted())

  # Test method is_empty()
  print()
  LL9 = LinkedList()
  print(LL9)
  print(LL9.is_empty())
  print(LL8)
  print(LL8.is_empty())

  # Test method merge_list()
  print()
  print(LL7)
  print(LL8)
  print(LL7.merge_list(LL8))

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print()
  LL10 = LL8.copy_list()
  LL11 = LL7.copy_list()
  print(LL10)
  print(LL11)
  print(LL10.is_equal(LL11))
  print(LL7)
  print(LL11)
  print(LL7.is_equal(LL11))

  # Test remove_duplicates()
  print()
  LL12 = LL7.merge_list(LL8)
  print(LL12)
  print(LL12.remove_duplicates())


if __name__ == "__main__":
  main()
