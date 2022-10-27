#  File: Boxes.py

#  Description: A12; find max number of nested boxes

#  Student Name: Rin Chiang

#  Student UT EID: ksc2495

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/16/2022

#  Date Last Modified:

import sys
file = open("boxes.in")

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
    # create 2-D list memo which holds [N(i), Max_Now, R(i), i]
    memo = [[0, 0, 0, 0] for i in range(len(box_list))]
    memo[0] = [1, 1, [1], 1]

    for i in range(1, len(box_list)):
        # store default values if there are no nests for box i in memo
        memo[i][0] = 1
        memo[i][1] = memo[i - 1][1]
        memo[i][2] = []
        memo[i][3] = i + 1
    
    for i in range(1, len(box_list)):
        

    # print memo to see if it computed correctly
    for i in range(len(memo)):
        print(memo[i])

    count = 0

    # return results
    return memo[len(memo) - 1][1], count

# returns True if box1 (smaller, i) fits inside box2 (larger, i + 1)
def does_fit (box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
    # read the number of boxes 
    line = file.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range (num_boxes):
        line = file.readline()
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