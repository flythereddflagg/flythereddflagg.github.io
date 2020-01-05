<!-- Navigation -->

---

[Previous: 11-Input-and-Output](./11-Input-and-Output.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 13-Logic-and-Boolean-Operators](./13-Logic-and-Boolean-Operators.md)

---
<!-- End Navigation -->

# 12 - Math, Operators and Data Types

Now before going further we need to talk about math. This is not a book about math. I will cover some concepts related to scientific/engineering math in an optional lesson later but I expect that you already know about the following concepts:

- Addition and Subtraction
- Multiplication and Division
- Remainders of Division
- Exponents
- Absolute Values

If you are unfamiliar with some of these concepts, I suggest you familiarize yourself with them before proceeding so you have at least a basic understanding of what they are. However if you intend to proceed anyway, just skip the stuff with which you are not familiar as it is probable you will never have to use it. 

The following exercise will introduce you to the basics of math:

```python
# math_learning.py

# we will use the variables x, y and z
x = 24.3
y = 9.0
z = x

print("x =", x)
print("y =", y)

# basic math operators
print("x +  y =", x + y)  # addition
print("x -  y =", x - y)  # subtraction
print("x *  y =", x * y)  # multiplication
print("x ** y =", x ** y) # exponentiation
print("x /  y =", x / y)  # division
print("x // y =", x // y) # integer division or floor division
print("x %  y =", x % y)  # modulo or remainder

print("z was:", z)

# assignment operators
z  += x # same as z = z +  x
z  -= x # same as z = z -  x
z  *= x # same as z = z *  x
z **= x # same as z = z ** x
z  /= x # same as z = z /  x
z //= x # same as z = z // x
z  %= x # same as z = z %  x

print("z is now:", z)
```

**Here is what should happen**

```
$ python math_learning.py
x = 24.3
y = 9.0
x +  y = 33.3
x -  y = 15.3
x *  y = 218.70000000000002
x ** y = 2954312706550.8345
x /  y = 2.7
x // y = 2.0
x %  y = 6.300000000000001
z was: 24.3
z is now: 4.70613749314111
$ 
```

**What is happening here?**

This is a demonstration of mathematical binary operators and assignment operators. Both types of operators will be explained below. Lines 28 - 34 demonstrate the assignment operators and were the equivalent of:

 `z = (((((z + x - x) * x) ** x) / x) // x) % x`,

`z = (z * x)**x / x // x % x` 

or $$z = modulo(\frac{(zx)^x}{x} // x, x)$$

We will explain all of this in this lesson.

### Data Types

In the lesson on [Variables and Memory](./09-Variables-and-Memory.md), we talked about a computer can only move and store numbers in "boxes". However, we can represent anything we want as a set of "boxes" with numbers using some clever tricks that we will not get into here. 

Suffice it to say that the computer has a way of 'marking' a box or series of boxes as number, letter, chunk of code or, indeed, anything we want. This mark allows the computer to deal with those boxes in a logical manner. For example, you should not try to mathematically divide a string. Therefore, the computer marks the series of numbers as a string so it knows how to properly deal with it and the code:

```python
name = "John" / 3
```

does not make any sense will make Python throw an error.

The different ways a computer can "mark" a set of numbers for interpretation are called "data types" or simply "types". Later on, we will deepen our understanding of types but for now we will talk about 3 basic types.

- **Integers**

  An integer is any whole number, positive or negative (e.g. -3, -2, -1, 0, 1, 2, 3). This changes how it is combined with other numbers (as we will see later). As it happens, a positive integer is the only data type that can be directly expressed as 1s and 0s in computer memory. Every other data type must have an interpretation attached to it (i.e. a data type).

  The most obvious feature of an integer is that it cannot have a decimal or any fraction value. To have those features you need a float or a floating point number.

- **Float**

  A floating point number or "float" for short is a number that can have a non-whole or fractional value. Values like `1.0`, `-0.06020`, or `16575.23` are all floats. A float generally takes up more memory than an integer and can give you more precision in mathematical calculations. The precision a computer can have is limited by how much space a float can take up.

  An important note about floats and integers are that if you combine them mathematically, you will always get a float back. Therefore, should you need to "upgrade" and integer to a float you can do so by multiplying an integer by `1.0`.

```python
number = 2 # 'number' is an integer
number = number * 1.0
# 'number' now has the same value but is a float
```

- **String**

  A string, is fundamentally a series of numbers in boxes in computer memory that are interpreted as a sequence of letters. Those numbers can be used to express thousands of characters. Strings can interact with floats and integers and be combined using operators but do not act the same way floats and integers do as we will see below.

There are many more types than these and we will introduce them later on. These are, however, the most common and fundamental types. If you wish to ever know the type of any variable you can use `print(type(var))`.

### Math Operators

Each set of symbols between x and y is called a binary operator. Below is a brief description of each binary operator and what it does to a integer, float and string.

| Operator                  | Math Example                                      | Integer and float                  | String                                                       |
| ------------------------- | ------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------ |
| + (plus)                  | `x + y`\(=x + y\)                                 | Addition                           | Concatenate two strings                                      |
| - (dash)                  | `x -  y`  \(=x - y\)                              | Subtraction                        | No meaning                                                   |
| * (asterisk)              | `x *  y`  \(= xy = x\cdot y\)                     | Multiplication                     | Multiply a string by a positive integer to concatenate string `y` with itself  `x` times |
| ** (double asterisk)      | `x ** y ` \(=x^y\)                                | The exponent                       | No meaning                                                   |
| / (forward slash)         | `x /  y` \(=x/y=\frac{x}{y}\)                     | Float (i.e. normal) division       | No meaning                                                   |
| // (double forward slash) | `x // y` \(=\frac{x}{y}\) rounded down to integer | Integer division or floor division | No meaning                                                   |
| % (percent character)     | `x %  y = y - x * (x // y)`                       | Modulo or Remainder                | "Old style" string formatting                                |

Among the above operators, the less commonly known operators are the last 2 and therefore we will give more details about them below:

- **Integer Division** 

  This is like normal division but the resulting number is rounded down to the next lowest integer. The result is always an integer value but not necessarily an integer number (e.g. `2.0` may be returned instead of `2`)

- **Modulo**

  This is the same thing as a remainder. For example: how many times does 3 goes into 5 evenly? Answer: 1 but if we subtract the product of 3 and 1 from 5 we get what is left over. 

### Assignment Operators

The assignment operator `=` will always evaluate whatever is on the right side of it before storing it in memory. Therefore, an operation like `z = z + x` tells the computer to do the following:

- Take the current value of `z` and add it to `x`
- Once you have that result, store that result in the same place 

Python has a shorthand for all of these operators to make certain things easier later on. We will explore this in a later lesson. These shorthand versions are also called assignment operators.

Below is a summary of the assignment operators and their corresponding string operations.

| Operator                   | Same as      | String Operation                              |
| -------------------------- | ------------ | --------------------------------------------- |
| `+=` Plus-equals           | `z = z + x`  | Append `x` to `z`                             |
| `-=` Minus-equals          | `z = z - x`  | No meaning                                    |
| `*=` Times-equals          | `z = z * x`  | The new `z` is the old `z` repeated `x` times |
| `**=` Exponent-equals      | `z = z ** x` | No meaning                                    |
| `/=` Divide-equals         | `z = z / x`  | No meaning                                    |
| `//= `Double-divide-equals | `z = z // x` | No meaning                                    |
| `%=` Modulo-equals         | `z = z % x`  | An expansion of the "old-style" formatting    |

### Order of Operations

Python uses normal math conventions when evaluating math expressions the following order of operations is observed proceeding left to right when conflicts appear:

1. Parentheses
1. Exponents
1. Multiplication, Division, Integer Division and Modulo
1. Addition and Subtraction

All Python expressions follow the convention of being evaluated left to right and any order can be broken by using parentheses.

### Built-in Math Functions

Lastly we will talk about some built-in functions (like `print()`) can help us evaluate and convert between math and string operations:

- `int`
  This function can be used to turn a float or a string into an integer if there is any way to interpret it as such. Therefore expressions like `int("123")`, `int(123.223)` and `int(123)` will all work and return `123` as an integer but `int("a 123")` will throw an error.

- `float`

  This will likewise turn any type into a float if possible. (e.g.  `float("123.00")`, `float("123")`, `float(123.00)` and `float(123)` will all work and return `123` as an integer but `float("a 123")` will throw an error.)

- `str`

  This function will turn any type into a string if possible. (e.g. `str(123)` becomes `"123"` and `str(123.00)` becomes `"123.0"` )

- `abs`

  This gives the absolute value of the number

- `pow`

  Pow or power is the exponent function and `pow(x, y)` is equivalent to `x ** y`

## Hone Your Skills

1. Write your own script that uses the built-in functions. Can you break them? What are their limitations?
2. Using the `input` function, write a script that asks the user for the parameters `a`, `b` and `c` corresponding to the quadratic equation ($ax^2+bx+c = 0$) and calculates the roots of the equation using the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_equation) with the user providing a, b and c. (Hint: A square root is the same as taking a number to the $\frac{1}{2}$ power. e.g. $\sqrt{a+b} = (a+b)^\frac{1}{2}$) 

## Advanced Mastery

1. Notice in the results of `math_learning.py` that you got some answers that were lots of 0s followed by a single digit. Research "round off error" to understand why this happens.

<!-- Navigation -->

---

[Previous: 11-Input-and-Output](./11-Input-and-Output.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 13-Logic-and-Boolean-Operators](./13-Logic-and-Boolean-Operators.md)

---
<!-- End Navigation -->
