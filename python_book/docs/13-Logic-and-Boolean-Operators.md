<!-- Navigation -->

---

[Previous: 12-Math-and-Data](./12-Math-and-Data.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 14-If-elif-and-else](./14-If-elif-and-else.md)

---
<!-- End Navigation -->

# 13 - Logic and Boolean Operators

For this section's exercises there will be a short example that you will work in the Python interpreter instead of a Python script. Enter each command from each exercise complete them.

### True and False

One of the most important concepts in programming is that of Boolean logic. On a fundamental level, your computer only knows 2 things: 1 and 0, Yes and No, On and Off, True and False. Everything else in a computer must be constructed from these two things. Within this framework the computer can do many things such as make decisions. However to make a decision, the computer must be able to evaluate a "truth value" of everything. Therefore, everything can be evaluated as True or False using the built-in `bool` function.

This gives rise to a new data type, the **Boolean data type**. The Boolean data type can only have two values, namely `True` or `False`. This makes it among the simplest and most useful of data types.

#### Try this out in the interpreter

Go to your python interpreter and try running the following commands:

```python
$ python3
Python 3.x.x ...
Type "help", "copyright", "credits" or "license" for more information.
>>> bool(True)
True
>>> bool(False)
False
>>> bool(0)
False
>>> bool(34)
True
>>> bool(-1)
True
>>> bool(0.0)
False
>>> bool(0.001)
True
>>> bool("")
False
>>> bool("s")
True
>>> exit()
$
```

What you should get out of this is that, for the three data types we have covered so far, anything that is a non-empty or non-zero value will evaluate to True and empty or zero values will evaluate to False. `True` and `False` are both key words in Python to express these boolean concepts. And every data type in Python, by default, will evaluate to one or the other. In the next lesson we will explore how we can use this idea to make decisions. Another way to return the boolean value of something is by using the logical comparison operators.

### Comparison Operators

We will introduce another set of binary operators called comparison operators. For all these operators we will use the example of `x <OPERATOR> y` to demonstrate the meaning of each operator

| Code Symbol | Meaning                  |
| ----------- | ------------------------ |
| `==`        | Equal to                 |
| `!=`        | Not equal to             |
| `>`         | Greater than             |
| `<`         | Less than                |
| `>=`        | Greater than or equal to |
| `<=`        | Less than or equal to    |



#### Try this out in the interpreter

A few things to do while doing this exercise:

- Note that some of these return errors. Which ones do this and why? 

- Read each line as you write it as such:
  - "1 is equal to 2: False"
  - "Empty quotes is equal to 0: False"
  - etc.

  This will help you learn to think about these logical statements.

```python
$ python3
Python 3.x.x ...
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 == 2
False
>>> "" == 0
False
>>> 0 == 0
True
>>> 1.0 == 1
True
>>> 3 != 2
True
>>> "" != 0
True
>>> 0 != 0
False
>>> 3 < 2
False
>>> 3 >=2
True
>>> 3 > 3
False
>>> "" == ""
True
>>> "" > 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'str' and 'int'
>>> "" > "23"
False
>>> "" < "23"
True
>>> "23" < "23"
False
>>> "23" == "23"
True
>>> "23" == "24"
False
>>> "23" > "24"
False
>>> exit()
$
```

You can see from the results of the above exercise that some types are incompatible with others. Also note that in most cases combining numbers and strings returns a not equal condition. 

### Logical operators

True and False may be combined using logical operators. This allows many statements to be chained and combined in logical ways. They use the truth value and based on their logic and then return one of the values. In a more useful sense, if you only combine two Boolean values or expressions that evaluate to Boolean values you can pull some logic out of the expression.

The following is pulled directly from the [official Python documentation](https://docs.python.org/3.7/library/stdtypes.html) to help you understand the result of each operator:

---

#### Boolean Operations — [`and`](https://docs.python.org/3.7/reference/expressions.html#and), [`or`](https://docs.python.org/3.7/reference/expressions.html#or), [`not`](https://docs.python.org/3.7/reference/expressions.html#not)

These are the Boolean operations, ordered by ascending priority:

| Operation | Result                                     | Notes |
| --------- | ------------------------------------------ | ----- |
| `x or y`  | if *x* is false, then *y*, else *x*        | (1)   |
| `x and y` | if *x* is false, then *x*, else *y*        | (2)   |
| `not x`   | if *x* is false, then `True`, else `False` | (3)   |

Notes:

1. This is a short-circuit operator, so it only evaluates the second argument if the first one is false.
1. This is a short-circuit operator, so it only evaluates the second argument if the first one is true.
1. `not` has a lower priority than non-Boolean operators, so `not a == b` is interpreted as `not (a == b)`, and `a == not b` is a syntax error.

---

#### Try this out in the interpreter

```python
$ python
Python 3.x.x ...
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 and 2
2
>>> 2 and 1
1
>>> bool(2) and bool(1)
True
>>> True and False
False
>>> True and True
True
>>> True or False
True
>>> True and False or True
True
>>> True and (False or True)
True
>>> True or False or True
True
>>> True and False and True
False
>>> "" and 4
''
>>> 3.14 or 0.0
3.14
>>> bool(3 and 4 and 0)
False
>>> "cheese" or "crackers"
'cheese'
>>> "cheese" and "crackers"
'crackers'
>>> True and not False
True
>>> not True or False
False
>>> not 3
False
>>> not 0
True
>>> exit()
$
```

For all of these operators, memorize their behavior and practice with them

<!--Potentially take out the results so they have to do it themselves and interpret what the results mean themselves?-->

## Hone your skills

- Make your own table or a set of flash cards for each of these operators and practice predicting the result of many different comparisons, logical statements and uses of the `bool` function.

## Advanced Mastery

- Look at the [official Python documentation](https://docs.python.org/3.7/library/stdtypes.html) on built-in types, focusing on the Boolean data type. Or, make your own internet search. Answer the following questions:
  - How do the equality operator `==` and the `is` operator differ?
  - Does order matter in logical operator statements? How can you use this to your advantage?
  - For objects that are not numbers or strings, how is the Truth value evaluated? How could you change this evaluation?

<!-- Navigation -->

---

[Previous: 12-Math-and-Data](./12-Math-and-Data.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 14-If-elif-and-else](./14-If-elif-and-else.md)

---
<!-- End Navigation -->
