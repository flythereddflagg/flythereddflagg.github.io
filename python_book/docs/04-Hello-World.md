
# 4 - Hello World!

If you have successfully installed Python and are able to do basic navigation in the command line, you are ready. Lets actually do some programming now! We will begin with one of the most basic programs in Python which is called the "Hello World" program. This is common when you want to begin any programming language.

## Let's make your first program!

- Start by opening your text editor and opening a new file
- Pick a folder to keep all your Python learning files in. This could be in your home folder but I recommend making a new folder, calling it something like `python_exercises` and putting it in your "Documents" folder. However, you can put it wherever makes sense. 
- Use the `File -> Save As` dialog and navigate to the folder you made.
- Give the file the name `hello_world.py` and save it

You will notice the `.py` part of the filename. This is called an **extension** and is a way of indicating what kind of file it is. Make sure you end all Python files you make with this "`.py`" or you will run into problems.

Also it is a good idea to *never* use spaces when naming files used in programming. Use underscores (`_`) instead of spaces. There are reasons for this but, just for now, trust me when I say that you are avoiding a lot of confusion and problems if you just commit to never using spaces in your filenames when you write code.

***NOTE:*** *You can name Python files anything you want to. However for our purposes, I will give you the name of each filename you should be using for each exercise in this book. When you see an octothorpe (`#`) followed by a filename at the beginning of a code example, it means I want you to make a new file with that name by following the steps above.*

- Type the following *exactly* as it is written here. Do *not* copy-paste it.

```python
# hello_world.py
print("Hello World!")
```

- *Make sure you save the file*
- Go to your terminal and navigate to the folder that holds your Python file. *(if you have trouble doing this, review the previous section until you can navigate the terminal with confidence.)*
- Enter the following command in your terminal (Remember, **DO NOT** type in the `$` and ignore everything in the terminal before the `$` or the `>`):

```bash
$ python hello_world.py
```

### Here is what should happen

```bash
$ python hello_world.py 
Hello World!
$ 
```

If you see the above output, congratulations! You have just written and run your first Python program!

If this did not work try the following:

- Look where you saved `hello_world.py` have you navigated to the same folder in the command line? If not navigate to the folder `hello_world.py` is in before trying again.
- Did you write *exactly* what was written above? Check it carefully before trying again.
- Check that Python is working. Type "python" or "python3" into the terminal like it says in [Section 2](./02-Getting-Started.md). Does it work as it says there? If not check the [Troubleshooting Section](./02-Getting-Started.md/#troubleshooting-your-installation) in Section 2.

### So, what did I just do?

Traditionally, displaying "Hello World!" in a console window is the first thing every programmer learns to do in a new language. Later, we will get into more detail on how exactly everything works.

## You made a program! Now do it again.

Go back to your Python file and add the following under the first line so the whole file looks like this (Again, type it *exactly* as it is written here):

```python
# hello_world.py
print("Hello World!")

print("I skipped a line in code!")

print("Here is a little song:")
print("Twinkle, twinkle little star,")
print("How I wonder what you are.")
print("Up above the world so high,")

print("Like a diamond in the sky")
print("Twinkle, twinkle little star")


print("How I wonder what you are.")
```

### Here is what should happen

Re-run the code as before and you should see the following:

```
$ python hello_world.py 
Hello World!
I skipped a line in code!
Here is a little song:
Twinkle, twinkle little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky
Twinkle, twinkle little star
How I wonder what you are.
$ 
```

As you can see here, the code runs in order line by line, ignoring any blank lines. This is how any python program works. It starts on line 1 and executes each line of code until it reaches the end of the file. 

If you did not get the above output *exactly* as it appears above or you got some error, review the code above and everything we have covered so far until the output matches the above output *exactly*.

Once you see the output appear *exactly* as it appears above, congratulations! You have completed the first exercise!

**Note:** *This is generally how each section in this book will work. In each section, I will have you write some code and then we will go back and try to understand it.*

## Hone Your Skills

This is the simplest program that exists in Python (i.e. simple statements in a ordered list). Now is a good time to get used to some fundamental concepts:

- **There is no such thing as perfect code**

  It is possible that, unless you were careful, you made a mistake. In which case you may have gotten an error such as the one below.

  In Example 1 below, I deleted the last three characters on line 8 and got this message. As you can see, Python tells me exactly where my mistake is and what kind of error it is. 

  Take some time and make changes to this program. Delete different parts and try to run it and see the kind of errors you get. 

  My hope is that you'll get two things out of this: First, don't be afraid to make mistakes (although you will, of course, want to avoid them where possible) and secondly, when an error does happen, this should help you begin to be comfortable with how Python reports errors and exceptions. We will cover these in more detail in a later lesson.

**Example 1: Python Error Reporting**

```python
File "hello_world.py", line 8
    print("How I wonder what you are
                    ^
  SyntaxError: EOL while scanning string literal
```

- **"Sparse is better than dense"**

  From "[Zen of Python](https://www.python.org/dev/peps/pep-0020/)" there is a line that says, "Sparse is better than dense". This refers, in part, to the fact that it is often much easier to read code when there is some white space in between lines. When you write code you should be organizing it in your mind and this should reflect in how the code is written.

  Look back at the code that you wrote down from this lesson. Does the spacing make sense? How would you change the spacing to be more consistent? Would you add more lines here or fewer there? Rewrite the code to reflect your mental understanding of the code.

