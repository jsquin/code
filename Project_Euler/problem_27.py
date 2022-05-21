"""
Euler discovered the remarkable quadratic formula:
    p(n) = n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However,
when n = 40. p(n) is divisible by 41, and certainly when n = 41, p(n) is clearly divisible by 41.

The incredible formula  was discovered, which produces 80 primes for the consecutive values . The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
    n^2 + an + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""
import numpy as np
primes = set()

def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return False
    for i in range(3, int((num) ** 0.5), 2):
        if num % i == 0:
            return False
    return True

def check_running_primes(ftn):
    n = 0
    count = 0
    while is_prime(ftn(n)):
        count += 1
        n += 1
    return count 

def generate_functions():
    max_vals = (0,0,0) #(primes, a, b)
    for a in range(-1000,1000):
        print('a:', a)
        for b in range(-1000, 1000):
            func = lambda n: n ** 2 + a * n + b 
            count = check_running_primes(func)
            if count > max_vals[0]:
                max_vals = (count, a, b)
    return max_vals

print(generate_functions())
