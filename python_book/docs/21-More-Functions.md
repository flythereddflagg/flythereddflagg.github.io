<!-- Navigation -->

---

[Previous: 20-Functions](./20-Functions.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 22-Try-Except](./22-Try-Except.md)

---
<!-- End Navigation -->
# 21 - More Functions

There are three more concepts tied to functions that we must understand before moving on. They are each demonstrated in the following exercise:

```python
# more_functions.py

# params and returns
def quadratic_formula(a, b, c):
    """
    Calculates the roots of f(x) given a, b, c where
    f(x) = a * x**2 + b * x + c
    Returns the solution as a tuple.
    Returns None if the solutions are imaginary 
    """
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return None
    
    root1 = (-b - discriminant**0.5) / 2 / a
    root2 = (-b + discriminant**0.5) / 2 / a
    
    return root1, root2


imaginary_solution = quadratic_formula(1, 2, 3)
real_solution = quadratic_formula(1, -2, -3)
print("Imaginary Solution is:", imaginary_solution)
print("Real Solution is:",      real_solution)


# default params
def print_a_number(number=1):
    print(f"Your number is: {number}")  

print_a_number(3)
print_a_number()

# recursion
def factorial(number):
    """
    Returns the factorial of a number
    It first turns it into an integer
    before calculating its factorial
    """
    number = abs(int(number))
    if number <= 0:
        return 1
    return number * factorial(number - 1)

print("4!   =", factorial(4))
print("2.5! =", factorial(2.5))
```

**Here is what should happen**

```
$ more_functions.py
Imaginary Solution is: None
Real Solution is: (-1.0, 3.0)
Your number is: 3
Your number is: 1
4!   = 24
2.5! = 2
$
```

### Parameters and Arguments

Parameters are related to arguments. Many times these two terms are used interchangeably. To clarify, a parameter is the variable name that is used in the definition of a function. Whereas, an argument is what actually gets passed into the function call as seen here:

```python

def function_name(parameter):
    parameter += 3
    print(parameter)
    
# now we call the function
function_name(argument)
```

Following this logic, the argument replaces the parameter while the function code executes. You have worked with arguments since the first Python program you ran. The simple statement `print("Hello World!")` is just you calling the Python function named `print` and passing in the string `"Hello World!"` as an argument. Somewhere in the Python core code, there is a `print` function defined in a similar manner that executes all the details of printing text out to the command line.

### Default Values for Parameters

We saw in line 29 the following line of code: `def print_a_number(number=1):`. This function definition supplied a default value for the `number` parameter. Any function parameter may have a default value. The effect of this definition is that if no argument is passed that corresponds to that parameter the value for the parameter will be assumed and inserted into the function. However, if the corresponding argument is given then it will override the default value.

### Returns and the None type

You may have found that functions in Python have some practical similarities with mathematical functions. Just as a mathematical function f(x) will evaluate to a number when a value of x is supplied, a Python function that returns a value will evaluate to whatever value is returned. There are a few things to understand about the return statement:

- Any time a `return` statement is reached in Python, the expression after the word `return` is evaluated and the function call takes on the value of that evaluation. Therefore, if you have a return statement such as `return 2*3 + 4` the function will evaluate to `10`.  This is shown below:

  ```python
  def get_10():
  	return 2*3 + 4
  
  x = get_10()
  # x now has a value of 10
  ```

- A function always ends after a `return` statement regardless of where the statement occurs in the code. Therefore, return is often used to end a function code early if necessary. We saw this on line 13 - 14 in `more_functions.py` where it says:

  ```python
      if discriminant < 0:
          return None
  ```

  This will end the function if it is found that the solution will be imaginary.

- Functions that have no `return` statement return a special data type called `None` by default. The `None` data type is basically Python's way of saying this data is nothing or void. Therefore when we explicit returned `None`  we could have also just written `return` . Both cases would be saying, if the solution will be imaginary return nothing!

- It is possible to return multiple values (as seen in  `more_functions.py`  in the `quadratic_formula` function). As you saw above, they will simply be returned as a tuple.

Return statements are crucial for effective functions and it is a good idea to experiment with what you can return in a function. 

### Recursion

Recursion is the idea that a function or some process can reference itself. A great explanation of recursion as a concept can be found on [Wikipedia](https://en.wikipedia.org/wiki/Recursion). We saw this with the factorial example. In mathematics, a factorial is a number being multiplied by all the positive integers below it and is symbolized by an exclamtion mark. So the factorial of 4 = 4! = 4 * 3 * 2 * 1. In this case we could do a loop to accomplish this but to demonstrate this principle we can do it with recursion. We set up a base case to end the recursion:

```python
    if number <= 0:
        return 1
```

Then we have the function call itself with a small adjustment:

```python
    return number * factorial(number - 1)
```

And the function starts over again. This continues until the base case has been reached.

## Hone your Skills

- Try to write a recursive function that acts like a for-loop or a while-loop. Can you do it? What are the pros and cons of doing this?
- Write a function that returns multiple value and then try to unpack those into variables (see "Hone Your Skills" in the section on Iterables for more on how to do this.)

<!-- Navigation -->

---

[Previous: 20-Functions](./20-Functions.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 22-Try-Except](./22-Try-Except.md)

---
<!-- End Navigation -->
