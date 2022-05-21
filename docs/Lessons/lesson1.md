---
title: Functions
layout: default
---

# {{"Lesson 1: Functions"}}

## Values

Fundamentally, a program is just a set of computer instructions that tells it how to manipulate values.\
But what is a value?


A value is information that a computer stores as a certain **data type**


| **Data Types** | **Examples**         |
|----------------|----------------------|
| Integers       | ```1``` ```2``` ```35139``` |
| Floats         | ```3.14159265``` ```2.7182182``` |
| Booleans       | ```True``` ```False```           |
| Strings        | ```"Hello World"``` ```'John'``` |

## Expressions

An expression is something that evaluates to values.\
Expression: ```'hello' + ' ' + 'world!'```
Value: ```'hello world!'```


An expression can contain operators (e.g.:```*```, ```+```, ...)\
* ```32 + 15```
* ```355 / 113```
* ```2 * 100```
* ```2 ** 100```


Try these out in the Notebook below!\
Type an expression into the bottom box then press ```shift``` + ```enter```\
The notebook will evaluate these expressions and print the value


<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1"
  width="100%"
  height="400px"
>
</iframe>


## Call Expressions
Expressions can also use function calls
* ```pow(2, 100)```
* ```max(50, 300)```
* ```min(-1, 30)```


How does python evaluate these call expressions?


| add | ( | 18 | , | 42 | ) |
|:---:|:---:|:---:|:---:|:---:|:---:|
|Operator| |Operand| |Operand| |


1. Evaluate the Operator
2. Evaluate the Operands
3. Apply the Operator (a function) to the evaluated operands (arguments)
Operators and Operands are also expressions so they need to be evaluated to get their values.


## Names

Names can be bound to values through the **assignment statement**


|x|=|7|
|:---:|:---:|:---:|
|name|assigment|value|


where the value can be any expression\
```x = 1 + 3 - mul(3,add(12 ** 2, 2))```


### Using Names

A name can be referenced as many times as you need
```python
x = 10
y = 5

answer = x * x + x - y / (y + x)
```


Note that a name can only have one value at a time.\
A name that's bound to a data value is also called a variable

### Name Re-Binding

Unlike most languages, python is a language with dynamic typing, binding, and rebinding.
That is, if you previously assigned ```a = 30```, then a is bound to an integer with the value 30.\
If you then run ```a = "hello"```, a will be bound to a string with the value "hello".


This is different from other common languages like Java, C, or C++. 


First: In other languages, running: 
```a = 30``` will throw an error because they're statically typed. Meaning you have to declare the data type of 
the variable, whereas python assumes it from the value you're binding the variable to.\
Python: ```a = True```. Assumes a is a boolean variable\
Java: ```Bool a = true;```. Needs to be told that a is a boolean variable


Second: Reassigning ```a = False;``` would be fine in Java, since a is still a boolean. However attempting to run: ```a = 30;``` would
cause an error because it cannot assign an Integer to a boolean variable.


Feel free to explore naming and expressions below.

<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1"
  width="100%"
  height="400px"
>
</iframe>


## Environment Diagrams
TODO 

## Functions
A function is a sequence of code that performs a specific task that can easily be reused.\
We've used functions already\
```python
add(5, 3)
mul(10, 12)
```


### Defining Functions

The most common way to create functions is using the ```def``` statement.
```python
def <name>(<parameters>):
    return <expression>
```
For example:
```python
def add(num1, num2):
    return num1 + num2 
```
and after we define it, it can be used:
```python
add(2, 2)
add(3, 4)
```

### Anatomy of Function Definitions


### Functions in Environment Diagrams


## Revisiting Names

### Name lookup rules










# {{ "Practice"}}



## Nested Expressions

How would we evaluate ```add(add(6, mul(4, 6)), mul(3, 5))```?

## Name Rebinding

What is the final value after this sequence of code?
```
f = min 
f = max 
g = min 
h = max 
max = g 
max(f(2, g(h(1, 5), 3)), 4)
```


<details>
    <summary>Click for Solution</summary>
  
    ### Solution
    ```python
    # Final State: 
    max = min()
    f = max() 
    g = min()
    h = max()

    # Expression
    min(max(2, min(max(1, 5), 3)), 4)
    
    # Evaluates to:
    3
    ```

</details>


<details><summary>Click to expand</summary>

<h1>Testing titles</h1>
<p>Now I am testing text</p>
<code>def hello(): </code>


</details>


<details><summary>CLICK ME</summary><br>
<p>

#### yes, even hidden code blocks!

```python
print("hello world!")
```

</p>
</details>

## Spot the Bug


## Name Lookup 


