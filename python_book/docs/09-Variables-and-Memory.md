<!-- Navigation -->

---

[Previous: 08-Formatted Strings](./08-Formatted-Strings.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 10-Better String Formatting](./10-Better-String-Formatting.md)

---
<!-- End Navigation -->
# 9 - Variables and Memory

Now we will introduce some concepts that make Python far more powerful. You have the ability to store things in computer memory and the following exercise will demonstrate how to use it.

```python
# vars_and_mem.py

# equals sign ( = ) is the assignment operator
# it says: assign whatever is on the right 
# to the name on the left
first_text = "Here is some text!"
more_text = "This is another string of text."

print("{} {}".format(first_text, more_text))

message = "You can print numbers too! Here are some"
number_1 = 1
number_2 = 23
number_34 = 25.34
print("{} {} {} {}".format(message, number_1, number_2, number_34))

# now lets do the same thing but assign these names to new values!
message = "Here are some more numbers"
number_1 = 34.1
number_2 = 203
number_34 = 3.14159265
print("{} {} {} {}".format(message, number_1, number_2, number_34))
```

---

**Here is what should happen**

```
$ python vars_and_mem.py
Here is some text! This is another string of text.
You can print numbers too! Here are some 1 23 25.34
Here are some more numbers 34.1 203 3.14159265
$
```

You can see that each name that is assigned a value can be used multiple times and refers to the same value that gets stored in memory. This name is called a **variable**. Here is how the computer works with variables: 

### Computer Bare Essentials

I want to begin here by saying a few things about computers that hopefully will help you understand them better.

Computers, including those that that run everything from your desktop to your phone to your car, basically only do 3 things:

1. Store numbers as 1s and 0s in different places
1. Move those 1s and 0s between the different storage places
1. Combine those 1s and 0s mathematically (i.e. addition and subtraction)

Of course, computers can do these things at blinding speeds and can be endlessly combined to do all sorts of complex things but these three basics make up all of computing. The programs we have been writing so far do just those things but the details of how this is done is hidden from you but don't be fooled! Nothing more than those three things is happening at any time.

### Storing Information

One of the most important things you can learn is how memory works on a computer. Storing 1s and 0s is the first thing that a computer must be able to do in order to function.

For now the most important things you need to understand are these:

- There are three basic parts to the computer that we will interact with constantly. They are:
  - The CPU
  - The RAM or volatile memory
  - The hard drive or persistent memory
- CPU stands for central processing unit. Every instruction you write gets executed there.
- RAM stands for Random Access Memory. You will put information relevant to your programs there as your program runs. As soon as your program stops running, all the information you have in RAM gets erased.
- The hard drive is like the RAM except the information you write there stays there until you actively erase it. We will be doing more with the hard drive later

The RAM is where your variables are stored. Without oversimplifying, you can think of the RAM as a large set of P.O. Boxes in a vast post office. Each P.O. box has a number associated with it called an address. When you run code like

 `x = 23` 

you are executing the following:

- Find an appropriate, empty 'box' and write 23 in that box.
- Get the address of the 'box' and associate it with the name 'x'. (This erases any previous associations x may have had before.)

Anytime x is referenced after that command, the computer looks up the address associated with 'x' and goes directly to the 'box' with that address and replaces 'x' with whatever is in that 'box'.

### More Practice

The python interpreter will illustrate this better. Go to your terminal and enter `python` to start the interpreter.

```python
$ python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
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

`type` spits out the type of variable between its parentheses.  `id` spits out the address of the variable in the RAM. This will be different for every time you start the Python interpreter. Entering the name of the variable simply prints its value and `exit()` simply exits the program.

### Naming Variables

As a programmer you will have to give names to your variables. Within certain rules you can make up any name you want but the following guides will help you make smart choices about how you name variables.

#### Naming Rules in Python

Python follows some rules on what a valid variable name can be. The rules are as follows:

- Names must start with a letter **or** and underscore `_` (e.g. Spam, eggs, _cheese)
- Names must **only** contain numbers, letters or underscores (i.e. spaces and punctuation are not allowed)
- Names are case sensitive (i.e. Spam, spAm and spam are three different names)
- Names cannot be one of the 35 reserved words in Python. These are listed in the table below. (As a note should you feel the need to use one of these names, you can turn it into a valid variable name by adding leading or trailing underscores e.g. `_False` or `False__ `  or a trailing number e.g. `False1`)

|Reserved Words|||||
| -------- | ------- | ----- | ----- | ------ |
| False | None    | True | and   | as     |
| assert   | async   | await | break | class  |
| continue | def     | del   | elif  | else   |
| except   | finally | for   | from  | global |
| if       | import  | in    | is    | lambda |
| nonlocal | not     | or    | pass  | raise  |
| return   | try     | while | with  | yield  |

#### Naming Conventions and Guidelines

Within the limits of these rules, you can call your variables any name you want and make them as long or as short as you want. However, there are some conventions you should stick to you make your coding better. The following conventions will help make your code easier to write and fix when something goes wrong. (And trust me, something *always* goes wrong.):

- **Use lower case and underscores**

  There are two common ways to name a variable. For an example we will consider a variable that will bear a name that can be read as "black knight". The first way is lower case with underscores for spaces: `black_knight`. The second is often called "camel case": `BlackKnight`. Obviously you can use all caps (`BLACKKNIGHT`), no spaces (`blackknight`), some form abbreviation (`blk_knt`)  or any combination of these. However, the lower case with underscores and camel case are the most common for general use variables. 

  When writing Python especially as you are learning, stick to the lower case with underscores. For what we will be doing this will help your code be more readable and clear to you and anyone else reading it. 

  Understand however, that this is not a hard and fast rule and should be broken if there is a good reason to do so. We will break this rule later on as we explore more features.

- **Avoid names that conflict with existing names**

  When naming you will find that, outside the 35 key words above, when you define a name, it overrides any variable connected to that name before. Therefore the following code:

  ```python
  print = 2
  print("cheese")
  ```

  will not work because you have changed the meaning of print from that of a function that writes things on the screen to an integer with a value of 2. Try this out for yourself.

  When naming variables always be careful to not use names that are already being used for another purpose. 

- **Write descriptive names**

  One time while working on someone else's code, I came across a line of code that looked something like this (I have changed it for privacy reasons but the lesson still stands):

  ```python
  val = a*cav + b*wtmcls + c*hcpv + d
  ```

  As a chemical engineer, I had some context but could not figure out what this was saying. Initially I could infer the following:

  - This was a mathematical statement equivalent to $val = a \cdot cav + b \cdot wtmcls + c\cdot hcpv + d$
  - a, b, c and d were constants related to all the other variables and if I could figure out the other 4 variables I could easily figure out a, b, c and d
  - `val` was short for 'value'. What value? I couldn't figure it out.

  The other 3 variables? I had no idea what they were.

  After weeks of digging I finally figured out what each of these variables were.

  - `val` was a predicted value of viscosity
  - `cav` stood for 'compound average value'
  - `wtmcls` was the number of 'water molecules' in the compound
  - `hcpv` was the 'heat capacity value' for that compound

  Now you don't need to understand what this does exactly but consider how much easier it would have been if the code had been written like this:

  ```python
  viscosity_value = a*compound_avg_val + b*h2o_molecules + c*heat_capacity + d 
  ```

  I have done this in my own code. I have worked on code and been lazy with naming. I came back to my code later and found I had to rewrite everything because I couldn't understand what I did before.

  This will take practice but it behooves you to write your variable names (and the rest of your code for that matter) descriptively to avoid issues like the one above. 

  ​	

- **Help your reader understand the code without comments**

  Ideally you want to write code clearly enough that it is apparent what the code does without needing comments explaining it. Comments are important and I do not want to diminish their importance but this clear writing is better than commenting. Up to now what your code does should be obvious to anyone that can read Python without any comments. However, as we go through the next several exercises think of ways you could name your variables so your code is more clear.

Any good programmer knows that the majority of the time we spend coding is actually spent reading and not writing. Python makes it easy for you to write readable code and the first step is write good variable names.

## Hone Your Skills

- Go to the [Python Built-in Function page](https://docs.python.org/3/library/functions.html) and experiment with as many functions in the Python interpreter as you can. What does each of these built in functions do?
- Using the addition operator `+`, write a program that adds two numbers together and then print the result. (Use three descriptively named variables.)
- Experiment with different names of variables in `vars_and_mem.py`. How can you make your variables more clear to those reading your code?

## Advanced Mastery

- Use the internet to answer the following questions:
  - What is binary?
  - How are numbers represented as 1s and 0s?
  - How are characters represented as 1s and 0s?
  - How do computers do addition and subtraction using binary math?
  - What is 2's compliment? Why is it used?



<!-- Navigation -->

---

[Previous: 08-Formatted Strings](./08-Formatted-Strings.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 10-Better String Formatting](./10-Better-String-Formatting.md)

---
<!-- End Navigation -->
