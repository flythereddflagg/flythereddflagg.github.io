<!-- Navigation -->

---

[Previous: 08 - Formatted Strings](./08-Formatted-Strings.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 10 - Better String Formatting](./10-Better-String-Formatting.md)

---
<!-- End Navigation -->
# 9 - Variables and Memory

Now we will introduce some concepts that make Python far more powerful. You have the ability to store things in computer memory and the following exercise will demonstrate how it works.

```python
# vars_and_mem.py

# equals sign ( = ) is the assignment operator
# it says: assign whatever is on the right 
# to the name on the left
first_text = "Here is some text!"
more_text = "This is another string of text."

print("{} {}".format(first_text, more_text))

# You can print numbers too! Here are some
random_integer_1 = 1
random_integer_2 = 23
random_number = 25.34

# notice the format of the code
# you can do this any time you have a
# comma separated list
# we also reuse the variable "first text" 
print("{} {} {} {}".format(
    first_text, 
    random_integer_1,
    random_integer_2,
    random_number
))

# now lets do the same thing but assign these 
# names to new values!
first_text = "Here are some more numbers"
random_integer_1 = 34
random_integer_2 = 203
random_number = 3.14159265

# notice how this print statement does the same
# thing as the last print statement
print(
    message, 
    random_integer_1, 
    random_integer_2,
    random_number
)
```

#### Here is what should happen

(If needed, see [Section 4](./04-Hello-World.md#making-and-running-your-first-python-file) to review how to run a script.)

```bash
$ python vars_and_mem.py
Here is some text! This is another string of text.
Here is some text! 1 23 25.34
Here are some more numbers 34 203 3.14159265
$
```

You can see that each name that is assigned a value can be used multiple times and refers to the same value that gets stored in memory. This name is called a <span title="Variable: a name assigned to a value. This value may be of any type in Python.">**variable**</span>. Here is how the computer works with variables.

### Computer Bare Essentials

I want to begin here by saying a few things about computers that hopefully will help you understand them better.

Computers, including those that run everything from your desktop to your phone to your car, basically only do 3 things:

1. Store numbers as 1s and 0s in different places
1. Move those 1s and 0s between the different places
1. Compare and combine those 1s and 0s mathematically (e.g. addition and subtraction)

Of course, computers can do these things at blinding speeds and can be endlessly combined to do all sorts of complex things but these three basics make up all of computing. The programs we have been writing so far do just those things but the details of how this is done is hidden from you but don't be fooled! Nothing more than those three things is happening at any time.

### Storing Information

One of the most important things you can learn is how memory works on a computer. Storing 1s and 0s is an essential ability for a computer to function.

For now, you need to understand that there are three basic parts to the computer that we interact with constantly. They are:

1. The **Central Processing Unit** (CPU): every instruction in the code gets executed here.
2. The **Random Access Memory** (RAM, or volatile memory): relevant program information is stored here as your program runs. As soon as your program stops running, all the information you have in RAM is erased.
3. The **persistent memory**: like the RAM, but the information you write here stays until you actively erase it (depending on your hardware). Your program gets stored here and is loaded into RAM to actually run. The persistent memory is generally contained on a drive of some sort (e.g a hard disk drive (HDD) or a solid-state drive (SSD)). We will be doing more with the persistent memory in a later section.

### Using RAM

The RAM is where your variables are stored. Without oversimplifying, you can think of the RAM as a large set of P.O. boxes in a vast post office. Each P.O. box has a number associated with it called an address. When you run code like

 `x = 23`

you are executing the following:

- Find an empty 'box' and write 23 in that box.
- Get the address of the 'box' and associate it with the name 'x'. (This erases any previous associations x may have had before.)

Anytime x is referenced after that command, the computer looks up the address associated with 'x' and goes directly to the 'box' with that address and replaces 'x' with whatever is in that 'box'.

### More Practice

The python interpreter will illustrate this better. Go to your terminal and enter `python` to start the interpreter.

```python
$ python
Python X.X.X ...
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Run the following commands:

```python
>>> x = 23
>>> type(x)
<class 'int'>
>>> id(x)
140737371887328
>>> x
23
>>> exit()
```

`type` , `id`  and `exit` are other built-in functions like `print` that provide some useful information about `x`. 

`type` spits out the type of variable between its parentheses (in this case, an integer or `int` as given in the interpreter).  `id` spits out the "address" of the variable in the RAM (***NOTE:** Depending on the Python implementation you are using, this may or may not be the literal address in memory but is always unique to the chunk of memory being used, hence its `id` or identification*). This address will likely be different for every time you start the Python interpreter. Entering the name of the variable simply prints its value and `exit()` simply exits the program.

### Naming Variables

As a programmer you will have to give names to your variables. There are certain rules for naming variables but, within those rules, you can make up any name you want for any variable. However, the guidelines below will help you make smart choices about how you name variables.

#### Naming Rules in Python

Python follows some rules on what a valid variable name can be. The rules are as follows:

- Names must start with a letter **or** an underscore (`_`) (e.g. `Spam`, `eggs`, `_cheese`)
- Names must **only** contain numbers, letters or underscores (i.e. spaces and punctuation are not allowed)
- Names are case sensitive (i.e. `Spam`, `spAm` and `spam` are three different names)
- Names cannot be one of the 35 reserved words in Python. These are listed in the table below. Should you feel the need to use one of these names, you can turn it into a valid variable name by adding a trailing underscore (e.g. `False_`).

|Reserved Words in Python|||||
| -------- | ------- | ----- | ----- | ------ |
| False | None    | True | and   | as     |
| assert   | async   | await | break | class  |
| continue | def     | del   | elif  | else   |
| except   | finally | for   | from  | global |
| if       | import  | in    | is    | lambda |
| nonlocal | not     | or    | pass  | raise  |
| return   | try     | while | with  | yield  |

For a complete explanation of naming see the section in [PEP 8](https://www.python.org/dev/peps/pep-0008/#naming-conventions).

#### Naming Conventions and Guidelines

Within the limits of these rules, you can call your variables any name you want and make them as long or as short as you want. However, there are some conventions you should stick to you make your code better. The following conventions will help make your code easier to write and fix when something goes wrong. (And trust me, something *always* goes wrong.):

- **Use lower case and underscores**

  There are two common ways to name a variable. For an example we will consider a variable with a name that can be read as "black knight". The first way is lower case with underscores for spaces: `black_knight`. The second is often called "camel case": `BlackKnight`. Obviously you can use all caps (`BLACKKNIGHT`), no spaces (`blackknight`), some abbreviation (`blk_knt`)  or any combination of these. However, the lower case with underscores and camel case are the most common for general use variables. 

  When writing Python especially as you are learning, stick to the lower case with underscores. For what we will be doing, this will help you avoid annoying errors and make your code more readable and clear to you and anyone else reading it.

  Understand however, that this is not a hard and fast rule and should be broken if there is a good reason to do so. We will break this rule later on as we explore more features.

- **Avoid names that conflict with existing names**

  When naming you will find that, outside the 35 key words above, when you define a name, it overrides any variable connected to that name before. Therefore the following code:

  ```python
  print = 2
  print("cheese")
  ```

  will break because you have changed the meaning of print from that of a function that writes things on the screen to an integer with a value of 2. Try this out for yourself.

  When naming variables always be careful to not use names that are already being used for another purpose. 

- **Write descriptive names**

  One time while working on someone else's code, I came across a line of code that looked something like this:

  ```python
  val = a*cav + b*wtmcls + c*hcpv + d
  ```

  I had some context for the code but could not figure out what this was saying. Initially, I could infer the following:

  - This was a mathematical statement equivalent to $val = a \cdot cav + b \cdot wtmcls + c\cdot hcpv + d$
  - a, b, c and d were constants related to all the other variables and if I could figure out the other 4 variables I could easily figure out a, b, c and d
  - `val` was short for 'value'. What value? I couldn't figure it out.

  The other 3 variables? I had no idea what they were.

  After weeks of digging I finally figured out what each of these variables were.

  - `val` was a predicted value of viscosity
  - `cav` stood for 'compound average value'
  - `wtmcls` was the number of 'water molecules' in the compound
  - `hcpv` was the 'heat capacity value' for that compound

  Now you don't need to understand all of this perfectly but consider how much easier to understand it would have been if the code had been written like this:

  ```python
  viscosity = a*compound_average + b*h2o_molecules + c*heat_capacity + d 
  ```

  I have done this in my own code. I have worked on code and been lazy with naming. I came back to my code later and found I had to rewrite everything because I couldn't understand what I did before.

  This will take practice but it behooves you to write your variable names (and the rest of your code for that matter) descriptively to avoid issues like the one above. 

- **Help your reader understand the code without comments**

  Ideally, you want to write code that can be read easily and makes readily apparent what the code does without needing comments explaining it. I do not want to diminish the importance of comments in code but writing easily understandable code is better than commenting. Up to now, what your code does should be obvious to anyone that can read Python without needing any comments. However, as we go through the next several exercises think of ways you could name your variables so your code is more clear.

Any good programmer knows that **the majority of the time spent coding is actually spent reading and not writing**. Python makes it easy for you to write readable code and the first step is write good variable names.

## Hone Your Skills

- Go to the [Python Built-in Function page](https://docs.python.org/3/library/functions.html) and experiment with as many functions in the Python interpreter as you can. What does each of these built in functions do?
- Using the addition operator (`+`), write a program that adds two numbers together and then print the result. (Use three descriptively named variables.)
- Experiment with different names of variables in `vars_and_mem.py`. How can you make your variables more clear to those reading your code?

## Advanced Mastery

- Search the internet to answer the following questions:
  - What is binary?
  - How are numbers represented as 1s and 0s?
  - How are characters represented as 1s and 0s?
  - How do computers do addition and subtraction using binary math?
  - What is 2's compliment? Why is it used?

<!-- Navigation -->

---

[Previous: 08 - Formatted Strings](./08-Formatted-Strings.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 10 - Better String Formatting](./10-Better-String-Formatting.md)

---
<!-- End Navigation -->
