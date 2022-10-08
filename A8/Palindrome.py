#  File: Palindrome.py

#  Description: A program to find the smallest string that is a palindrome that you can construct from a given string. Construct palindrome by
#               adding letters to the beginning of the given string.

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/3/22

#  Date Last Modified: 10/3/22

import sys

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a boolean stating if the string is a palindrome
# Helper method to find out if a given string is already a palindrome.
def is_palindrome(str):
    forward = str
    backward = str[::-1]
    return forward == backward

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    if is_palindrome(str):
        # no changes needed
        return str

    else:
        # add last letter of string to beginning
        result = str[-1]

        # if adjusted string is still not a palindrome, add next to last letter and check. repeat as needed.
        # second statment to prevent infinite loop: stop checking if entire string has been checked.
        i = -2
        while not is_palindrome(result + str) and (i > (len(str) * -1)):
            result += str[i]
            i -= 1
            
        return result + str


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  assert smallest_palindrome("cacb") == "bcacb"
  assert smallest_palindrome("") == ""
  assert smallest_palindrome("kayak") == "kayak"
  assert smallest_palindrome("z") == "z"
  assert smallest_palindrome("fghj") == "jhgfghj"

  return "all test cases passed"

def main():
    file = open("palindrome.in")
    # read the data line by line 
    # and print the smallest palindromic string that can be made for each input
    lines = file.readlines()
    for i in lines:
        i = i.strip()
        small = smallest_palindrome(i)
        print(small)


if __name__ == "__main__":
  main()