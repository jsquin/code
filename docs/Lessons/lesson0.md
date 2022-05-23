---
title: Lesson 0- Python
layout: default
---

# {{"Lesson 0: Python Basics"}}

Note: Not everything here will make sense immediately. This is meant to be a refresher / supplement on python as you progress through the lessons.

## What is Python?

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.\
Python being interpreted means that each line of code is run directly, without converting it into machine code.\
This is the opposite of languages like Java and C, which are compiled languages. Compiled languages first convert the human-made code into machine code, instructions that the CPU understands.\
The rest of the terms like object-oriented and dynamic semantics will be explained later throughout the lessons.

## Printing

Printing is how you can see what the computer is "thinking" at any point in time. Say you have a variable that you manipulate many times. You can use print statements to make sure the code is doing what you want it to do.

```python
a, b = 1, 1
while b < 1000:
  a, b = b, a + b 
  print(a) # What do you think this code does?
```

Try running it here
<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1"
  width="100%"
  height="500px"
>
</iframe>

<details><summary>Click for Solution</summary>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight">
<code>It generates the Fibbonacci numbers less than 1000.</code>
</pre></div></div></details>


## Comments

Comments are text in code that are ignored by the python interpreter. The program can't see comments, they're meant entirely for humans

```python
a = 1
# return a 
# the statement above does nothing
return a 
# the statement above does something
"""
This is a multi-line comment
which is actually just a really long string.
"""
```


## Arithmetic Operations

Python has many arithmetic operators that work on various data types. The basic ones are:
* ```+``` for addition 
* ```-``` for subtraction
* ```*``` for multiplication
* ```/``` for division
* ```%``` for modulo (remainder)
* ```**``` for exponentiation

```python
3 + 3 # = 6
's' + 'tring' # = 'string'
[3] * 3 # = [3,3,3]
3 ** 2 # = 9
```


## Assignment Operators

Python has assignment operators that set the value of the variable on the left side. The basic ones are:
* ```=``` for assigning
* ```+=``` for adding then assigning
* ```-=``` for subtracting then assigning
* ```*=``` for multiplying then assigning
* ```/=``` for multiplying then assigning

```python
x = 10 # x = 10 
x += 2 # x = 12 
x /= 6 # x = 2
x *= 4 # x = 8
```

## Comparison Operators

Python has comparison operators that return true or false based on the values on the left and right. The basic ones are:
* ```==``` check if equal
* ```<``` check if less than
* ```<=``` check if less than or equal to 
* ```>``` check if greater than
* ```>=``` check if greater than or equal to

```python
x = 10 # x = 10 
x == 10 # Returns True
x < 10 # Returns False
x <= 10 # Returns True 
```

## Modulo Operator

The modulo operator is also known as the remainder operator. It returns the remainder of the division of the left by the right number.

```python
4 % 2 == 0 
2 % 4 == 2 
7 % 3 == 1
```

Activity: How would you implement the modulo operator without using ```%```?


## Strings

Strings are essentially a list of single characters. ```"hello"``` can be thought of as ```['h', 'e', 'l', 'l', 'o']```

### Indexing

Sometimes we want to access parts of a larger string. We do this by indexing into the string with brackets at the end.\
A single character can be accessed with ```[<index>]```, and a substring can be accessed with ```[<start>:<end>]``` where start is inclusive and end is exclusive.
Note: Python is zero indexed. This means the first letter in a string is accessed with ```[0]```.
Note 2: You can also index with negative numbers, which wraps around to the end of the string.
Note 3: If you ommit start or end in a substring, python assumes you mean the beginning or end of the string, respectively.

```python
string = "coding is fun"
string[0] # = "c"
string[-2] # = "u"
string[0:5] # = "codin"
string[:4] # = "cod"
string[4:] # = "ing is fun"
```

### in 

The ```in``` keyword is used to see if a value is present in a sequence. For strings, it returns true if a string exists in a different string and false otherwise.

```python
"fun" in "coding is fun" # = True 
"fun!" in "coding is fun" # = False 
"bca" in "abc" # = False 
"e" in "ea sports its in the game" # = True 
```

### length

Python has a built-in ```len()``` function that returns the length of the string.

```python
len("hello") # = 5
len("") # = 0
```

### Iterating

Sometimes you want to access each character in a string in succession. You can do this using a ```for``` loop.

```python
for letter in "hello!":
  print(letter) # "h", "e", "l", "l", "o", "!"
```



<!--
You can use HTML elements in Markdown, such as the comment element, and they won't
be affected by a markdown parser. However, if you create an HTML element in your
markdown file, you cannot use markdown syntax within that element's contents.
-->