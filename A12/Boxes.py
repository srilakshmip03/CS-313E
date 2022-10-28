#  File: Boxes.py

#  Description: A12; find max number of nested boxes

#  Student Name: Rin Chiang

#  Student UT EID: ksc2495

#  Partner Name: Srilakshmi Palanikumar

#  Partner UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/16/2022

#  Date Last Modified: 10/18/2022

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
    # create 2-D list memo which holds [N(i), Max_Now, R(i)]
    memo = [[0, 0, []] for i in range(len(box_list))]
    memo[0] = [1, 1, []]

    for i in range(1, len(box_list)):
        # store default values if there are no nests for box i in memo
        memo[i][0] = 1
        memo[i][1] = memo[i - 1][1]
        # create value to store local max for boxes that fit in box i
        localmax = 1
        # loop through boxes smaller than i
        j = 0
        while (j < i):
            # check to see if box j fits in box i and if the new value is
            # greater than the local max
            if (does_fit(box_list[j], box_list[i]) 
                and (memo[j][0] + 1 >= localmax)):
                # update N(i), localmax, Max_Now (if needed), and R(i)
                memo[i][0] = memo[j][0] + 1
                localmax = memo[i][0]
                if (localmax > memo[i][1]):
                    memo[i][1] = localmax
                memo[i][2].append(j)
            j += 1

    # find number of sets matching the max subset amount
    count = 0
    for i in range(len(memo)):
        if (memo[i][0] == memo[len(memo) - 1][1]):
            # call recursive counting function for each box with max N(i)
            count += num_subsets(memo, memo[i][2], memo[len(memo) - 1][1] - 1)
    
    # return results
    return memo[len(memo) - 1][1], count

# recursive function to compute the number of subsets with the given n
# Input: memo, list of R(i) from larger box to check, and n of larger box
# Output: sum of all possible subset pathways
def num_subsets(memo, idxs, n):
    # base case if n = 1 is reached (idxs holds boxes with no nests)
    if (n == 1):
        # return number of boxes with no nests
        return len(idxs)
    else:
        new_idxs = []
        # loop through idxs (or the R(i) of the box we are testing)
        for i in range(len(idxs)):
            box = idxs[i]
            # catch cases of boxes that have correct number of subsets
            if memo[box][0] == n:
                # add box to new idx list
                new_idxs += memo[box][2]
        # call recursive function with new indexes and next subset size
        return num_subsets(memo, new_idxs, n - 1)

# returns True if box1 fits inside box2
def does_fit (box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
    # read the number of boxes 
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range (num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range (len(box)):
            box[j] = int (box[j])
        box.sort()
        box_list.append (box)

    '''
    # print to make sure that the input was read in correctly
    print (box_list)
    print()
    '''

    # sort the box list
    box_list.sort()

    '''
    # print the box_list to see if it has been sorted.
    print (box_list)
    print()
    '''

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes (box_list)

    # print the largest number of boxes that fit
    print (max_boxes)

    # print the number of sets of such boxes
    print (num_sets)

if __name__ == "__main__":
  main()