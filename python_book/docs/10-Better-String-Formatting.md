<!-- Navigation -->

---

[Previous: 09-Variables-and-Memory](./09-Variables-and-Memory.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 11-Input-and-Output](./11-Input-and-Output.md)

---
<!-- End Navigation -->
# 10 - Better String Formatting

This is a short lesson in which we will learn a "trick" that will make all that formatting a lot more efficient using variables.

```python
# adv_format.py

# let's make some variables
pickle_brand = "Fantastic"
number_of_pickles = 7
average_pickle_weight = 2.34758475 # oz

# now lets print those variables in a string
pickle_info = """I have a jar of {} brand pickles. 
In the jar, there are {} pickles with an average
weight of {} ounces.\n""".format(
                                pickle_brand, 
                                number_of_pickles, 
                                average_pickle_weight) 

print(pickle_info)

# lets redefine pickle_info in a better way
pickle_info = f"""I have a jar of {pickle_brand} brand pickles. 
In the jar, there are {number_of_pickles} pickles with an average
weight of {average_pickle_weight:.3f} ounces.\n"""

print(pickle_info)

# lets take a bunch of numbers below
random_number_1 =    7583        # integer
random_number_2 =    -123        # negative integer
random_number_3 =      23.0      # float number
random_number_4 = 4838495.23221  # bigger float number
random_number_5 =     483.234    # medium float number
random_number_6 =    1293.0      # round float number

# now let's print them
print("Printing the numbers without any formatting.")
print(f"{random_number_1}")
print(f"{random_number_2}")
print(f"{random_number_3}")
print(f"{random_number_4}")
print(f"{random_number_5}")
print(f"{random_number_6}")
print("")

print("Notice how this can be hard to read.")
print("Let's try printing them and lining up the decimals.")
print(f"{random_number_1:7d}")    
print(f"{random_number_2:7d}")    
print(f"{random_number_3:11.3f}") 
print(f"{random_number_4:11.3f}")
print(f"{random_number_5:11.3f}")
print(f"{random_number_6:11.3f}")

```

**Here is what should happen**

```
$ python adv_format.py
I have a jar of Fantastic brand pickles. 
In the jar, there are 7 pickles with an average
weight of 2.34758475 ounces.

I have a jar of Fantastic brand pickles. 
In the jar, there are 7 pickles with an average
weight of 2.348 ounces.

Printing the numbers without any formatting.
7583
-123
23.0
4838495.23221
483.234
1293.0

Notice how this can be hard to read.
Let's try printing them while up the decimals.
   7583
   -123
     23.000
4838495.232
    483.234
   1293.000
$
```

**What is happening here?**

lets go through each new concept one-by-one:

- *Lines 8-14:*
  You can have a indented new line in python anytime you have a comma or a
  open parenthesis also you can assign a multi-line string to a variable in this way.

  You'll notice this was many lines of code to get this to do what we want. And Python has a better way.

- *Lines 19-21 and 33- 50:* Notice the `f` in front of the string. This is known as a "literal string interpolation" and is explained below.

- *Lines 43-50 and line 21:* These are format instructions. `d` is the symbol that corresponds 
  to formatting an integer. `f` is the symbol for floats. The number before the decimal is the amount of space padding. The number after the decimal is the number of decimal places to show in the number. There are more instructions that can be passed. See "Hone your skills" for more on this subject. The important thing here is that for numbers, changing the padding and decimal places can align the numbers' decimals in an easy-to-read fashion.


### Literal String Interpolation

The `f` that we put in front of a string is referred to technically as a "literal string interpolation". Colloquially, it is called an "f-string". It tells Python to automatically call `format()` on the string using the variable names in the braces. The colon and the text following it tells Python to accept format codes that we explored before. This feature was added relatively recently and is now a standard way of string formatting.

## Hone Your Skills

1. Look up what a Python PEP is and specifically look up PEP 498. Why do PEPs exist?
1. `f` is not the only thing that we can put at the beginning of a string to make it do something different. What happens when you put the following letters in front of a string? (Search for these on the internet if you can't figure it out.)
    - `r`
    - `b`
    - `u`
1. Now you can make a form with variables that will print out information. Make a form that gives the name, age and occupation of whatever you set those variables
1. The format instructions are detailed [here](https://docs.python.org/3.7/library/string.html#format-string-syntax) in the Python documentation. Learn what each of these things do and experiment with them.
1. Experiment with the format instructions. Can you align all the numbers in different ways?

<!-- Navigation -->

---

[Previous: 09-Variables-and-Memory](./09-Variables-and-Memory.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 11-Input-and-Output](./11-Input-and-Output.md)

---
<!-- End Navigation -->
