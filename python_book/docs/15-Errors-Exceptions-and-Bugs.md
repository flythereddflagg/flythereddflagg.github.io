# 15 - Errors, Exceptions and Bugs

We are going to "break" Python in a lot of ways in this section. Your assignment for this section is to fix all the problems in the following script. For the purposes of this exercise, here is how you should go about doing this:

- Write out the code exactly as it appears as always
- Try to run it
- Each time it breaks or throws an error, fix the error
- Continue running the script and fixing each error that comes up until the script runs without any errors

```python
# errors.py

fav_number = input("Please enter your favorite number: "

fav_number = float(fav_number)

# there is a line of code missing here

# pi is the same as π and should have a value of 3.14
if fav_number > pi
    print("Your number is bigger than pi!")
else:
    print("Your number is less than or equal to pi!")
    
print("You can print all sorts of "numbers" given by the user.")
```

**Here is what should happen**

This is what should happen as you run it. You should be fixing the problems with the script between each time you attempt to run it.

```bash
$ python3 errors.py 
  File "errors.py", line 5
    fav_number = float(fav_number)
             ^
SyntaxError: invalid syntax
$ python3 errors.py 
  File "errors.py", line 5
    fav_number = float(fav_number)
             ^
SyntaxError: invalid syntax
$ python3 errors.py 
  File "errors.py", line 9
    if fav_number < pi
                     ^
SyntaxError: invalid syntax
$ python3 errors.py 
  File "errors.py", line 14
    print("You can print all sorts of "numbers" given by the user.")
                                             ^
SyntaxError: invalid syntax
$ python3 errors.py 
  File "errors.py", line 14
    print("You can print all sorts of \"numbers" given by the user.")
                                                     ^
SyntaxError: invalid syntax
$ python3 errors.py 
Please enter your favorite number: 23
Traceback (most recent call last):
  File "errors.py", line 9, in <module>
    if fav_number < pi:
NameError: name 'pi' is not defined
$ python3 errors.py 
Please enter your favorite number: 23
Your number is less than or equal to pi!
You can print all sorts of "numbers" given by the user.
$ python3 errors.py 
Please enter your favorite number: 23
Your number is bigger than pi!
You can print all sorts of "numbers" given by the user.
$ python3 errors.py 
Please enter your favorite number: 23d
Traceback (most recent call last):
  File "errors.py", line 5, in <module>
    fav_number = float(fav_number)
ValueError: could not convert string to float: '23d'
$ 
```

### Errors and Exceptions

I am using the term "error" loosely here. In reality, there was a time when an error was the computer equivalent of certain death. You see, Python has all sorts of protections and carefully constructed walls up to protect the programmer from him or herself. But it wasn't always this way. Older languages such as C (especially in their earlier years) were perfectly happy to let you crash your entire computer. (It turns out that you could also destroy your hardware too but that's another can of worms we are not getting into here.) From the stand point of these programming languages, an error is a death sentence, at least, for the program in which it occurs. Not to mention, there were potentially a lot of weird side effects from a program that just stopped running unexpectedly.

To deal with the problems that this caused, languages like C++ introduced the concept of an "exception" in which an error could be caught and handled without breaking the program or computer. In Python, there are no such things as "errors", at least in the sense that is described above. Everything is an exception. This means that Python is a relatively forgiving language. You can put any amount of junk in there and generally it will keep you from causing major problems. In fact as you have seen by now, Python does everything it can to help you understand what went wrong and sometimes even tells you how you can fix it.

I mentioned in an earlier section that "There is no such thing as perfect code". I mean it. Even when you write the simplest programs there are hundreds if not thousands of little things that have to go right for you to get a desired result. 

And I want you to understand this now as well. You will make mistakes. This doesn't necessarily make you a bad programmer. Mistakes are almost inevitable. What I want you to get from this lesson is to not fear making mistakes and to know how to fix them when you make them. To that end we will now go over the kinds of exceptions and errors you will run into and how they can be fixed.

#### Syntax Errors

*When Python says, "I have no idea what you are saying."*

This is the simplest problem to fix and is also the most common mistake  most programmers make. Syntax errors occur when you make mistakes such as forgetting to close parentheses. When you make these mistakes Python cannot even understand what you are telling it to do.

When you run a command on the CLI like `$ python a_script.py`, Python first passes over the whole script file scanning for syntax errors. Before running any code Python has to make sure that you're giving it valid Python code to parse and run. Once this is done, it begins executing the script line by line until the file ends or an exception is thrown. Therefore you may have noticed that none of your script ran until you fixed everything that was considered a `Syntax Error`.  (See "Hone Your Skills" for more on this subject.)

#### Exceptions

*When Python says, "I know what you're saying but I can't do that."*

Once Python starts executing code there are many things that can go wrong. Mostly, these consist of you asking Python to do things it was not designed to do. An obvious example is when you attempt to divide by 0 in Python. You can try this by opening the Python interactive prompt and typing `>>> 1/0`. This error occurs because you are telling Python "Divide 1 by 0" to which Python replies "I have no idea how to do that," and throws an exception. The programmer has to be aware of what these exceptions mean and how to handle them.  (See "Hone Your Skills" for more on this subject.)

#### Warnings

*Soft exceptions. Python says, "I can do that but you're going to have a bad time."*

A warning is like an exception but it doesn't stop the script execution. Generally, you will see warnings when you are getting close to the limits of what Python can do or Python couldn't do *exactly* what you wanted.

There are many different Syntax Errors, Exceptions and Warnings that are built in to python. It is a good idea to learn about as many as you can. (See "Hone Your Skills" for more on this subject.)

#### Logic errors

*When it's not Python it's you. You are not doing what you think you are doing*

Did you notice that I put the wrong comparison operator on the line that says `if fav_number < 3.14`? You should have realized that the wrong operator was being used and switched it for `>`. This is an example of a logic error, the hardest kind of error to detect and fix. This is mainly because Python has no idea anything is going wrong. Python is only executing the commands you gave it. If you give Python the wrong commands you cannot expect it to give you the right result.Later on, you will get a chance to make and fix your own logic errors.

#### User Errors

*You were not prepared for the tidal wave of junk coming your way.*

Users are stupid. Repeat that 3 times. Get it tattooed on your forehead. Engrave it in your grave stone. One thing to always remember about using the `input` function is that when you put that in your code you are asking for your program to be abused. You must be ready to handle the situation whatever that may be. A few examples are when you want a number but the user gives you letters or when you want a certain word but the users gives you that word misspelled.

With all that said, we will cover how to deal with bad user input in later lessons. But for now just understand that you have no guarantee what your user will provide as input. We saw this in the output for `errors.py` when the user input `23d` for their favorite number. The error happened when Python tried to turn the the string `"23d"`  into a number. Python didn't know what to do with it and threw an exception.

### Bugs and debugging

There is a story that you can read in detail [here](https://en.wikipedia.org/wiki/Software_bug#Etymology). The story goes that in one of the earliest computers a system failure occurred when a moth got stuck inside the computer. Since then, the terms "bugs" and "debugging" are a catch-all terms for exceptions and logic errors in a program and the process of identifying and fixing these errors respectively. Much of what programmers do involves debugging programs. 

As I noted above, the hardest thing to fix is logic errors. Later we will go much more into detail about debugging such errors. However for the purposes of lesson, the above strategy of running and fixing until all the errors disappear is sufficient. Just note for now that this is not the only way nor necessarily the best way of debugging.

## Hone Your Skills

- Go to the [Python Documentation](https://docs.python.org/3/tutorial/errors.html)  on errors and exceptions and learn about as many of them as you can. How can you avoid each type of exception? If you come to one that you don't understand don't worry, you'll understand more as you go along.
- Research defensive programming and test-driven development. How do these practices improve code?

## Advanced Mastery

- Research and begin to learn how to use the [Python Debugger](https://docs.python.org/3/library/pdb.html). This will be more useful for more for larger and more complex programs.

- Research debugging strategies and begin to implement them in your programs.

