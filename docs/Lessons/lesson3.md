---
title: Lesson 3- Higher Order Functions
layout: default
---

# Lesson 3: Higher Order Functions

## Fibonacci Numbers

Discovered by Virahanka in India in 600-800 AD and later re-discovered in Western mathematics called Fibonacci Numbers


0 1 1 2 3 5 8 13 21 34 55 89 ... 


Fibonacci Numbers are a sequence of numbers where each number is defined as the sum of the previous two numbers.\
The Fibonacci Sequence starts with 0 and 1.
```python
def fib_number(n)
""" 
Compute the nth Virahanka - Fibonacci Number, for N >= 1
>>> fib_number(2)
1
>>> fib_number(6)
8
"""
prev, curr = 0, 1
index = 1
while index < n:
    prev, curr = curr, prev + curr 
    index += 1
return curr
```

### Describing Functions

```python
def square(x):
    """ Returns the square of X"""
    return x * x
```
* A function's **domain** is the set of all inputs it might possibly take as input. (e.g.: ```x``` is a number)
* A function's **range** is the set of output values it might return. (e.g.: ```square``` returns a non-negative real number)
* A pure function's **behavior** is the relationship it creates between input and output. (e.g.: ```square``` returns the square of ```x```)


### Designing Functions

Advice: Give each function exactly one job, but make it apply to many related situations
```python
round(1.23) # 1
round(1.23, 0) # 1
round(1.23, 1) # 1.2
round(1.23, 5) # 1.23
```


**Don't Repeat Yourself (DRY):** Implement a process just once, execute it many times.

## Generalization

### Generalizing Patterns with Arguments
Geometric Shapes have similar area formulas.
* Square:                1 * r ^ 2
* Circle:               pi * r ^ 2
* Hexagon: 3 * sqrt(3) / 2 * r ^ 2

### The Non-Generalized Approach
```python
from math import pi, sqrt

def area_square(r):
    return r * r

def area_circle(r):
    return r * r * pi

def area_hexagon(r):
    return r * r * (3 * sqrt(3) / 2)
```

How do we generalize this common structure?


```python
from math import pi, sqrt

def area(r, shape_constant):
    """Return the area of a shape from length measurement R."""
    if r < 0:
        return 0
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)
```

## Higher Order Functions

### What is a Higher Order Function?

A function that either:
* Takes another function as an argument
* Returns a function as its result
All other functions are considered first order functions

