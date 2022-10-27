
#  File: Radix.py

#  Description: A radix sort algorithm to sort an array of integers

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/25/2022

#  Date Last Modified: 10/25/2022

import sys

numbers = []
for i in range(1, 10):
  numbers.append(str(i))

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

  # print queue, debugging purposes
  def rep (self):
    return self.queue

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  # create a list with queue objects, one per index (0-9, a-z) and one final
  queue_list = [0] * 38
  for i in range(len(queue_list)):
    queue_list[i] = Queue()

  # find the number of passes aka greatest number of digits
  most_digits = len(str(max(a, key=len)))

  # find longest string
  longest = a[0]
  for i in range(1, len(a)):
    if len(a[i]) > len(longest):
      longest = a[i]

  # pad strings
  add_to = len(longest)
  for i in range(len(a)):
    while len(a[i]) < add_to:
      a[i] += "-"

  # pass 0: all elements of array go into final queue
  for i in range(len(a)):
    queue_list[37].enqueue(a[i])

  pass_number = 1
  while pass_number <= most_digits:
    # set the current string to look at as the one at the front of the queue
    for i in range(queue_list[37].size()):
        curr = queue_list[37].dequeue()

        # set where to sort string by: search from end
        end = -1 * pass_number
        char = curr[end]
          
        # determine what queue to put the string into
        queue_into = 0
        if char in numbers:
          queue_into = int(char)
        elif char.isalpha():
          queue_into = ord(char) - 86
          
        # queue string into where it belongs
        queue_list[queue_into].enqueue(curr)

    # put everything into final queue for another pass
    for i in range(37):
      while not queue_list[i].is_empty():
        curr = queue_list[i].dequeue()
        queue_list[37].enqueue(curr)

    # increment pass value
    pass_number += 1

  # remove hyphens
  result = []
  for i in range(queue_list[37].size()):
    mod_string = queue_list[37].dequeue()
    result_string = mod_string.replace("-", "")
    result.append(result_string)
 
  return result

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append ((word))
    
  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    