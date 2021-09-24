<!-- Navigation -->

---

[Previous: 04 - Hello World](./04-Hello-World.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 06 - Strings and the Print Function](./06-Strings-and-the-Print-Function.md)

---
<!-- End Navigation -->

# 5 - Comments 

The next thing you need to understand that is fundamental to programming is comments in code.


### What is an octothorpe?
You have probably seen this symbol at some point:

```python
#
```
The proper name for this symbol is an octothorpe. However, I have heard the following names for it: Hash, Hashtag, Pound, Tic-tac-toe symbol etc. For the purposes of this book, I will refer to it as a hash. The hash has a special purpose that will be seen in the code you will write below.

```python
# octothorpe.py

# I can explain the code here

"""
I can do some lengthy explanations
here too. But this can span over 
multiple lines
"""

'''
Sometimes I want to use single quotes though
when I want to do this, Python doesn't care.
It just ignores me as long as I am consistent.
'''

print("Here is some text that will appear.") # comment
#print("Here is some text that will not appear.")

print("A good line of code is hard to find.")
""" print("But this line doesn't even work.") """

print("At last we can print again.")

""" 
print("none")
print("of")
print("these")
print("lines")
print("print")
"""

print("Well I guess we're done here.")
```
#### Here is what should happen

```
$ python octothorpe.py
Here is some text that will appear.
A good line of code is hard to find.
At last we can print again.
Well I guess we're done here.
$
```

Again if the result you get isn't *exactly* like the book's, go back in fix it until you get it right.

### About comments

As you may be able to gather from the code, the hash symbol tells Python, "Ignore everything after this on this line". The triple quotes (``` """```  or ```'''```) begin and end a block of text that can span as many lines as you want that Python will likewise ignore. (There are a few exceptions to this but we will cover them later.)

These are generally called "comments" in the code. They let the programmer make comments that either explain small bits of code or provide detailed explanations of his code. They also allow the programmer to disable a line or a chunk of code if desired. 

***NOTE:*** *Whenever you use quotes in Python, you must be consistent in whether you use single (`'`) or double (`"`) quotes to open or close text. Generally, it does not matter which you choose. The only requirement is that you are consistent.*

### Comment Conventions

The following rules of thumb apply to code comments and are demonstrated below (don't bother writing this all out, just read it):

```python
'''
File        : comment_conventions.py
Author      : Mark Redd
Version     : 1.0
Description :
It is common to have a header at the top of your file that 
has the filename, author and a general description of the 
program in the file. This space may also be used to 
include pertient data about the software such as its 
version number or the date it was last modified. In many 
cases, this header may be long and detailed depending on 
the intent of the programmer. This header is commonly called a 
"documentation string" or a "doc string".

For the purposes of this book, we will not worry about having
headers in our code until we tackle some larger, more complex
problems but it's good to know that these things exist.
'''

'''
Single line comments that explain code should be in 
one of two places:
'''

# By convention, this comment explains the next 
# line of code below it. The comment may be at 
# the end of the line as well if space permits
print("Here are some words") # an end-of-line comment

# If needed, the comment may span
# multiple lines. In any case, the comment 
# is generally above the line or block of code
# it explains.
print("Here are some more words")

"""
It is bad practice to write comments that trail off 
the visible screen. Later, we will explore code style 
and explain this convetion more fully.

Multi-line comments may be placed wherever appropriate 
to make general comments or explain a large block of code.
"""
```

I will put comments in the code I have you write. You do not need to put these in your code as well but sometimes I may have you explain your code line by line with comments. You may find it useful to take notes in the form of code comments as you write code to help you remember what you have learned.

## Hone Your Skills

1. Comment and uncomment some of the lines in the code you wrote. What can you make happen by uncommenting code?
1. Look up what Python Docstrings are. Why would you want to use them?

<!-- Navigation -->

---

[Previous: 04 - Hello World](./04-Hello-World.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 06 - Strings and the Print Function](./06-Strings-and-the-Print-Function.md)

---
<!-- End Navigation -->
