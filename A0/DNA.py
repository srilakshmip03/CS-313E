#  File: DNA.py

#  Description: Assignment 0 - Create a program that finds the longest common sequence between two given strands of DNA.
#               I think I got the "extra credit" bit to work as well!

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: August 26, 2022

#  Date Last Modified: August 29, 2022

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.

import sys

def all_substrings(s):
  result = []

  # define size of window
  wnd = len(s)

  # generate all substrings
  while (wnd > 1):
    i = 0
    while (i + wnd) <= len(s):
      sub_str = s[i:i + wnd]
      result.append(sub_str)
      i += 1

    # decrease window size
    wnd = wnd - 1

  # return result
  return result


def longest_subsequence(s1, s2):
  subs_s1 = all_substrings(s1)  # get all substrings in s1 (list)
  subs_s2 = all_substrings(s2)  # get all substrings in s2 (list)

  results = set(subs_s1) & set(subs_s2)
  is_common = bool(results) # is the set of intersections non-empty?

  if is_common:
    results = list(results)
    results.sort(key = len)
    results = max(results, key = len)
    return results
  else:
    return "No Common Sequence Found"

def main():

  # read number of pairs
  num_pairs = sys.stdin.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int(num_pairs)

  for i in range(num_pairs):
    st1 = sys.stdin.readline()
    st2 = sys.stdin.readline()

    st1 = st1.strip()
    st1 = st1.upper()

    st2 = st2.strip()
    st2 = st2.upper()

    # get the longest subsequences
    long_sub = longest_subsequence(st1, st2)

    # print result
    print(long_sub)
    print()

main()
