# 20 - Functions

We are nearing the end of the basics of Python programming. Most of the concepts we have covered so far are features in all programming languages. To recap, all complete programing languages have the following basic features or some equivalent:

- The ability to format text and print it to the command line
- Assignment of variables and storage in volatile memory
- Receiving user input
- Reading and writing files in persistent memory
- Performing mathematical operations on numbers
- Conditionals (i.e. if, else statements) and logical evaluation
- Both for-loops and while-loops
- The ability to define and manipulate list-like structures (i.e. array or linked structures)
- Functions

It is this last feature that we have not yet sufficiently explored. This next exercise will introduce what is perhaps the most powerful of the features we have explored so far.

```python
# function_intro.py

# define a global variable
number_of_sandwiches = 0

# 'def' defines a function
def count_sandwiches():
    print(f"\nThere are {number_of_sandwiches} sandwiches.") 


def make_a_sandwich():
    global number_of_sandwiches
    number_of_sandwiches += 1
    print("\nA sandwich has been made.")
    print(f"There are now {number_of_sandwiches} sandwiches.")


def eat_a_sandwich():
    global number_of_sandwiches
    number_of_sandwiches -= 1
    print("\nYou ate a sandwich.")
    print(f"There are now {number_of_sandwiches} sandwiches.")


def main():
    """
    The text between these quotes is the "documentation string".
    Documentation strings are used to explain the function 
    they are in. They go before the code of the function but 
    after the first line of the function (the line with "def"
    in it). I am explaining this here but usually you will 
    just see an explanation like:
    
    This is the main function of the program.
    It will be the place from which all other functions 
    in this program will be called.
    """
    prompt = """
Would you like to "make" a sandwich, "eat" a sandwich,
"count" your sandwiches or "quit"?
--> """
    running = True

    while running:
        choice = input(prompt)

        if "count" in choice:
            count_sandwiches()
            
        elif "make" in choice:
            make_a_sandwich()

        elif "eat" in choice:
            if number_of_sandwiches > 0:
                eat_a_sandwich()
            else:
                print("There are no sandwiches to eat!")

        elif "quit" in choice:
            running = False

        else:
            print("That isn't an option.")

main()

```
### Here is what should happen
```
$ python3 function_intro.py

Would you like to "make" a sandwich, "eat" a sandwich,
"count" your sandwiches or "quit"?
--> make

A sandwich has been made.
There are now 1 sandwiches.

Would you like to "make" a sandwich, "eat" a sandwich,
"count" your sandwiches or "quit"?
--> count

There are 1 sandwiches.

Would you like to "make" a sandwich, "eat" a sandwich,
"count" your sandwiches or "quit"?
--> make

A sandwich has been made.
There are now 2 sandwiches.

Would you like to "make" a sandwich, "eat" a sandwich,
"count" your sandwiches or "quit"?
--> eat

You ate a sandwich.
There are now 1 sandwiches.

Would you like to "make" a sandwich, "eat" a sandwich,
"count" your sandwiches or "quit"?
--> eat

You ate a sandwich.
There are now 0 sandwiches.

Would you like to "make" a sandwich, "eat" a sandwich,
"count" your sandwiches or "quit"?
--> eat
There are no sandwiches to eat!

Would you like to "make" a sandwich, "eat" a sandwich,
"count" your sandwiches or "quit"?
--> quit
$ 
```

## Functions

Upon finishing this lesson, you should have made your first functions!

There will always be times when you code that you will wish to reuse a chunk of code multiple times. A function allows you to reuse that code as many times as you want with a line of code to call the function. We will explore the basic aspects in this and the next lessons.

Functions follow the following syntax:

```python
def function_name(argument1, argument2 ...):
    <statements ...>
    <statements ...>
    <statements ...>

# code continues unindented

# call the function using
function_name(argument1, argument2)

# or if there are no arguments
function_name()
```

We will talk more about arguments in the next lesson so don't worry too much about them here. As seen from the syntax above, when called the function executes the code in the indented block (this is what is meant by `<statements ...>`). The first example of this was in the `count_sandwiches()` function. As you saw while executing the script, it simply gets the value of `number_of_sandwiches` and prints the corresponding text. **Remember** that when you write a variable name followed by parentheses (e.g. `function_name()`), you are telling Python, "Run this function!".

## Scope

In the second and third functions,  `make_a_sandwich()` and `eat_a_sandwich()`, you see the statement `global number_of_sandwiches`. The word `global` is a keyword in Python that we have not talked about yet and relates to how Python manages variables and memory.

Up to this, point we have used only global variables. That is, we have had variables that were visible to every part of the program. Consider the following code:

```python
egg = "Brown"

def change_color():
    egg = "White"

change_color()
print(f"The egg is {egg}")
```

Based on this code, which will print?

- `The egg is White`
- `The egg is Brown`

If you try this out yourself, you will find that `The egg is Brown` is printed even though we changed the color of `egg` with `change_color()`. This is because of the scope of the `egg` variable. From Python's point of view, the `egg` defined on line 1 and the `egg` defined on line 4 inside the `change_color()` function are two different variables. The `egg` defined in the function only works inside the function and ceases to exist once the function ends.

If we want the `egg`  on line 1 and the `egg` inside the function to be the same variable we need to tell Python to do that. We do this with the `global` key word as follows:

```python
egg = "Brown"

def change_color():
    global egg
    egg = "White"

change_color()
print(f"The egg is {egg}")
```

The line `global egg` tells Python to treat the `egg` variable in the function as the same `egg` variable defined in the global scope. There are many possible scopes that could exist in a Python program but for now the function scope and the global scope are the most important.

A good thing to bear in mind while writing functions is that every variable that is defined in the context of the function will disappear as soon as the function ends. This means that if you want a variable to hang around after the function ends that variable needs to be defined in a scope outside the function.

In the case of `function_intro.py`, you may have noticed that we did not have to use `global` in the first function. Why? This is a nuance of how Python deals with scope. If you are not defining a variable in a function but only referencing it (as was the case with `count_sandwiches()`), Python first searches the function for the referenced name and then then expands the scope of the variable until the variable name is found. For the other two functions we were using assignment operators. Any time an assignment operator is used, Python defines the scope of the variable this way. This means that if you comment out the lines in `function_intro.py` you will get an error because the function variables have not yet been defined in that scope. Try this out for yourself!

## Main-loops

The code under the `main` function is what is known as a "main-loop" or a "main-program loop". It uses the model of REPL (Read, Evaluate, Print, then Loop) to execute as many commands as the user needs (the Python interactive prompt uses this same model). Notice, the use of the while-loop and the structure of the function. Understand this part of the program as it will become more important in the following sections.

## Hone Your Skills

- Make a function that calculates the [factorial of a number](https://en.wikipedia.org/wiki/Factorial) (use a for-loop in your function) using a global variable from the user as your input.
- Experiment with the main-loop or REPL function. How could you use this model to do something useful?

