<!-- Navigation -->

---

[Previous: 22 - Try Except](./22-Try-Except.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 24 - Reading Code](./24-Reading-Code.md)

---
<!-- End Navigation -->
# 23 - Imports

This is the last concept we will cover that I would consider the "basics" of Python and programming in general. Up to now, we have been using only the built-in functionality of Python. This is, in fact, a very limited view of what Python can do. To get the full power and utility of Python, we can use libraries of code that other programmers have written to do all sorts of complex and powerful tasks.

In this lesson we will introduce many different tools that you may want to use. While going through the exercises in this lesson do not worry about learning everything there is to know about each set of tools. The point of this lesson is to get you familiar with how to get what you need for programming.

With that said let's start!

```python
# import_practice.py

import os
from math import sin, log, pi
from random import random
import csv
import datetime as dt

# os example
print("Python doing: ls")
for root, dirs, files in os.walk("."):
    print("-" * 20)
    print("Folder Name:", root, "\n----")
    print("Sub-folders:")
    for directory in dirs:
        print("\t", directory)
    
    print("---\nFiles:")
    for file in files:
        print("\t", file)
    print("")

print("-" * 20)


# math example
print("sin(\u03C0/2) =", sin(pi/2))
print("ln(23)   =", round(log(24), 2))


# random example
def gen_random_matrix(size):
    """
    Returns a 2D matrix (a.k.a. a list of lists)
    of shape "size X size" with elements generated 
    having random values between 0 and 1
    """
    matrix = []
    for row_index in range(size):
        row = []
        for element in range(size):
            row.append(random())
        matrix.append(row)
    return matrix


# csv example
with open("data.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(gen_random_matrix(3))


# datetime example
print("\nThe exact date and time is:", dt.datetime.now())

```

**Here is what should happen**

```
$ python import_practice.py
Python doing: ls
--------------------
Folder Name: .
----
Sub-folders:
         .ipynb_checkpoints
---
Files:
         data.csv
         import_practice.py
         import_text.py
         solution_test_1.py
         test_write.ipynb
         TOC_tba.md
         wacky_story.py

--------------------
Folder Name: .\.ipynb_checkpoints
----
Sub-folders:
---
Files:
         test_write-checkpoint.ipynb

--------------------
sin(π/2) = 1.0
ln(23)   = 3.18

The exact date and time is: 2019-01-05 12:38:55.442190
$ python import_practice.py
Python doing: ls
--------------------
Folder Name: .
----
Sub-folders:
         .ipynb_checkpoints
---
Files:
         data.csv
         import_practice.py
         solution_test_1.py
         test_write.ipynb
         TOC_tba.md
         wacky_story.py

--------------------
Folder Name: .\.ipynb_checkpoints
----
Sub-folders:
---
Files:
         test_write-checkpoint.ipynb

--------------------
sin(π/2) = 1.0
ln(23)   = 3.18

The exact date and time is: 2019-01-05 12:49:54.332969
$
```

### Imports

The main concept we introduced in this exercise is that of an `import` statement. These statements are how we use code from another script written in Python. The syntax of an import statement follows two basic forms:

- `import NAME`

  This statement pulls an object called `NAME` into your script that contains the entirety of the script called   `NAME.py`. This kind of object is called a module.  (Python has rules to keep track of where to look for any module you import.) 

  You can then use any of the contents of `NAME.py` such as functions or objects defined in that module. You use them by the dot notation as we saw in the case of `os` (i.e. `NAME.function_name()` or as above with `os.walk()`).

- `from MODULE import NAMES`

  Sometimes pulling in an entire script is inefficient especially when you want only one or two things from the script. You can pick and choose what you want to use with the `from-import` style statements.  As we saw from the `math` and `random` examples, you can then call these functions directly without dot notation. However be aware that if you make a variable or write a function with the same name as these, it will override their definition.

For the line that reads `import datetime as dt`, the `as` part of the statement is just changing the name of the function and is practically the same as writing `dt = datetime`.  This is common practice in Python especially for libraries with longer names.

### Standard Libraries

The five libraries we used in `import_practice.py` are part of the [Python Standard Library](https://docs.python.org/3/library/) and can be considered "built-in" to Python. There are well over 200 different modules in Standard Library and to go over each one would be tedious and not very useful. Therefore, this exercise is designed to introduce a few common libraries and get you used to the syntax of importing and using them. But to be thorough, here some brief explanations of each of the libraries we used in this exercise:

- `os`

  `os` stands for "Operating System". This module allows you to interact with the operating system and the command line to some extent. It contains some file managing tools (e.g. rename or move files, explore the file system etc.) and also some system-specific functionality. There are other modules like `sys` and `subprocess` that provide more specific functionality depending on what you need.

- `math`

  This module allows you to access the basic math functions provided by the C standard library. These include but are not limited to trigonometric and hyperbolic functions (e.g. sin, cos, sinh, cosh etc.), exponential and logarithmic functions (e.g. exp, log etc.) and common logical functions you may need.

- `random` 

  This provides a large selection of random number generators and functionality related thereto.

- `csv`

  A popular plain-text format for data is the "Comma-Separated Values" format. This is a handy library for working with these files without having to constantly reinvent the wheel. Specifically, it can turn iterables into `csv` files with minimal coding.

- `datetime`

  A library for working with date and time. The library bases its times on computer times and is a useful feature for getting calendar-like functionality out of your programs. It includes sub modules for both `date` and `time` if you happen to be interested in only one of the two.

These are just a surface look at each of these libraries but don't worry too much about learning every library. I have never had occasion to use many of the standard libraries but they are a great starting place for accomplishing complex tasks more easily.

### Getting More Libraries and Packages

Any package in the Python Standard Library is written and endorsed by the creators and maintainers of Python. However, there is an enormous number of libraries that are written and maintained by thousands of programmers everywhere. These are sometimes called third-party libraries or packages and are available for quick download and installation through a handy software called `pip` which is built-in to your standard Python 3 installation.

Let's practice with it here by installing a package called `nose`. Open your command line and the following:

```bash
$ pip install nose --user
<a bunch of text>
Successfully installed nose-1.3.7
$ 
```

The `--user` option tells `pip` to install the package only for the current user. This avoids certain permission problems that can occur on your operating system. If you see something like `Successfully installed nose-1.3.7` then the package installed correctly. `nose` is a package that allows you to write tests for larger programs. However, it is not actively being maintained so we don't need it. Since this was just for practice anyway, let's uninstall it. Uninstall the package by using the following command:

```bash
$ pip uninstall nose
Uninstalling nose-1.3.7:
  Would remove:
    <list of files that will be removed>
Proceed (y/n)? y
  Successfully uninstalled nose-1.3.7
$
```

Likewise if you see something like ` Successfully uninstalled nose-1.3.7` the package was removed successfully.

Skim the basic commands of pip [here](https://pip.pypa.io/en/stable/quickstart/) and use them to install libraries/packages when you need them. We will install more packages later once we get further along.

## Hone Your Skills

- The [Python Standard Library](https://docs.python.org/3/library/) is a good reference to get an idea of all the things that Python can do without even including third-party libraries and packages. Read the general statement at the beginning of the linked page and browse the index looking for 2 or 3 things that interest you. Begin to experiment with them and see if you can pick up how they work.
- There are hundreds of libraries in the [Python Package Index](https://pypi.org/). Follow that link and look around for packages that look interesting and try installing them and using them. For practice, can you find, install and use a package that opens a game of [tetris](https://en.wikipedia.org/wiki/Tetris) in your terminal?
- Consider the following function definition from  `import_practice.py`:

```python
def gen_random_matrix(size):
    """
    Returns a 2D matrix (a.k.a. a list of lists)
    of shape "size X size" with elements generated 
    having random values between 0 and 1
    """
    matrix = []
    for row_index in range(size):
        row = []
        for element in range(size):
            row.append(random())
        matrix.append(row)
    return matrix
```

  It turns out Python has a neat trick called a [List Comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) to turn all that code into one line of code so that it can be written as follows:

```python
def gen_random_matrix(size):
    """
    Returns a 2D matrix (a.k.a. a list of lists)
    of shape "size X size" with elements generated 
    having random values between 0 and 1
    """
    return # insert line of code here
```

  After reading about list comprehensions write one line of code that will do the same thing as above and run it to test it.

<!-- Navigation -->

---

[Previous: 22 - Try Except](./22-Try-Except.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 24 - Reading Code](./24-Reading-Code.md)

---
<!-- End Navigation -->
