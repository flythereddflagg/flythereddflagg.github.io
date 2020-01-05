<!-- Navigation -->

---

[Previous: 13-Logic-and-Boolean-Operators](./13-Logic-and-Boolean-Operators.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 15-Errors-Exceptions-and-Bugs](./15-Errors-Exceptions-and-Bugs.md)

---
<!-- End Navigation -->

# 14 - If, elif and else

We will use the concepts of True and False to drive our scripts ability to make decisions. The following exercise will help introduce program decisions and conditionals. 

**Note:** This will be the first time we see indented blocks of code. Whenever you see an indented line of code, follow the [Python standard](https://www.python.org/dev/peps/pep-0008/#code-lay-out) of always indenting 4 spaces (do *not* use tabs). Your text editor can and should be configured to insert 4 spaces instead of a tab character `\t` when the "Tab" key is pressed.

```python
# if_else.py

# let's start with some variables
# this will tell us to print an error
# message if necessary
error = False

# this is how much each farmer 
# needs in revenue to break even
break_even = 1000.00

# these are farming data
berry_farmer = "Barry Farmer"
wheat_farmer = "Ray Wheatley"

number_of_berries = 3294
bushels_of_wheat  = 523.45

berry_hired_hands = 34
wheat_hired_hands = 23

price_per_bushel = 2.50
price_per_100_berries = 15.23

# now let's get the farmer we
# want to know about
farmer_name = input("Enter the name of the farmer\n\t--> ")

if farmer_name == berry_farmer:
    produce = "Berries"
    amount  = number_of_berries / 100
    hands   = berry_hired_hands
    pricing = price_per_100_berries

elif farmer_name == wheat_farmer:
    produce = "Wheat"
    amount  = bushels_of_wheat
    hands   = wheat_hired_hands
    pricing = price_per_bushel

else:
    error = True
    
if not error:
    revenue = amount * pricing
    payment_per_hand = revenue / hands
    
    if revenue < break_even:
        message = "Farm is below break-even point. Sorry"
    else:
        message = "Farm is above break-even point. Congratulations!"
    
    print(f"""
        --- Farm Report for {farmer_name} ---
    Product for sale               : {produce:>11}
    Price per unit                 : ${pricing:10.2f}
    Total revenue                  : ${revenue:10.2f}
    Amount owed to each hired hand : ${payment_per_hand:10.2f}
        
        {message}
    """)

else:
    print(f"Farmer name \"{farmer_name}\" does not exist in record!")
```

**Here is what should happen**

Run this program 3 times as shown below. You should see similar results.

```
$ python if_else.py
Enter the name of the farmer
	--> Barry Farmer

        --- Farm Report for Barry Farmer ---
    Product for sale               :     Berries
    Price per unit                 : $     15.23
    Total revenue                  : $    501.68
    Amount owed to each hired hand : $     14.76
        
        Farm is below break-even point. Sorry
        
$ python if_else.py
Enter the name of the farmer
	--> Ray Wheatley

        --- Farm Report for Ray Wheatley ---
    Product for sale               :       Wheat
    Price per unit                 : $      2.50
    Total revenue                  : $   1308.62
    Amount owed to each hired hand : $     56.90
        
        Farm is above break-even point. Congratulations!
        
$ python if_else.py
Enter the name of the farmer
	--> Gary Hart
Farmer name "Gary Hart" does not exist in record!
$
```
**What is happening Here?**

We are using conditional logic to get data for a pair of farmers. We begin by prompting the user for the farmer's name. We then check the names of the farmers we have data for. If the name does not match any of the farmer's on record we print an error message. (This is the `else`  part on line 63.) The `error` variable we set earlier in the script will be set to `True` on line 42 in the case that we do not find  the name of any farmer in record.

Should the name given match a name in our records we prepare the output by setting appropriate variables and then formatting and printing them out in the absence of an error.

### Conditionals

The section about logical operators introduced us to the idea that everything can be evaluated with a value of `True` or `False`. In this section we put that logic to work for us. The conditional or "if" statement in python has the following syntax:

```python
if Expression1: # don't forget the colon
    do_thing_one() # indent 4 spaces

# if Expression1 evaluates to False check Expression 2
elif Expression2: 
    do_thing_two()

# and so on
elif Expression3:
    do_thing_three()
    
# if all previous expressions evaluate to False do the 'else' part
else:
    do_thing_four()
```

We will explain the syntax step by step. When Python comes to an `if` statement, the following is executed:

- Python evaluates whatever is in place for `Expression1` for a truth value.  
- If `Expression1` evaluates to `True`:
  -  Everything in the indented block of code under `if` will be executed. 
  - Once the block has ended (by un-indenting), the rest of the `elif` and `else` blocks of code are skipped. 
- If `Expression1` evaluates to `False`, `Expression2` is checked for its truth value 
- If`Expression2` evaluates to `True` :
  -  Everything in the indented block of code under `elif` will be executed. 
  - Once the block has ended (by un-indenting), the rest of the `elif` and `else` blocks of code are skipped.
- If `Expression2` evaluates to `False`, `Expression3` is checked for its truth value and so on...
- This pattern continues for all the `elif` expressions.
- Finally, if none of the 'if' or `elif` expressions evaluate to `True`, the code under the `else` is executed. 

Python's conditional syntax allows as many `elif` statements as the programmer wishes. However, the `elif` and `else` parts are not necessary. You may choose to have a conditional block without an `else` or without an `elif` part. We will discuss good practices for conditional statements in the section about errors.

### Indented Blocks

We have introduced an important syntax in Python. That is the indented block. This one feature that Python uses to make code more readable and to avoid cluttering the code page with unnecessary symbols or words. As you saw below each `if`, `elif` or `else` statement, the code is executed as normal. An indented block is just a way of Python separating a chunk of code and executing it in a different context, in this case, the context is that the code is executed if the logical expression evaluates to `True`. There are many other contexts that we will cover later but for now, memorize the following rules about indented blocks:

- *Indented blocks must start with a colon `:`.* A colon tells Python in effect "This is the beginning of a new indented block"
- *Indent 4 spaces.* Four spaces is an accepted convention although Python will technically allow whatever spacing you want as long as you are consistent. Any code you see written will follow the 4 space convention and that is the standard so it is best if you follow suit. If you mix spacings or are inconsistent with this Python will throw a syntax error.
- *End the block by un-indenting.* The only way Python knows that the indented block has ended is when an un-indented line of code is observed. 
- *Nested blocks are allowed.* If you want to have an indented block inside an indented block that is fine. the same rules apply in all cases.

You may not know understand yet why these are so important but as we go along it will be obvious why they exist.

## Hone Your Skills

1. Write a script that has several nested `if` and `elif` statements. Can you simplify the logic to not need as many nested blocks of code?

## Advanced Mastery

1. There is a problem in the above script `if_else.py` that can cause errors if we're not careful. Can you find the problem? How would you fix it?

   <!-- Answer: It is possible, with very little editing, to make it so the variables defined between lines 30 and 40 may be referenced without assignment should the `else` block be deleted. This can be fixed by making sure they are defined above before the user is even prompted. There are other ways to fix this as well. -->

<!-- Navigation -->

---

[Previous: 13-Logic-and-Boolean-Operators](./13-Logic-and-Boolean-Operators.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 15-Errors-Exceptions-and-Bugs](./15-Errors-Exceptions-and-Bugs.md)

---
<!-- End Navigation -->
