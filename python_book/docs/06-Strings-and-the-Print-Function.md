<!-- Navigation -->

---

[Previous: 05 - Comments ](./05-Comments.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 07 - Escape Characters](./07-Escape-Characters.md)

---
<!-- End Navigation -->

<!-- How to make text appear on hover <span title="I am hovering over the text">This is the text I want to have a mousover</span> -->

# 6 - Strings and the print function

## The print function 

Let's talk about the `print()` statement or, as it is more correctly called, the print function.

`print` is what is known as a built-in function in Python. Let's get some terminology out of the way before moving on:

- **Function**: A chunk of code that you can run using a single line of code. This single may be used multiple times to reuse the code in various places.

We will learn a lot more about functions later on and you will even build your own. But for now, just understand the following:

- There is some chunk of code labeled `print` in the Python <span title="source code: Text files written in a particular programming language. Not to be confused with the program itself.">**source code**</span>.
- When you write `print(stuff)` in your code you are telling the computer, "Activate that chunk of code labeled `print`!"
- The chunk of code then comes alive and says, "Okay! My job is to write the `stuff` between the parentheses in the terminal window!"
- The chunk of code does just that and then becomes dormant awaiting the next time it is called to action. 

When we talk about functions you will see that they have things (such as `stuff` above) between the parentheses. Sometimes these things are in a comma-separated list. These things between the parentheses are called <span title="arguments: Values and variables passed into a function.">**arguments**</span>. For now, we have just one argument being fed to the `print` function and that is simply the text you want printed out to the screen. 

## Strings

You may have noticed that the text inside the parentheses is also between single or double quotes. It may not be clear why this is. In Python, putting text inside quotes designates it as a string.

- **String**: a sequence of characters that is treated as non-code text

The quotes are necessary to differentiate between code being fed into the print statement and the text to be printed.

If you want to print single quotes (`'`) in your text you can do this by enclosing the text with double quotes (`" "`) or vice versa. Python does not care if you use single or double quotes to enclose your strings as long as you are consistent.

We will illustrate this in the next exercise:

```python
# string_quotes.py

print("This is a string:")
print("with'double' quotes but 'single quotes' inside it.")
print('with "single" quotes but "double quotes" inside it.')
print("mixing "double" and'single' quotes will cause an error.")
```

#### This is what should happen

(If needed, see [Section 4](./04-Hello-World.md#making-and-running-your-first-python-file) to review how to run a script.)

```
$ python string_quotes.py
File "string_quotes.py", line 6
 print("mixing "double" and'single' quotes will cause an error.")
                   ^
SyntaxError: invalid syntax
$
```

If we comment out the last line,

```python
# string_quotes.py

print("This is a string:")
print("with'double' quotes but 'single quotes' inside it.")
print('with "single" quotes but "double quotes" inside it.')
#print("mixing "double" and'single' quotes will cause an error.")
```

we will get:

```bash
$ python string_quotes.py
This is a string:
with'double' quotes but 'single quotes' inside it.
with "single" quotes but "double quotes" inside it.
$
```

When ever you make a string by using quotes always remember to be consistent 
with your use of single and double quotes or you will run into problems.

## Advanced Mastery

**Remember:** It is not required to figure out everything in these sections. Advanced Mastery is for those who are especially curious or wish to do more to understand the topics explained above. If you want you can skip this part and move on to the next section.

- Look up strings as they relate to computers. How are strings represented by a computer?

<!-- Navigation -->

---

[Previous: 05 - Comments ](./05-Comments.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 07 - Escape Characters](./07-Escape-Characters.md)

---
<!-- End Navigation -->
