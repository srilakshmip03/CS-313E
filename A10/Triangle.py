#  File: Triangle.py

#  Description: Types of search algorithms to find greatest path sum

#  Student Name: Srilakshmi Palanikumar

#  UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/07/2022

#  Date Last Modified: 10/11/2022

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
# Input: given grid of numbers
# Output: an integer representing the greates sum in the list
def brute_force(grid):
    # list to store all paths
    sums = []

    row = 0
    col = 0
    total = 0

    brute_helper(grid, sums, row, col, total)

    #return biggest in list of all
    return max(sums)

# Input: given grid, counters for each variable that incremements, running total
# Output: a list of all possible path sums
def brute_helper(grid, sums, row, col, total):
    hi = len(grid)

    # base case: add each sum to the empty list of sums when you get to bottom, return the result
    if row == hi:
        return (sums.append(total))
        
    #recursive case: if not at bottom, add and return each adjacent number
    else:
        total += grid[row][col]
        brute_helper(grid, sums, row + 1, col, total)
        brute_helper(grid, sums, row + 1, col + 1, total)

# returns the greatest path sum by finding the next row's largest adjacent number
# Input: given grid of numbers
# Output: integer representing a high path sum (not necessarily the highest)
def greedy (grid):
    hi = len(grid)
    total = 0
    row = 0
    col = 0

    # search rows until bottom of grid is reached
    for row in range(hi):

        # add the greater adjacent number
        to_add = max(grid[row][col], grid[row][col + 1])
        total += to_add
        
        # if next number is further down the grid than current, increment column
        if to_add == grid[row][col + 1]:
            col += 1
    
    return total

# returns the greatest path sum using recursion but without storing a list of all sums
# Input: given grid of integers
# Output: integer representing highest path sum
def divide_conquer(grid):
    # list to store all paths
    row = 0
    col = 0
    total = 0
    return divide_helper(grid, row, col, total)

# Input: given grid, counters for each variable that incremements, running total
# Output: a list of all possible path sums
def divide_helper(grid, row, col, total):
    hi = len(grid)

    # base case: when bottom of triangle is reached, 
    if row == hi:
        return total
    
    # recursive case: when current row is not bottom of triangle, add current element (which is highest adjacent)
    #                 to running total. then make current element be the higher of the two adjacent elems in next row
    #                 until bottom is reached.

    else:
        total += grid[row][col]
        return max(divide_helper(grid, row + 1, col, total), divide_helper(grid, row + 1, col + 1, total))

# returns the greatest path sum and the new grid using dynamic programming
# Input: given grid
# Output: integer representing the highest sum path
def dynamic_prog(grid):
    # initialize the new grid
    triangle = [[0 for i in range(len(grid))] for j in range(len(grid))]
    triangle[-1] = grid[-1]
    hi = len(grid) - 1

    # bottom up approach
    for i in reversed((range(hi))):
        # add old grid to new grid line by line
        triangle[i] = grid[i]
        # find the greater number to add to the current element
        for j in range(i + 1):
            if triangle[i + 1][j] > triangle[i + 1][j + 1]:
                to_add = triangle[i + 1][j]
            else:
                to_add = triangle[i + 1][j + 1]
    
            # add the greater number to the current element
            triangle[i][j] += to_add

    # the number at the very top will be a sum of all of the greatest numbers, aka the greatest path sum
    return triangle[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int (line)

    # create an empty grid with 0's
    grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
    for i in range (n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list (map (int, row))
        for j in range (len(row)):
            grid[i][j] = grid[i][j] + row[j]
    
    return grid 

def main ():
    # read triangular grid from file
    grid = read_file()

    '''
    # check that the grid was read in properly
    print (grid)
    '''
    
    # output greatest path from exhaustive search
    print("The greatest path sum through exhaustive search is")
    print(brute_force(grid))
    times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
    times = times / 10
    # print time taken using exhaustive search
    print("The time taken for exhaustive search in seconds is")
    print(times)

    # output greatest path from greedy approach
    print("The greatest path sum through greedy search is")
    print(greedy(grid))
    times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
    times = times / 10
    # print time taken using greedy approach
    print("The time taken through greedy search in seconds is")
    print(times)

    # output greatest path from divide-and-conquer approach
    print("The greatest path sum through recursive search is")
    print(divide_conquer(grid))
    times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print("The time taken through recursive search in seconds is")
    print(times)

    # output greatest path from dynamic programming 
    print("The greatest path sum through dynamic programming is")
    print(dynamic_prog(grid))
    times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
    times = times / 10
    # print time taken using dynamic programming
    print("The time taken for dynamic programming in seconds is")
    print(times)

if __name__ == "__main__":
  main()