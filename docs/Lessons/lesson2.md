---
title: Lesson 2- Control
layout: default
---

# {{"Lesson 2: Control"}}


## The ```None``` Value

```None``` represents nothingness in Python. A function without a return statement returns ```None```.
```python
def square(x):
    x * x 
```
When a function returns ```None``` the console shows no output.
```python
print(square(4))
>>> None 
```
Treating ```None``` like a number causes problems
```python
sixteen = square(4)
sum = sixteen + 4
>>> TypeError
```

## Side Effects

Side effects are things that happen from calling a function besides the function's return value. \
The most common side effect is using the ```print()``` statement for debugging purposes\
Other common side effects include drawing things on the screen and accessing files.


Ask yourself: Which one has a side effect? What are the data types of the return values?
```python
def square(x):
    return x * x 
```
```python
def square2(x):
    print(x * x)
```

## Nested Print Statements

What will this display? (Hint: Recall how functions are evaluated)
```Python
print(print(1), print(2))
```
<details><summary>Click for Solution</summary>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight">
<code>1
2
None None</code></pre></div></div>

<details><summary>Click for Explanation</summary>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight">
<code>Python starts by evaluating the operator. It reads print() and realizes its the built-in print() function.
Python then evaluates each operand. The first print statement, print(1) is evaluated.
To evaluate print(1) it repeats by evaluating the operator, print(). Then evaluates the operand 1, as the integer 1.
It then runs print(1), which prints out 1 into the console, then returns None.
It repeats this process for print(2).
Finally it runs the first print() function, which has the arguments None and None.</code>
</pre></div></div></details>

</details>

<!--Needs more/better explanation-->

Try running it here
<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1"
  width="100%"
  height="500px"
>
</iframe>


## More Function Features

In the function signature, a parameter can specify a **default value**. If the parameter isn't passed in, the default value is used instead.\
Default values can be overridden by specifying the parameter name or just placing a value where the default value is.

```python
def multiply_by(num, multiplier = 10):
    return num * multiplier 

multiply_by(3)
>>> 30
# Overriding default values
multiply_by(3, 10)
>>> 30 
multiply_by(3, multiplier = 10)
>>> 30 
```

## Mutliple return values

A function can specify more than one return value, separated by commas.

```python
def divide_exact(n, d):
    quotient = n // d
    remainder = n % d 
    return quotient, remainder
```
Any code that uses a function with more than one return value must also unpack the return values

```python
p, q = divide_exact(618, 10)
```

## Booleans

A boolean is either ```True``` or ```False```


Expressions can evaluate to booleans, usually using comparison or logical operators
```python
passed_class = grade >= 70
wear_jacket = is_raining or is_windy or is_snowing
```

### Comparison Operators

|Operator|Meaning|True Expressions|
|:---:|:---:|:---:|
|==|Equality|```32 == 16 + 16``` ```'a' == 'a'```|
|!=|Inequality|```32 != 16``` ```'a' != 'b'```|
|>|Greater than|```32 > 16``` ```16 + 1 > 16```|
|>=|Greater than or equal|```32 >= 16``` ```16 >= 16```|
|<|Less than|```32 < 64``` ``` 1-3 < 13```|
|<=|Less than or equal|````23 < 46``` ```13 <= 13```|

### Logical Operators

|Operator|True Expressions|Meaning|
|:---:|:---:|:---:|
|```and```|```4 > 0 and 2 < 3```|Evaluates to ```True``` if both conditions are true. ```False``` otherwise.|
|```or```|```4 > 0 or 2 < -3```|Evaluates to ```True``` if either conditions are true. ```False``` if both are false.|
|```not```|``` not (5 == 0)```|Evaluates to ```True``` if the condition is false. ```False``` if the condition is true.|


### Compound Booleans

When combining multiple operators in an expression, you can use paranthesis to group them together.

``` mobility_issues = (age >= 0 and age <= 2) or age > 90```


