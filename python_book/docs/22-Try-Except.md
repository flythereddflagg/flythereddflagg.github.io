<!-- Navigation -->

---

[Previous: 21-More-Functions](./21-More-Functions.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 23-Imports](./23-Imports.md)

---
<!-- End Navigation -->
# 22 - Try Except

Surely you have noticed by now that errors can be common as you program. Well they are more than common. They are practically inevitable. In this lesson we will explore how you can "try" some code without letting it break your program.

```python
# try_except.py

month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

running = True

while running:
    date_string = input("Enter a date of the format: MM/DD/YYYY\n--> ")
    
    try:
        month, day, year = date_string.split("/")
        month, day, year = int(month), int(day), int(year)
        
        if day < 1 or day > 31:
            raise Exception("Invalid day value.")
        
        era = "B.C." if year < 0 else "A.D."
        year = abs(year)
        
        print(f"The date you entered was {month_names[month - 1]}"\
              " {day} in the year {year} {era}")
        running = False
    
    except Exception as e:
        print("Invalid Date detected!")
        print(e)
        
```

**Here is what should happen**

```
$ python try_except.py
Enter a date of the format: MM/DD/YYYY
--> 100/10/1230
Invalid Date detected!
list index out of range
Enter a date of the format: MM/DD/YYYY
--> 12/200/-30
Invalid Date detected!
Invalid day value.
Enter a date of the format: MM/DD/YYYY
--> 12/10/-100
The date you entered was December 10 in the year 100 B.C.
$
```

### The `try-except` Statement

Most of the time time in programming, you, the programmer, cannot guarantee that an error will not occur or an exception will not be thrown. You could try to prevent every problem with a series of if statements but   that becomes cumbersome and is difficult to cover every eventuality.

Python deals with this problem with `try-except` statements. A `try` statement will attempt to execute code in its corresponding block of indented code until an exception is "raised" or "thrown". If such is the case, then the `try` block stops and the `except` block is executed. If no exceptions are "raised" the except block is skipped. In `try_except.py`, we used the statement to deal with bad user input and invalid dates. The syntax is as follows:

```python
try:
    # Block of code you expect may
    # raise an exception
except:
    # this block runs if an exception is raised
```

You will notice that we added a part to the except line that reads `except Exception as e:`. This allows us to capture data about the Exception that was thrown but the `Exception` covers all exceptions that can be thrown in Python. If you wish to catch a particular exception or multiple types of exceptions you may do so with multiple `except` blocks as follows:

```python
try:
    # Block of code you expect may
    # raise an exception
except ZeroDivisionError:
    # this block runs if the 
    # try block tries to divide by 0
except TypeError:
    # this block runs if 
    # a type error is raised
except Exception as e:
    # this block runs for all other exceptions
```

Any exception in Python can be handled this way. When writing these statements one should always order them from specific errors to more general errors. This is because Python will execute the first valid `except` block it comes to. Therefore if you begin your list of except blocks with `except Exception:` no other `except` block will ever run.

These statements allow for writing more secure code that can handle any amount of garbage that is fed to it. Use these judiciously as overuse can clutter your code and silence bugs and issues in your programs. 

### Raising Exceptions 

We saw in `try_except.py` that we can force an exception to be raised with the `raise` statement. This is a powerful tool as it allows us to throw exceptions with customized messages. These can be very useful in debugging especially if we are careful about where we raise errors and what message we send. In our case we just wanted to send a general error to the user so a general `Exception` worked just fine here.

### Line Continuation

You may have noticed the snippet of code from `try_except.py`:

```python
print(f"The date you entered was {month_names[month - 1]}"\
              f" {day} in the year {year} {era}")
```

The backslash `\` at the end of the line is called a "line continuation character" and allows us to split long lines of code into multiple lines that are interpreted as one line of code. These are useful when you are trying to limit the length of your lines for ease of reading.

## Hone Your Skills

- Change the code to catch specific exceptions such as a `TypeError` and others. Try to do multiple `except` statements. How does this improve your code's usability?
- Change the code to `raise` some errors when a date is invalid. Does your message help the user understand what went wrong?
- Experiment with the security of this script. Try to break it or make it produce invalid dates. You may notice some dates that can be written are invalid. Rewrite this script so that it cannot produce an invalid date according to the [Gregorian Calendar](https://en.wikipedia.org/wiki/Gregorian_calendar). (Go as detailed as you like, but at least account for basic leap years and months having different lengths.)
- Notice the string method `.split()`. What does this do? Research and learn exactly what this method does and how you can use it.

## Advanced Mastery

- What is a [User-Defined Exception](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions) and why would you want to use one?
- What is the [`finally`](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions) statement for and why would you need it?

<!-- Navigation -->

---

[Previous: 21-More-Functions](./21-More-Functions.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 23-Imports](./23-Imports.md)

---
<!-- End Navigation -->
