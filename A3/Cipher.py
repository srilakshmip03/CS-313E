#  File: Cipher.py

#  Description: A program to encrypt and decrypt short strings by manipulating a 2D array onto which the original
#               string is mapped.

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: September 12, 2022

#  Date Last Modified: September 12, 2022

import sys
import math

def get_table(strng):
    # determine the size of the matrix
    strng = strng.strip()
    string_len = len(strng)
    root_string = math.sqrt(string_len)
    global side_len
    if root_string.is_integer():
        side_len = root_string
    else:
        side_len = math.ceil(root_string)
    matrix_size = math.pow(side_len, 2)

    # make string fit the matrix by adding asterisks to the end
    strng = strng.strip()
    while len(strng) < matrix_size:
        strng = strng + "*"

    # initialize matrix
    side_len = int(side_len)
    init_table = [["" for _ in range(side_len)] for _ in range(side_len)]


    # fill matrix with given string
    cursor = 0
    for i in range(side_len):
        for j in range(side_len):
            init_table[i][j] = strng[cursor]
            cursor += 1

    # return a matrix filled with the string (as long as it goes) and asterisks to fill space.
    return init_table

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def encrypt(strng):
    # initialize a table with the text to be encrypted
    init_table = get_table(strng)

    # initialize a table to store the encryption in
    result_table = [["" for _ in range(side_len)] for _ in range(side_len)]

    # do encryption:
    # the x and y coordinates of each element from the original table are swapped and stored in new table.
    # the order of each row is reversed.
    for i in range(side_len):
        for j in range(side_len):
            result_table[i][j] = init_table[abs(j - (side_len - 1))][i]

    # convert the table to a string, ignoring the asterisks.
    encrypted = ""
    for i in range(side_len):
        for j in range(side_len):
            if result_table[i][j] != "*":
                encrypted += result_table[i][j]

    # return encrypted string
    return encrypted

# # Input: strng is a string of 100 or less of upper case, lower case,
# #        and digits
# # Output: function returns a decrypted string
def decrypt(strng):
    # initialize a table with the encrypted text.
    init_table = get_table(strng)

    # initialize a table to store the results in.
    result_table = [["" for _ in range(side_len)] for _ in range(side_len)]

    # perform decryption:
    # swap x and y coordinates of each element in the original matrix and store in new one.
    # the order of columns are reversed.
    for i in range(side_len):
        for j in range(side_len):
            result_table[i][j] = init_table[j][abs(i - (side_len - 1))]

    # convert the table to a string, ignoring the asterisks.
    decrypted = ""
    for i in range(side_len):
        for j in range(side_len):
            if result_table[i][j] != "*":
                decrypted += result_table[i][j]

    # return decrypted string
    return decrypted

def main():
    # read the two strings P and Q from standard input
    # p = sys.stdin.readline()
    # q = sys.stdin.readline()
    file = open("cipher.in", "r")
    p = file.readline()
    q = file.readline()

    # encrypt the string P
    encrypted = encrypt(p)

    # decrypt the string Q
    decrypted = decrypt(q)

    # print the encrypted string of P and the
    # decrypted string of Q to standard out
    print(encrypted)
    print(decrypted)


if __name__ == "__main__":
  main()