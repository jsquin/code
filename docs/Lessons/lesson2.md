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


## Pure vs Not Pure Functions

Pure functions _only_ return a value, whereas not sure functions have a side effect (like printing a value)

## Nested Print Statements

What will this display? (Hint: Recall how functions are evaluated)
```Python
print(print(1), print(2))
```
<details><summary>Click for Solution</summary>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight">
<code>1
2
None None</code>

</pre></div></div>


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

## More Function Features

Try running it here
<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1"
  width="100%"
  height="500px"
>
</iframe>


