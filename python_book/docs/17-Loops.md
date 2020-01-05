<!-- Navigation -->

---

[Previous: 16-File-Reading-and-Writing](./16-File-Reading-and-Writing.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 18-Iterables](./18-Iterables.md)

---
<!-- End Navigation -->
# 17 - Loops

We are about to introduce another fundamental aspect of programming that will be used over and over again in programming. We will, as always, introduce the subject in an example script.

```python
# loops.py

# we need to print numbers 1 - 5 with each
# number on its own line so:

print(1)
print(2)
print(3)
print(4)
print(5)

# there is a better way of doing this
print("")

n = 1
while n <= 5:
    print(n)
    n += 1

# better! that only took 4 lines of code
# but here is an even better way
print("")

for n in range(5):
    print(n + 1)
```

**Here is what should happen**

```
$ python loops.py
1
2
3
4
5

1
2
3
4
5

1
2
3
4
5
$
```

**What is happening here?**

Here we see the concept of a loop. We just did the same thing (i.e. print numbers 1-5 with each number on its own line) 3 different ways. We will briefly touch on the pros and cons of each way of doing this particular task:

- Writing out each print statement: Never do this. Just don't. Not only is this tedious to do but if you want to do this for 1-10 or 1-1,000,000 the second and third ways require a change to only one variable. This way literally requires 10 or 1,000,000 lines of code respectively. Now that you have seen how terrible this is I will never ask you to do it again. (Remember, the point of programming is to make the computer do the work, not you.)
- A while-loop: The way we have used the while-loop here is not how while-loops should be used. I am only showing it here to introduce the syntax. Again, I have asked you to do it this way once so that we can explore the syntax. After this lesson you should **NEVER** use it this way again. (If you're confused about what "this way" is, don't worry, I'll explain it below.)
- A for-loop: This is, by far, the optimal way to do this particular task. A for-loop is perfect for when you know exactly how many times you want to loop. I will explain while-loops and for-loops below.

### while-loops

I consider while-loops to generally be more simple than for loops. The while-loop follows the following syntax:

```python
while truth_expression:
    do_things1
    do_things2
    ...
# end of the indented block
```

This can be read as "While `truth_expression` evaluates to `True`, `do_things` or else end the loop." The while-loop proceeds as follows:

- The `truth_expression` is some conditional expression like `var > 3` 
- If `truth_expression` evaluates to `True`:
  - The statements in the indented block are executed in order until the block ends 
  - The code then returns to the while statement and evaluates the `truth_expression` again and the process starts over. 
  - This will repeat until `truth_expression` evaluates to `False`. 
- If at any time `truth_expression` evaluates to `False`, the indented block is skipped over and the code continues normally.

`truth_expression` is sometimes known as the *loop exit condition*. For the while-loop we did in `loops.py`, we wanted to loop a particular number of times so we initialized `n` to `1` and then incremented `n` each time before the loop started again.

### for-loops

The built-in function `range` produces a range object which is a type of *iterable*. An iterable is something in code that produces a sequence that can give each value one at a time. It can do this through a number of methods that we will not cover here. In the case of `range` however, it produces a sequence of integer numbers starting with 0. (Remember: Python counting *always* starts with 0.) The sequence increments by integers up to but not including the number passed as an argument. (Note: `range` can be modified to do other things but we will get to that later.) In our case, that means that `range(5)` produced the sequence: `0, 1, 2, 3, 4`. This is a common way to say that we want to do something 5 times (as we see the sequence is 5 elements long) or to count up to from 0 to 4. The `range` function is a common way to do a for-loop but any iterable will do. We will learn more about ranges in the next lesson.

For-loops follow the following syntax:

```python
for i in iterable:
    do_things1
    do_things2
    ...
# end of the indented block
```

A for-loop will only repeat as many times as the iterable fed to it allows. (Again in `loops.py`, this was 5 times.) It also has the feature that, before each time that the loop runs, it defines a variable (which, in the example above, is `i` but you can name it whatever you want) based on the current element of the iterable. Therefore, `i` gets redefined for every iteration of the loop based on the next element of `iterable`. 

Other than that, the statements executed in the indented block are done normally and an un-indentation indicates that the loop block is done and the loop can continue. Once the `iterable` has run out of values to give to `i`, the loop terminates and code continues normally.

In my estimation, for-loops are one of the most powerful features in programming and, as we discussed above, are closely connected with iterables. In the next lesson we will talk more in depth about iterables and how to make and use them.

## Hone Your Skills

- For the while loop in `loops.py`, there are a number of ways we can change the loop exit condition so that the code is technically different but it does the same thing. What are some ways we can change the  loop exit condition to do the same thing? How would each of these be better or worse than the original?
- Play around with the code in `loops.py` and try to change what the `range` function does in a for-loop. Can you make it start at a number *other* than 0? Can you make it count by 2s or 3s? Can you make it count down instead of up? (Hint: The documentation [here](https://docs.python.org/3/library/functions.html#func-range) should be helpful.)

<!-- Navigation -->

---

[Previous: 16-File-Reading-and-Writing](./16-File-Reading-and-Writing.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 18-Iterables](./18-Iterables.md)

---
<!-- End Navigation -->
