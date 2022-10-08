#  File: Spiral.py

#  Description: Creates an anti-clockwise spiral inward of a number given,
#               then for the rest of the numbers given, find the sum of its adjacent numbers

#  Student Name: Annie Yu

#  Student UT EID: ay7273

#  Partner Name: Srilakshmi Palanikumar

#  Partner UT EID: sp46964

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: Aug. 31, 2022

#  Date Last Modified: Sept. 1, 2022

import sys
import math

# Input: dimensions of the spiral,
# an odd integer to indicate that # of rows and # of columns
# Output: a blank list of nested lists that includes # of rows and # of columns
def create_blank_grid(a):
  blank_grid = []
  
  for i in range(a):
    blank_grid.append([])
  for i in range(a):
    for j in range(a):
      blank_grid[i].append([])
  
  return blank_grid

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
  # if even, then add one
  if (n % 2) == 0:
    n += 1
    
  first_row = 0
  last_row = n - 1
  first_col = 0
  last_col = n - 1
  nums_in_counter = 0
  nums_out_counter = 0

  max_num = int(n ** 2)

  # make the blank grid to fill in with numbers
  grid = create_blank_grid(n)

  # fill in blank grid with numbers except for the center of the grid
  # center of grid is when first_row = last_row and first_col = last_col
  while first_row != last_row and first_col != last_col:
  
    # fill in first row except for the top right corner
    # always fill in till one last corner so the next set can be added
    # and the total size will be the dimensions added, or else the dimensions
    # of the spiral might be + 1 or - 1
    for i in range(last_col, first_col, -1):
      grid[first_row][i] = max_num
      max_num -= 1
      
    first_row += 1
  
    #  fill in first column down except for bottom left corner
    for i in range((first_row - 1), last_row):
      grid[i][first_col] = max_num
      max_num -= 1
      
    first_col += 1

    #  fill in last row except for bottom right corner
    for i in range((first_col - 1), last_col):
      grid[last_row][i] = max_num
      max_num -= 1
      
    last_row -= 1
    
    #  fill in last column except for top right corner (since already filled)
    for i in range((last_row + 1), (first_row - 1), -1):
      grid[i][last_col] = max_num
      max_num -= 1
      
    last_col -= 1

  # add 1 to the center of the spiral
  grid[last_row][last_col] = 1

  #return spiral
  return grid

# Input: the spiral created and the integer we want to find
# Output: returns the row and column of that integer within the spiral
def find_num (spiral, j): 
  col = -1
  row = -1

  # search each row and column for the integer wanted
  for i in spiral:
    row += 1
    if j in i:
      col = i.index(j)
      break
    
  # returns position of the integer and if not found col will remain -1  
  return [row, col]

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral_1, n):
  # find position of the integer specified 
  pos = find_num(spiral_1, n)

  row = pos[0]
  col = pos[1]
  sum = 0

  # if the integer is not found, find_num() will return a column of -1
  # which will return 0 in this funtion
  if col == -1:
    return 0
  
  # check for each position adjacent to the indicated number
  # if it exists, add it to the sum
  else:
    if col - 1 >= 0:
      sum += spiral_1[row][col - 1]
      
      if row - 1 >= 0:
        sum += spiral_1[row - 1][col - 1]
        
      if row + 1 < len(spiral_1):
        sum += spiral_1[row + 1][col - 1]

    if col + 1 < len(spiral_1[1]):
      sum += spiral_1[row][col + 1]

      if row + 1 < len(spiral_1):
        sum += spiral_1[row + 1][col + 1]

      if row - 1 >= 0:
        sum += spiral_1[row - 1][col + 1]

    if row + 1 < len(spiral_1):
        sum += spiral_1[row + 1][col]

    if row - 1 >= 0:
      sum +=spiral_1[row - 1][col]

    # returns the sum of adjacent numbers to the indicated number    
    return sum

def main():
  
  # read the input file
  dimension = sys.stdin.readline()
  dimension = dimension.strip()
  dimension = int(dimension)

  # create the spiral
  spiral = create_spiral(dimension)
  
  # add the adjacent numbers
  sum_total = []
  adjacent_nums = sys.stdin.readlines()

  for i in range(len(adjacent_nums)):
    adjacent_nums[i] = int(adjacent_nums[i].strip())
  
  for i in adjacent_nums:
    sum_total.append(sum_adjacent_numbers(spiral, i))

  # print the result
  for i in sum_total:
    print(i)

if __name__ == "__main__":
  main()
