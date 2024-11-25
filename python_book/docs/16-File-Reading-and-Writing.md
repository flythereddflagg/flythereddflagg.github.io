
# 16 - File Reading and Writing

When we talked about variables and memory I mentioned that there were three basic parts to the computer. They are:

- The CPU
- The RAM or volatile memory
- The persistent memory (i.e. the storage drive)

This lesson is an opportunity to interact with the third part, that is the hard drive. We will learn in this lesson how to read and write files from the storage drive.

```python
#io_files.py

ext       = '.txt'
user_name = input("Enter your name       : ")
user_age  = input("Enter your age        : ")
user_job  = input("Enter your occupation : ")
filename  = input("Enter a valid filename: ")

# let's print out what we got from the user
print(f"\nHello {user_name}! You are {user_age} years old.")
print(f"You work as a/an {user_job}")
print(f"\nSaving Your Information to \"{filename + ext}\"...", end="")

data  = user_name + "," # concatenate a string of data
data += user_age  + ','  
data += user_job  + "\n" 

# an example of the older/worse way of working with files
f = open(filename + ext , "w")   # open in write mode "w"
f.write("name,age,occupation\n") # write column headers to file
f.write(data)                    # then write data to the file
f.close()                        # save and close the file
    
print("Done.")

# better way of working with files
# always use 4 spaces to indent
with open(filename + ext, 'r') as f: # 'r' is for read
    data = f.read()                 
    print("\nHere are your data:\n---")
    print(data)
    print("---")

```
### Here is what should happen

```
$ python io_files.py
Enter your name       : Mark
Enter your age        : 92
Enter your occupation : Professional Old Guy
Enter a valid filename: mark_info

Hello Mark! You are 92 years old.
You work as a/an Professional Old Guy

Saving Your Information to "mark_info.txt"...Done.

Here are your data:
---
name,age,occupation
Mark,92,Professional Old Guy

---
$
```

If you open the file `"mark_info.txt"` that should have appeared in the same folder you will see the following:

```
name,age,occupation
Mark,92,Professional Old Guy

```

**What is happening here?**

We are writing and reading files here with a special tool called a file object. A file object from Python's point of view is another data type although that is not the most convenient way of understanding it. Without going too much into detail here is what is happening:

- We get some data from the user and print it out for reference. (Lines 3-12)
- We organize this data into a table where the rows are separated by newline characters (`\n`) and the columns are separated in each row by commas (`,`). We give this table headers and concatenate this string all together using the addition operator. (Lines 14-16)
- We call `open` on a string containing a filename which returns a file object. (Line 19)
- We feed appropriate method statements to the file object to read, write. (Lines 20-21)
- The file object is altered as we use the file object's methods.
- We then save and close the object. (Line 22)
- Finally, we re-open the file in "read" mode using a `with` statement and print the contents of the file out to the screen. (Lines 28-32)

Some of these topics and nomenclature are new. I will now explain these below.

## Objects

In Python, every variable you work with is an object. Objects are instances of types just as you are an instance of a human. Read that last sentence again.

A type, as I explained before, is a marker that a computer puts on a 'box' or set of 'boxes' in the RAM. It is a label that lets the computer know how to work with those boxes. An object is the actual box or set of boxes themselves.

For example, when you have a string variable such as `"Tim {}"`, you have a set of 'boxes' in a certain order and each box has a bunch of 1s and 0s that represent each character in "Tim {}". In addition, you have other sets of boxes that contain code that makes the string object's methods work (e.g. `"Tim {}".format("The Enchanter")`) and any other data the string needs to function properly. Collectively, all these boxes are grouped together in memory and constitute the string object. This nomenclature will be used often so it's important to internalize this concept early.

Other objects we have talked about such as `int` and `float` are also objects but are significantly simpler than strings. These generally have very simple data and methods associated with them but they still have the same fundamental structure as the string objects. 

## File Objects and Methods

Now that we have discussed objects lets look specifically at file objects. Lets begin with the `open` built-in function. The basic usage for the open function has the following form and arguments:

- `open(filename, mode)`

where `filename` is the path to the file you want to open and `mode` is the way you want to open the file. The basic ways you can open a file are:

- `'r'` for read mode. In this mode the file can only be read (this is sometimes called "read-only" mode). This is the default mode, meaning if you do not give the `open` function a mode, it will assume read mode. Because you are in read mode, operations like `.write()` will throw an error. Also, if the filename you put into `filename` doesn't exist that will also throw an error.

  The `.read()` method returns the entirety of the file as a string. Experiment with this function. What happens when you try to call `.read()` twice?

- `'w'` for write mode. Write mode will automatically overwrite whatever was previously in the file. This may also be considered a "write-only" mode, meaning methods like `.read()` will throw an error. However, unlike read mode, if the filename does not exist, `open("filename.txt", 'w')` will create a new file with the name "filename.txt".

- `'a'` for append mode. This mode is like write mode in that methods like `.read()` will throw an error.  It is also like read mode in that if the filename doesn't exist it will also throw an error. It is used to write without truncating and simply appends text to the end of files. However using methods like the ones [here](https://docs.python.org/3.7/library/io.html#class-hierarchy), you can edit files directly. (With that said and depending onthere are better ways to do this that we will cover later.)

 These are not the only options for `mode` and there are ways to combine these that you can experiment with in "Hone Your Skills" below.

## `with` Statements

To save the changes we made to the file we opened in `f = open(filename + ext , "w")`, we need to call `f.close()` on our file object. This ends up being a problem if you forget to call `f.close()` on the object. A better way to deal with files is with a `with` statement. 

To be clear, the following code snippet:

```python
f = open(filename + ext , "w")  
f.write("name,age,occupation\n")
data  = user_name + ","         
data += user_age  + ','  
data += user_job  + "\n" 
f.write(data)                   
f.close()                       
```

is equivalent to:

```python
with open(filename + ext , "w") as f:
    f.write("name,age,occupation\n")
    data  = user_name + ","  
    data += user_age  + ','  
    data += user_job  + "\n" 
    f.write(data)     
```

Not only does the second code snippet use fewer lines of code but it is clear by looking at the indented block when you are working with the file and when you are done. The `with` statement simply remembers to close the file when the indented block ends. Whenever you work with files you should always use a `with` statement (unless you have a *very* good reason not to do so). Also note that working with files is not the only situation in which it is appropriate to use a `with` statement but it is a very common one.

## A Quick Note About Function Arguments

You may have noticed the following feature of the `print` function on Line 12  that we have not used before:

```python
print(f"\nSaving Your Information to \"{filename + ext}\"...", end="")
```

You may have rightly wondered what that business about `end` was. `end` is an optional argument in the print function. Normally when you use the print function, what is actually being printed is the string or arguments you give to the print function and a newline character (`\n`) is automatically appended to the end of the printed text. `end` is an argument that you must call by name, as seen above but with it you may override the default `'\n'` with anything else you wish. In the exercise we are just using an empty string.

## Hone Your Skills

Remember to use `with` statements in all the following exercises.

- Try using the three basic ways of writing files (`'r','w','a'`). Try to write a paragraph of text to a file, close it and edit it again, putting a line of text at the beginning and end of the file. How would you do this?
- Experiment with the ways of opening a file by trying the combined and other options (e.g. `r+`,  `'wb+'` etc.) for opening files. You can read about them [here](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files). How do they differ?
- Research the `open()` function and learn all you can about how it works. The official Python reference is [here](https://docs.python.org/3.9/library/functions.html#open).
- Look up all the file operation

## Advanced Mastery

- Try to open and read a non-.txt file with Python. Were you able to read it? Research why or why not.
- Read about the complete list of methods for working with files [here](https://docs.python.org/3.9/library/io.html#class-hierarchy). How could you use these methods?

