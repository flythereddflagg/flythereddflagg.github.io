<!-- Navigation -->

---

[Previous: 24-Reading Code](./24-Reading-Code.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 26-Objects and Classes](./26-Objects-and-Classes.md)

---
<!-- End Navigation -->
# 25 - Do a Project

It is now time to put your new found skills to use! You have learned enough in Python to find out how to solve many of your own problems. Now your assignment is to integrate everything you have learned into a project. My only requirement is that the project must interact with a user and the user must have some measure of control over what happens in the program. There are two basic ways this can be done. The first is by using the `input` function as we have covered. Another way is to use `sys.argv` (i.e. the `argv` variable from the `sys` module).

Before you get started, make sure you read the entirety of this lesson before deciding what to do. The next few sections are important concepts that will aid you as you synthesize your first fully featured program. This section also has an appendix with a quick introduction to some minor things we have not yet covered that you may find useful.

Have fun with this. Think about why you started this in the first place. This may not be a perfect program but it will be a great learning and growing experience for you as a programmer. Remember that the internet is your friend and 99% of questions you have can be found there. Good luck!

## Styling Code

Before you begin coding you should make sure you are styling your code correctly. Up to now you should have been following my code along and styling it as I have in each example. To make your code easy to debug and easy to read as possible you should continue to use good style practices in Python. 

Before doing any coding, read Python's style guide called [PEP-8](https://www.python.org/dev/peps/pep-0008/#introduction). Commit to using these conventions to make your code readable and easier to debug. Once you have practiced this style enough you will be able to follow and debug your code much more easily. 

## Debugging

Inevitably you may run into situations where your code is doing unexpected things (think 'logic errors' from the lesson on errors exceptions and bugs). Fixing these errors is not a trivial process. In fact by some estimates, programmers generally spend 50 - 75 percent of their time just debugging their programs! The following are some simple strategies used by professionals to avoid debugging or effectively debug their software:

- **Plan Ahead**

  The best way to fix bugs is to do your best to ensure that they never happen. You can plan your code so you have an idea of where you want to be when you finish up.

  Before you write any code at all, pull out a pencil and paper or open up a drawing software like [draw.io](https://www.draw.io). Make an outline and write down in general what your code will do. Then get more specific by specifying how it will do it. Repeat this process until you have a general idea of what you need to code the project and the logic it will follow. This can be a flow chart or a list of function names and descriptions of what they do. This can be a difficult habit to follow but rest assured that doing good planning up front will save you a large amount of time debugging later on.

- **Use Good Coding Practice**

  One strategy that should probably go without saying is to use good coding practice while you work. The following are some suggestions used by professionals to make 

  - Ensure you are following the [Python Style Guide](https://www.python.org/dev/peps/pep-0008/). Good style makes code easy to read and therefore  easier to debug.
  - Use descriptive variable names that make clear the purpose of a variable
  - Follow the principles found in the [Zen of Python](https://www.python.org/dev/peps/pep-0020/#id3) 
  - Document your code as you go. It is easy to forget what your code is doing. If you leave notes for yourself you are less likely to get lost.

- **Do a little at a time**

  There are two general approaches to implementing a large project. The first it s a "Top-Down" approach where you get the simplest version of the program working and add features, fleshing out the auxiliary parts of the program as you go. The other is the "bottom-up" approach where you get one little part of the program to work at a time. Once enough parts are working independently, you link them together. Both have advantages depending on the application but for this first attempt at a larger program I will recommend doing the bottom-up approach. As you go, decide what each part of the program must do and get each part working before you link them together.

- **Test-Driven development**

  As you build your code up you will inevitably run into errors. One of the best ways to avoid difficult-to-debug logic errors is to implement test-driven development. The process of test-driven development is simple to understand. Before writing any code you write code that tests the function or you will write. The test should be written to get certain outputs of inputs to the function. You will want to write tests that test the normal cases and the edge cases of your function. Once the tests have been written and you have ensured that they work (a relatively simple coding task), write your code so it passes those tests. If you have written good tests then the code will act as you expect it to.

- **Getting intermediate values**

  Everything we have listed above is about how to prevent errors. Eventually you will have to go in and figure out how you messed up. When this happens getting intermediate values will help you see what your code is doing.

  - Use the print function to print out values as you go. 
  - Start by ensuring that you are getting the input you think you are. 
  - Then check your loops are doing what you think they are by going through just one iteration (i.e. use a `break` statement to end the loop early).
  - Finally, check your returns so you know you are getting back what you think you should be getting back.

  This is not an exhaustive list of strategies. But the simple act of checking intermediate values will help you a lot as you go along.

- **Explain it to a rubber duck**

  This is one of the weirdest and most effective strategies used by programmers. More detail about it can be found [here](https://en.wikipedia.org/wiki/Rubber_duck_debugging). The idea is to explain your code out loud to a rubber duck (although you could explain it to another person too if they were willing to listen for that long).  As you explain the code out loud you will find that often the solution to your problem will occur to you. This is a strange practice but has been shown to be a powerful debugging too to help you gain clarity about what is going wrong.

- **"If you cannot solve your problem, solve an easier problem first." - Dr. David Lignell**

  Taken from [here](https://ignite.byu.edu/che541/programming_tips.html). This is a good tip for you if you find yourself at a dead end. Split up your problem into parts and tackle each one at a time. For example, split your code into shorter sub-functions and debug each of them.

## Possible Projects

There are many different things you may want to do with your newfound skills. In reality, this project will be the most valuable thing you do yet as it will introduce problems you have not yet faced and develop skills you have not yet even thought of. Ideally, you will make something that interests you and feeds your passions. Below I have provided some general ideas and perhaps a push in the right direction. However, you must flesh out the ideas here and make them your own. Please note that right now, everything you will do will interface with your user in the command line. This however does not mean that you cannot make something interesting or useful. With that said, here are some possible projects.

### Design A Game

Video games back in earlier days of computing were all based in the command line. A popular one that was among the first video games was called "Zork". Search the Internet for information about Zork and make your own little version. A tiny version of a Zork-like might look like:

```python
def entrance_hall():
    look = """
You find yourself locked inside a castle.
You are in the entrance hall to the palace.
To the SOUTH there is a locked door to the outside.
To the NORTH there is a staircase.
To the EAST and WEST there are large wooden doors
standing ajar.
"""
    print(look)
    do = input("What will you do? > ")
    
    if do == "go north":
        staircase()
    elif do == "go south":
        print("You're pretty bad at this game.")
    elif do == 'go east' or do == "go west":
        east_west_rooms()
    else:
        print("You lose. Next time try doing something",
              "like 'go <direction>' to do something.")

def staircase():
    look = """
There is a lot of treasure here!
You take the treasure, get rich and live happily ever after!

YOU WIN!
"""
    print(look)

def east_west_rooms():
    look = """
There is a monster in this room. He eats you and
you regret ever being born as you fall down his throat.

GAME OVER
"""
    print(look)

entrance_hall() # this starts the game
```

It is up to you to develop this idea. The following are some suggestions the intent of this exercise it that you make the best game you can with your current skill set. Try some of the following as you develop your game:

- Draw a map and allow your character to move through many rooms. (At least 10 rooms/encounters.) 
- Make obstacles, enemies or puzzles for your character to overcome. 
- Allow the user to do many things in each room and write code to allow the user to put in bad input without breaking the game. 
- Figure out how to parse and interpret input so that GO WEST and Go WEst are both interpreted as go west. 
- Use a main-loop structure to simplify how the game works.

There are no real limits or minimum requirements for this. Like I said above what you get out of this is what you put into it.

### Make a Database Manager

Make a manager for a database. The database can consist of a text file or a `.json` file or a `.csv` file to store your data. (Note: There are both `json` and `csv` libraries built into Python for working with these types of files.)

For example suppose you are writing software to manage an inventory and assets for a used car dealership. Make a dictionary of all the pertinent data for each car (i.e. make, model, year, mileage, price)  for each car and keep a database of these. Make a fully featured program that lets the user keep track of all the pertinent data and allows you to add, delete and edit car data in the database. Ensure these are saved to a file of some type.

### Code a Calculator

Write a program that allows the user to quickly enter mathematical statements and evaluates them. This would be similar to how a graphing calculator works. This should go without saying but, this should be more extensive than running `python` in the command line and using the built-in functionality. The user may not know what an import statement is or that you need to use `x**y` to get `x` to the power of `y`. Make the program as smart as possible and able to do as many things as possible. If you wish to use add graphing functionality, I suggest looking up the third-party `matplotlib` library.

## APPENDIX: A quick introduction to some useful concepts

### `sys.argv`

Included here are some useful concepts and ideas for your project. Write out the following file and run it:

```python
# add_numbers.py

from sys import argv

print(f"The name of this file is: {argv[0]}") # get the filename

numbers = [float(i) for i in argv[1:]] # turn string arguments into numbers

print(f"The sum of the numbers given is {sum(numbers)}") # sum numbers together

```

**Here is what should happen**

```
$ python add_numbers.py 1 0.2 3 5 4 3
The name of this file is: add_numbers.py
The sum of the numbers given is 16.2
$
```

`argv` is short for argument variables and represents the space-separated arguments passed in with any call to Python. It takes the form of a list of strings with the first element being the name of the script that is being run. In our case the rest of the arguments are numbers to be summed together. If you want more detail on `argv` you can read about it [here](https://docs.python.org/3/library/sys.html#sys.argv). This is a common way to have your user interact with a program by passing it arguments as you run it. 

### Main-loops

Write out the following and run it as well:

```python
# mainloop.py

menu = '''
Enter one of the following.
    1 - print a word
    2 - do a thing
    3 - quit the program
'''

running = True

while running:
    print(menu)
    command = input("--> ")
    
    if command == "1":
        print("a word")
        
    elif command == "2":
        for i in range(10):
            print(i+1)
        print("I did a thing!")
        
    elif command == "3":
        running = False
    
    else:
        print("I do not understand that command.")

```

**Here is what should happen**

```
$ python mainloop.py

Enter one of the following.
    1 - print a word
    2 - do a thing
    3 - quit the program

--> 1
a word

Enter one of the following.
    1 - print a word
    2 - do a thing
    3 - quit the program

--> 2
1
2
3
4
5
6
7
8
9
10
I did a thing!

Enter one of the following.
    1 - print a word
    2 - do a thing
    3 - quit the program

--> 4
I do not understand that command.

Enter one of the following.
    1 - print a word
    2 - do a thing
    3 - quit the program

--> 3
$
```

As you can see, this program has a main-loop which runs the program until the user elects to end the program. In fact, it is a staple of programming to have a main-loop-like structure. The basic idea of a main-loop is a program that acts as follows:

1. Gets user input (e.g. a button press, keystroke etc.)
1. Processes the user input and apply some internal logic to it
1. Produces some output (e.g. a printed statement or a newly rendered image on screen)
1. Returns to step one

This basic structure should be a norm of programming for a user. Use this as your model for user input.

### Break and Continue statements

You can skip a loop iteration or stop a loop entirely with the `continue` or ` break` statements respectively. Write out the following code to practice it.

```python
# cont_break.py

# this loop counts to 100 by 10's
for i in range(1,101):
    if not i % 10 == 0:
        continue
    print(i, end=" ")

print("")

# this loop will prematurely end at 24
for j in range(100):
    print(j, end=" ")
    if j > 23:
        break

print("")
```

**Here is what should happen**

```
$ python cont_break.py
10 20 30 40 50 60 70 80 90 100 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 
$
```

Consider how the `break` and `continue` statements change the flow of the code.  Use these statements to skip iterations of loops or get out of loops entirely.

You may notice that these introductions have been brief. This is on purpose. My goal was to simply let you know that these features exist. It is up to you to research and utilize them. They are not required. 

<!-- Navigation -->

---

[Previous: 24-Reading Code](./24-Reading-Code.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 26-Objects and Classes](./26-Objects-and-Classes.md)

---
<!-- End Navigation -->
