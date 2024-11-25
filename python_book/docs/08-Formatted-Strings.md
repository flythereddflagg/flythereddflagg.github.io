
# 8 - Formatted Strings

As you use the `print` function there will be times when you need to "fill in the blank" and you can do this with format statements. Also we will introduce a few more features in addition to these.

```python
# format_strings.py

# We can print a comma-separated list
print("How much will this cost?", 23.00, "dollars")

# However, this is more readable and flexible 
# with a .format statement
print("How much will this cost? {} dollars.".format(23.0))

# The benefits of formatting become more
# apparent with more blanks to fill in.
print("Prices for cheese: "
    "${}/1 oz, ${}/5 oz, ${}/10 oz".format(1.23, 5.35, 9.84)
)

# Change the formatting order with indices in the braces
print("Would you like {2}, {0} or {1}?".format(
    "Brie", "Gouda", "Cheddar"
	)
)
# notice the formatting of code  in the previous two examples
# so each line of code stays short. Always use 4 spaces for 
# indents in Python.

# line up numbers and decimal places with format codes
print("""
Prices for cheese:
${:5.2f}/ 1 oz
${:5.2f}/ 5 oz
${:5.2f}/10 oz
""".format(1.23232, 5.3593, 9.84655))
```

### Here is what should happen

(If needed, see [Section 4](./04-Hello-World.md#making-and-running-your-first-python-file) to review how to run a script.)

```
$ python format_strings.py
How much will this cost? 23.0 dollars
How much will this cost? 23.0 dollars.
Prices for cheese: $1.23/1 oz, $5.35/5 oz, $9.84/10 oz
Would you like Cheddar, Brie or Gouda?

Prices for cheese:
$ 1.23/ 1 oz
$ 5.36/ 5 oz
$ 9.85/10 oz

$
```

## Formatting and the `.format()` method

We must understand a few things before understanding this code. 

- Print statements can be called on multiple strings or values separated by commas. As seen in line 4 that reads `print("How much will this cost?", 23.00, "dollars")` when we put a list of comma-separated strings in a print function, the print function prints them out with a space instead of a new line between them.

- We have introduced a powerful feature in the `.format` statement. The `.format`  statement refers to special kind of code called a 'method'. A method is like a function, such as the `print` function. But in this case, it is tied to whatever is on the left side of the dot (`.`). In this case, it only acts on the string to which it is tied. We first see this in line 7 which reads:

  `print("How much will this cost? {} dollars.".format(23.0))`

- To understand this process, here is what `.format()` does to the string from which it is called:

  - Scans the string looking for braces (`{}`) in the text
  - If there is text between the braces it interprets the text as format instructions.
  - It then looks at what is given between the parentheses (`.format("Text")`) and puts that text in place of the braces formatting it as per the format instructions.

## Format commands

Let's look at each example of a `.format`  statement one by one:

- `print("Prices for cheese: ${}/1 oz, ${}/5 oz, ${}/10 oz".format(1.23, 5.35, 9.84))`

   Each pair of braces is replaced by each value, in order, as they appear in the comma-separated list inside the parentheses. This is the default behavior if no format instructions in the braces are given. This is executed in the same way on line 24. If you notice in the case of line 24, there are numbers in the braces. Each of these is an index number that counts from 0.

- `print("Would you like {2}, {0} or {1}?".format("Brie", "Gouda", "Cheddar"))`

  As above you are putting indexes in the format braces. But what we see here is that you can put them in any order you want and even repeat them if you wish. (See "Hone your Skills" for an example of repetition.) 

  ***Note***: *In Python, counting always begins with 0.  (I.e. `0, 1, 2, ...` instead of `1, 2, 3, ...`) We will explain more about this when we discuss lists and iterables.) This means that when you write the following `"{1}".format("First", "Second")` you are commanding `.format("First", "Second")` to replace that text with `"Second"`. If the string were instead `"{0}"`the text would be replaced by `"First"`*

- The third example:
  
  ```python
  print("""
  Prices for cheese:
  ${:5.2f}/ 1 oz
  ${:5.2f}/ 5 oz
  ${:5.2f}/10 oz
  """.format(1.23232, 5.3593, 9.84655))
  ```
  
  Here we see that we are using format commands to organize data. The part that says `{:5.2f}` means to allow at least `5` spaces for the number to exist (fill any unused space with whitespace), round the number to `2` decimal places, and treat the number as a floating point number `f`.  We have omitted the index of the values for simplicity but they would be written on the left side of the colon (e.g. `{0:5.2f}`).

There are other formatting commands other than this but this is a good start to using formatting that will come up again and again. To review:

```python
# formatting cheat sheet
print("{<identifier><command>:<format>}".format(arguments))
```

## Hone Your Skills

```python
print("No. " * 3)
print("No.","No.","No.")
print("{0} {0} {0}".format("No."))
print("{} {} {}".format("No.","No.","No."))
print("{0} ".format("No.") * 3)
```

- Write the above code in a separate Python file and run it. As you will see, all 5 lines apparently do the same thing. Which way is the best way to do that and why? What are some potential advantages and drawbacks to each?
- Try rewriting lines of code from `format_strings.py` to make it so all the cheeses are aligned vertically. How can you do this with what we learned in this exercise?
- Look in the [Python documentation](https://docs.python.org/3.8/library/string.html#custom-string-formatting) for other format commands. Experiment with these and learn how to use them.

