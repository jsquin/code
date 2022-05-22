###########################
#                         #
#       Homework 1:       #
#  Written by Marcus Lee  #
#   Course Content from   #
#    Berkeley's CS61A     #
#                         #
###########################

from operator import add, sub

# QUESTION 1: k in Num
#     Write a function k_in_num which takes in two integers, k and num. 
#     k_in_num returns True if num has the digit k and returns False if num does not have the digit k. 
#     0 is considered to have no digits.

def k_in_num(k, num):
    """
    Complete k_in_num, a function which returns True if num has the digit k and
    returns False if num does not have the digit k. 0 is considered to have no
    digits.

    >>> k_in_num(3, 123) # .Case 1
    True
    >>> k_in_num(2, 123) # .Case 2
    True
    >>> k_in_num(5, 123) # .Case 3
    False
    >>> k_in_num(0, 0) # .Case 4
    False
    """

    "*** YOUR CODE HERE ***"


# QUESTION 2: A Plus Abs B
    # Python's operator module defines binary functions for Python's intrinsic arithmetic operators. 
    # For example, calling operator.add(2,3) is equivalent to calling the expression 2 + 3; both will return 5.
    # Fill in the blanks in the following function for adding a to the absolute value of b, without calling abs. 
    # You may not modify any of the provided code other than the two blanks.

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """

    if b < 0:
        f = _____
    else:
        f = _____
    return f(a, b)


# QUESTION 3: Two of Three:
#     Write a function that takes three positive numbers as arguments and returns the 
#     sum of the squares of the two smallest numbers. use only a single line for the body of the function.

def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    HINT: consider using the max or min functions
        >>> max(1, 2, 3)
        3
        >>> min(-1, -2, -3)
        -3

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """

    return _____


# QUESTION 4: Largest Factor 
#     Write a function that takes an integer n that is greater than 1 
#     and returns the largest integer that is smaller than n and evenly divides n.

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    HINT: 
        To check if b evenly divides a, you can use the expression a % b == 0, 
        which can be read as, "the remainder of dividing a by b is 0."

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """

    "*** YOUR CODE HERE ***"