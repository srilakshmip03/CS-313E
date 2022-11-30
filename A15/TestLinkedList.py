#  File: TestLinkedList.py

#  Description: linked list exercises

#  Student Name: Srila Palanikumar

#  Student UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/31/2022

#  Date Last Modified: 11/1/2022


class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self) -> str:
    return str(self.data)

class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.first = None

  # get number of links 
  def get_num_links (self):
    # if empty, zero links
    if self.first == None:
      return 0

    # go through list and add 1 for every element that exists
    else:
      current = self.first
      counter = 1
      while current.next != None:
        current = current.next
        counter += 1
      
      return counter
  
  # from notes
  # add an item to the beginning of the list
  def insert_first (self, data):
    new_link = Link(data)
    new_link.next = self.first
    self.first = new_link

 # from notes
 # add an item to the end of the list
  def insert_last (self, data):
    new_link = Link (data)

    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

  # add an item in an ordered list in ascending order
  # assume that the list is already sorte
  def insert_in_order (self, data): 
    new_link = Link(data)
    previous = self.first
    current = self.first

    # account for if link has lowest value or is being put into empty list
    if (current == None):
        self.insert_first(data)
        return
    if (data < current.data):
        self.insert_first(data)
        return
    
    # if neither of those, traverse list until you find an element smaller than
    # given data - that's the spot to insert it into.
    while (current.data <= data):
      # special case: last item in list
      if (current.next == None):
          self.insert_last(data)
          return
      else:
          # traversal
          previous = current
          current = current.next
    
    # insertion
    previous.next = new_link
    new_link.next = current

  # from notes
  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
    current = self.first

    if (current == None):
      return None
    else:
      while (current.data != data):
        if (current.next == None):
          return None
        else:
          current = current.next

      return current

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    current = self.first

    if (current == None):
      return None

    while current.data != data:
      if current.next == None:
        return None
      elif current.data > data:
        return None
      else:
        current = current.next
    
    return current

  # from notes
  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = current.next
    else:
      previous.next = current.next

    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    result = ""
    current = self.first
    counter = 0

    if current == None:
      return ""

    else:
      # fencepost method adding data and a corresponding space
      while current.next != None:
        result += (str(current.data) + "  ")
        counter += 1

        # every ten, start new line
        if counter % 10 == 0:
          result += "\n"
    
        current = current.next
   
    # fencepost end
    result += str(current.data)
    return result
        
  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
    result = LinkedList()
    current = self.first
    size = self.get_num_links()

    if current == None:
      return None

    # insert each element of self into result
    else:
      for i in range(size):
        result.insert_last(current.data)
        current = current.next

    return result

  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self):
    result = LinkedList()
    current = self.first
    size = self.get_num_links()

    if current == None:
      return None

    # same as copy but add each new elem at beginning to get backwards
    else:
      for i in range(size):
        result.insert_first(current.data)
        current = current.next

    return result 

  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 
    result = LinkedList()
    current = self.first
    size = self.get_num_links()

    if current == None:
      return None

    # add each element to what exists in order.
    else:
      for i in range(size):
        result.insert_in_order(current.data)
        current = current.next

    return result

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first
    size = self.get_num_links()

    if current == None:
      return True

    # if each element is smaller than the next, list is in ascending order
    else:
      for i in range(size - 1):
        if current.data > current.next.data:
          return False
        current = current.next

    return True


  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    return self.first == None

 # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
    sself = self.get_num_links()
    sother = other.get_num_links()
    size = min(sself, sother)

    # the larger of the two given linked lists will be the base to insert 
    # elems into. the smaller is basically a container of links to insert
    if sself > sother:
      result = self.copy_list()
      inserts = other.copy_list()
    else:
      inserts = self.copy_list()
      result = other.copy_list()

    if self.is_empty() and other.is_empty():
      return None

    # insert links from smaller list in order into larger list
    current = inserts.first
    for i in range(size):
      result.insert_in_order(current.data)
      current = current.next
    
    return result

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    curr_one = self.first
    curr_two = other.first
    size = min(self.get_num_links(), other.get_num_links())
    result = False

    if curr_one == None and curr_two == None:
      return True

    # test item by item, break if something that is equal comes up
    else:
      for i in range(size):
        if curr_one.data == curr_two.data:
          result = True
          break
    
    return result

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
      result = self.copy_list()
      previous = result.first
      current = result.first
      memo = []

      while current != None:
        # if something is in the memo, it exists in the linked list
        # and is skipped
        if current.data in memo:
          current = current.next
          previous.next = current
        
        # if it's not in the memo, put it into the memo, and it's
        # added to the result list
        else:
          memo.append(current.data)
          previous = current
          current = current.next
          
      return result
      
  def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    print("Testing inserting first and string representation:")
    list_one = LinkedList()
    for i in range(15):
      list_one.insert_first(i)
    print(list_one)

    # Test method insert_last()
    print("Testing insertion at end:")
    list_two = LinkedList()
    for i in range (20, 40, 2):
      list_two.insert_last(i)
    print(list_two)

    # Test method insert_in_order()
    print("In order insertion:")
    list_two.insert_in_order(37)
    list_two.insert_in_order(21)
    list_two.insert_in_order(15)
    print(list_two)

    # Test method get_num_links()
    print("Testing getting number of links:")
    len_one = list_one.get_num_links()
    print(len_one)

    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 
    print("Testing unordered search:")
    list_four = LinkedList()
    list_four.insert_last(14)
    list_four.insert_last(17)
    list_four.insert_last(1)
    list_four.insert_last(30)

    unordered_one = list_four.find_unordered(72)
    unordered_two = list_four.find_unordered(17)

    print(unordered_one)
    print(unordered_two)


    # Test method find_ordered() 
    print("Testing ordered search:")

    # Consider two cases - data is there, data is not there 
    ordered_one = list_two.find_ordered(100)
    ordered_two = list_two.find_ordered(21)

    print(ordered_one)
    print(ordered_two)

    # Test method delete_link()
    print("Testing deleting a link and returning it:")

    # Consider two cases - data is there, data is not there 
    del_one = list_one.delete_link(100)
    del_two = list_one.delete_link(11)

    print(del_one)
    print(del_two)
    
    # Test method copy_list()
    print("Testing making copies:")
    print(list_one.copy_list())

    # Test method reverse_list()
    print("Testing reversing a list:")
    print(list_one.reverse_list())


    # Test method sort_list()
    print("Testing sorting the list:")
    sorted_list = list_four.sort_list()
    print(sorted_list)

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("Testing whether list is sorted: ")
    print("Expect false,", list_one.is_sorted())

    sorted_list = LinkedList()
    sorted_list.insert_first(0)
    sorted_list.insert_last(1)
    sorted_list.insert_last(2)
    sorted_list.insert_last(3)
    print("Expect true,", sorted_list.is_sorted())
    

    # Test method is_empty()
    print("Testing whether list is empty:")
    print("Expect false,",list_four.is_empty())
    empty_list = LinkedList()
    print("Expect true,", empty_list.is_empty())

    # Test method merge_list()
    print("list one:", list_one)
    print("list two:", list_two)
    merged = list_one.merge_list(list_two)
    print("merged:", merged)

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print("Testing unordered search:")
    print(list_one.is_equal(list_two))

    # Test remove_duplicates()
    print("Testing removing duplicates:")
    list_six = LinkedList()
    list_six.insert_last(6)
    list_six.insert_last(6)
    list_six.insert_last(7)
    list_six.insert_last(7)
    list_six.insert_last(7)

    removed = list_six.remove_duplicates()
    print(removed)


  if __name__ == "__main__":
    main()