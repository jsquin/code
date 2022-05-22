---
title: Lesson 0- Python
layout: default
---

# {{"Lesson 0: Python Basics"}}

Note: Not everything here will make sense immediately. This is meant to be a refresher / supplement on python as you progress through the lessons.

## What is Python?

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
These words might not mean much right now, but hopefully it will make sense as you progress through these lessons.

## Printing

Printing is how you can see what the computer is "thinking" at any point in time. Say you have a variable that you manipulate many times. You can use print statements to make sure the code is doing what you want it to do.

```python
a, b = 1, 1
while b < 1000:
  a, b = b, a + b 
  print(b) # What do you think this code does?
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
</pre></div></div>

# {{ "Practice"}}

<!--
You can use HTML elements in Markdown, such as the comment element, and they won't
be affected by a markdown parser. However, if you create an HTML element in your
markdown file, you cannot use markdown syntax within that element's contents.
-->