#  File: Hull.py

#  Description: Given a set of points, find the convex hull (convex polygon that encompasses all points).

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/26

#  Date Last Modified: 9/26

import sys

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("(" + str(self.x) + ", " + str(self.y) + ")")

# input: a list of lists that represent point objects
# output: a list of point objects
def make_points(string_lists):
    result = [] # result

    for i in range(len(string_lists)):
        point = Point()
        point.x = string_lists[i][0]
        point.y = string_lists[i][1]
        result.append(point)

    return result

# Input: A set of point objects in the x-y plane.
# Output: A list of point objects that define the vertices of the convex
#         hull in clockwise order.
def convex_hull(points):
# 1.  Sort the points by x-coordinates resulting in a sorted sequence p_1 ... p_n.
    points.sort(key=lambda point: point.x, reverse=False)

# 2.  Create an empty list upper_hull that will store the vertices in the upper hull.
    upper_hull = []

# 3.  Append the first two points p_1 and p_2 in order into the upper_hull.
    upper_hull.append(points[0])
    upper_hull.append(points[1])

# 4.  For i going from 3 to n
    for i in range(3, len(points)):
# 5.    Append p_i to upper_hull.
        upper_hull.append(points[i])

# 6.    While upper_hull contains three or more points and the last three
#       points in upper_hull do not make a right turn do (refer to the
# 	    notes below on determinants for right and left interpretations)

# 7.    Delete the middle of the last three points from upper_hull

# 8.  Create an empty list lower_hull that will store the vertices in the lower hull.
    lower_hull = []

# 9.  Append the last two points p_n and p_n-1 in order into lower_hull with p_n as the first point.
    lower_hull.append(points[-1])
    lower_hull.append(points[-2])

# 10. For i going from n - 2 downto 1
    for i in range(len(points) - 2, 1):
# 11.   Append p_i to lower_hull
        lower_hull.append(points[i])

# 12.   While lower_hull contains three or more points and the last three
#       points in the lower_hull do not make a right turn do
#
# 13.     Delete the middle of the last three points from lower_hull
#
# 14. Remove the first and last points for lower_hull to avoid duplication with points in the upper hull.
    lower_hull.remove(lower_hull[0])
    lower_hull.remove(lower_hull[-1])

# 15. Append the points in the lower_hull to the points in the upper_hull and call those points the convex_hull
    convex_hull_result = lower_hull + upper_hull

# 16. Return the convex_hull.
    return convex_hull_result

def main():
    # num_points = sys.stdin.readline().strip()

    file = open("hull.in")
    num_points = int(file.readline().strip())

    string_lists = []

    # make a list of point objects
    for i in range(num_points):
        current = file.readline().strip().split("\t") # read in one line, make into list
        current_ints = [int(x) for x in current]
        string_lists.append(current_ints)
    point_list = make_points(string_lists)

    # send list of point objects into convex hull function
    hull_vertices = convex_hull(point_list)

    # convert point objects to strings and prints them out
    hull_vertices = [str(p) for p in hull_vertices]

    print("Convex Hull")
    print(hull_vertices)

    # print("Area of Convex Hull: " + str(area))

if __name__ == "__main__":
    main()
