#  File: Intervals.py

#  Description: A program to collapse intervals that overlap in a given list of intervals, and print the new list.
#               The program also sorts the intervals by length and prints out a sorted list.

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: September 10, 2022

#  Date Last Modified: September 12, 2022

import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the interval

def merge_tuples(tuples_list):
    tuples_list.sort()

    result_merged_list = [tuples_list[0]]
    last_in_result = 0

    # check if the last item in new list overlaps with the next item in tuples list. if there's an overlap,
    # alter the last item in result list to account for overlap. otherwise, move on to check next item in tuples list.
    for i in tuples_list[1:len(tuples_list)]:
        if result_merged_list[last_in_result][0] <= i[0] <= result_merged_list[last_in_result][1]:
            if result_merged_list[last_in_result][1] < i[1]:
                result_merged_list[last_in_result][1] = i[1]
        else:
            result_merged_list.append(i)
            last_in_result += 1

    return result_merged_list


# Input: tuples_list is a list of tuples denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval

def sort_by_interval_size(tuples_list):
    # find "length" of the tuples
    for i in tuples_list:
        diff = i[1] - i[0]
        i.append(diff)

    # sort by new diff measurement
    tuples_list.sort(key=lambda x: x[2])

    # convert everything back to tuples, omit the difference measurement.
    result_sorted_list = []
    for item in tuples_list:
        result_sorted_list.append(tuple(item[0:2]))

    return result_sorted_list


# Input: no input
# Output: a string denoting all test cases have passed

def test_cases():
    assert merge_tuples([(1, 2)]) == [(1, 2)]
    assert merge_tuples([(1, 2), (5, 6)]) == [(1, 2), (5, 6)]
    assert merge_tuples([(1, 5), (2, 6)]) == [(1, 6)]

    assert sort_by_interval_size([(1, 3), (4, 5)]) == [(4, 5), (1, 3)]
    assert sort_by_interval_size([(1, 7), (1, 5)]) == [(1, 5), (1, 7)]

    return "all test cases passed"


def main():
    # open file intervals.in and read the data and create a list of tuples
    num_intervals = int(sys.stdin.readline())
    tuples_list = []

    for i in range(num_intervals):
        line = sys.stdin.readline().strip()
        interval = line.split()
        current_list = [int(interval[0]), int(interval[1])]
        tuples_list.append(current_list)

    # merge the list of tuples
    merged_list = merge_tuples(tuples_list)

    # convert each item in merged list into a tuple and print the final list.
    result_merged_list = []
    for i in merged_list:
        result_merged_list.append(tuple(i[0:2]))
    print(result_merged_list)

    # sort the list of tuples according to the size of the interval, print it
    result_sorted_list = sort_by_interval_size(merged_list)
    print(result_sorted_list)


if __name__ == "__main__":
    main()