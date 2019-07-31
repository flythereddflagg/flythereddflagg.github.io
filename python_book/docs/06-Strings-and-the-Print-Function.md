
# 6 - Strings and the print function

###  The print function 

Lets talk about the print statement or as it is more correctly called, the print function.

"print" is what is known as a built-in function in Python. Let's get some terminology out of the way before moving on:

- **Function**: A chunk of code that you can reuse multiple times with a single line of code.

We will learn a lot more about functions later on and you will even build your own. But for now, just understand the following:

- There is some chunk of code labeled 'print' out there in the Python ether 
- When you write `print(stuff)` in your code you 
  are telling the computer, "ACTIVATE THAT CHUNK OF CODE LABELED 'print'!"
- The chunk of code then comes alive and says,
  "Okay! My job is to write the `stuff` between the parentheses  in the terminal
  window!"
- The chunk of code does just that and then becomes dormant awaiting 
  the next time it is called to action. 

When we talk about functions you will see that they have things (such as `stuff` above) between the parentheses. Sometimes these things are in a comma-separated list. These things between the parentheses are called **arguments**. For now, we have just one argument being fed to the `print` function and that is simply the text you want printed out to the screen. 

### Strings

You may have noticed that the text inside the parentheses is also between single or double quotes. It may not be clear why this is. In Python, putting text inside quotes designates it as a string.

- **String**: a sequence of characters that is generally treated as non-code 
  text

The quotes are necessary to differentiate between code being fed into the print
statement and the text to be printed.

If you want to print single quotes (`' '`) in your text you can do this by enclosing the text with double quotes (`" "`) or vice versa. Python does not care if you use single or double quotes to enclose your strings as long as you are consistent.

```python
# string_quotes.py

print("This is:")
print("a string with 'double' quotes enclosing it but 'single quotes' inside it.")
print('a string with "single" quotes enclosing it but "double quotes" inside it.')
print("This will cause an error because I am mixing "double" and'single' quotes.")
```

**This is what should happen**

```
$ python string_quotes.py
File "string_quotes.py", line 6
    print("This will cause an error in Python because I am mixing "double" quotes with 'single' quotes.")
                                                                        ^
SyntaxError: invalid syntax
$
```

If we comment out the last line we will get:

```python
# string_quotes.py
print("This is:")
print("a string with 'double' quotes enclosing it but 'single quotes' inside it.")
print('a string with "single" quotes enclosing it but "double quotes" inside it.')
#print("This will cause an error because I am mixing "double" and'single' quotes.")
```

```
$ python string_quotes.py
This is a string with 'double' quotes enclosing it but 'single quotes' inside it.
This is a string with "single" quotes enclosing it but "double quotes" inside it.
$
```

When ever you make a string by using quotes always remember to be consistent 
with your use of single and double quotes or you will run into problems.

## Advanced Mastery

- Look up strings as they relate to computers. How are strings represented in computer language?

