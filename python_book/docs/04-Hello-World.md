<!-- Navigation -->

---

[Previous: 03-CLI](./03-CLI.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 05-Comments](./05-Comments.md)

---
<!-- End Navigation -->

# 4 - Hello World!

If you have sucessfully installed Python and are able to do basic navagation in the command line, you are ready to begin programming in Python!

We will begin with the most basic program that actually does something in 
Python. This is common when you want to begin any programming language. As with
all things, beginning in Python is very simple.

#### Making your first Python source file

- Start by opening your text editor and opening a new file

- Pick a folder to keep all your Python learning files in. This could be in your home folder but I recommend making a new folder, calling it something like `python_exercises` and putting it in your "Documents" folder. However, you can put it wherever makes sense.

- Use the 'Save as' dialog and navagate to the folder you made.
   
- Give the file the name `hello_world.py` and save it
   
You will notice the `.py` part of the filename. This is called an extension and 
   is a way of telling the computer or anyone who looks at the file what kind of 
   file it is. Make sure you name all files you make in Python using this extension.
   
   Also it is good practice to never use spaces when naming files used in
   programming. Use underscores (`_`) instead of spaces. There are reasons for this but 
   just for now trust me when I say that you are avoiding a lot of confusion and 
   problems if you just commit to never using spaces in your filenames when you 
   write code.
   
   **NOTE: I will give you the name of each filename you should be using for each
   exercise in this book. When you see an octothorpe (`#`) followed by a filename at the beginning of a code example, it means I want you to make a new file with that name by following the steps above.**
   
- Type the following *exactly* as it is written here. Do *not* copy-paste it.

```python
# hello_world.py
print("Hello World!")
```

- Go to your terminal and navigate to the folder that holds your Python file. *(if you have trouble doing this, review the previous section until you can navigate the terminal with confidence.)*
- Enter the following command in your terminal:

```
$ python hello_world.py
```

*(Remember, DO NOT type in the `$` and ignore everything in the terminal before the `$` or the `>`)*

**Here is what should happen**

```
$ python hello_world.py 
Hello World!
$ 
```

If you see the above output, congratulations! You have just written and run your first Python program!

**What is happening here?** 
Traditionally, displaying "Hello World!" in a console window is the first thing every programmer generally learns to do in a new language. Later we will get into more detail on how exactly everything works and what is happening on a fundamental level.

Go back to your Python file and add the following under the first line so the whole file looks like this:

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

**Here is what should happen** 

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

This is generally how each section in this book will work. In each section, I will have you write some code and then we will go back and try to understand it.

## Hone Your Skills

This is the simplest type of program that exists in Python (i.e. simple statements in a ordered list). Now is a good time to get used to some fundamental concepts:

- **There is no such thing as perfect code**

  It is likely that unless you were paying very careful attention to what you were doing that you made a mistake. In which case you may have gotten an error such as the one below

  In Example 1 below, I deleted the last three characters on line 8 and got this message. As you can see, Python tells me exactly where my mistake is and what kind of error it is. 

  Take some time and mess with this program. Delete different parts and try to run it and see the kind of errors you get. 

  My hope is that you'll get two things out of this: First, don't be afraid to make mistakes (although you will, of course, want to avoid them where possible) and secondly, when an error does happen, this should help you begin to be comfortable with how python reports errors and exceptions. We will cover these in more detail in a later lesson.

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

<!-- Navigation -->

---

[Previous: 03-CLI](./03-CLI.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 05-Comments](./05-Comments.md)

---
<!-- End Navigation -->
