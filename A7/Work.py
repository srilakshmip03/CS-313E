#  File: Work.py 

#  Description:  A simple binary search program

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID:  sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/29/22

#  Date Last Modified: 9/30/22

import sys, time

# Find the sum of the finite series of a given v value - helper function
# Input: an integer named v for the initial number of lines to write
# Output: the total number of lines possible with that v value
def find_sum(v, k):
    total = 0
    p = 0

    # add each term in the series to the final result
    while (v // (k ** p)) > 0:
        total += v // (k ** p)
        p += 1

    return total

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v (named i) the minimum lines of code to write using linear search
# Goes through each possible v value's sum one at a time and see which one goes past the requirement first.
def linear_search (n, k):
    i = 1

    # loop through n number of possibilities
    while i < n:
        total = find_sum(i, k)
        if total >= n:
            break
        else:
            i += 1

    return i

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee, as found by binary search
def binary_search (n: int, k: int) -> int:
    global mid
    lo = 0
    hi = n

    # find the total lines of code that middle value gives you
    while (lo < hi):
        mid = (lo + hi) // 2
        total = find_sum(mid, k)

        # binary search algorithm
        if total < n:
            lo = mid + 1
        elif total > n:
            hi = mid - 1
        else:
            break

    # adjust result because binary search doesn't get fine enough with result
    result = mid
    if lo == hi:
        result = lo

    return result

# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()