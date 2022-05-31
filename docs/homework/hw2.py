###########################
#                         #
#       Homework 2:       #
#  Written by Marcus Lee  #
#   Course Content from   #
#    Berkeley's CS61A     #
#                         #
###########################

from operator import add, mul
square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1


def count_until_larger(num):
    """
    Complete the function count_until_larger that takes in a positive integer num.
    count_until_larger examines the rightmost digit and counts digits from right to
    left until it encounters a digit larger than the rightmost digit, then returns that count.

    >>> count_until_larger(117) # .Case 1
    -1
    >>> count_until_larger(8117) # .Case 2
    3
    >>> count_until_larger(9118117) # .Case 3
    3
    >>> count_until_larger(8777)  # .Case 4
    3
    >>> count_until_larger(22) # .Case 5
    -1
    >>> count_until_larger(0) # .Case 6
    -1
    """
    "*** YOUR CODE HERE ***"
    digit, num, count = num % 10, num // 10, 1
    while num > 0:
        if num // 10 > digit:
            return count
        count += 1
    return -1

def filter_sequence(cond, start, stop):
    """
    Returns the sum of numbers from start (inclusive) to stop (inclusive) that satisfy
    the one-argument function cond.

    >>> filter_sequence(lambda x: x % 2 == 0, 0, 10) # .Case 1
    30
    >>> filter_sequence(lambda x: x % 2 == 1, 0, 10) # .Case 2
    25
    """
    "*** YOUR CODE HERE ***"
    return sum([x for x in range(start, stop + 1) if cond(x)])
    # Alternatively:
    total = 0
    for i in range(start, stop+1):
        if cond(i):
            total += i 
    return i 
    # Alternatively:
    total = 0
    while start <= stop: 
        start += 1 
        if cond(start):
            total += i 
    return total 


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(3 * n + 1) + 1


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    prod = 1
    for i in range(1, n+1):
        prod *= term(i)
    return prod 

def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    total = start 
    for i in range(1,n+1):
        total = merger(total, term(i))
    return total 
    