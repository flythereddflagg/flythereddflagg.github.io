<!-- Navigation -->

---

[Previous: 30-Packages-and-Project-Structure](./30-Packages-and-Project-Structure.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: index](./index.md)

---
<!-- End Navigation -->
# 31 - Automated Testing

In some sense, the job of a programmer is to get a computer automatically do a task that someone else would have to do. The best programmers automate everything they can, including programming itself where possible. This section in particular will help you automate what can be one of the most necessary and evil necessary evils of programming. Testing your programs.

### Test-Driven Development

I have mentioned before that taking some time to plan your project will make the process of programming easier. One way to do this is to make programs that test whether your program performs as expected. Do this before you even write one line of code for your project. This forces you to ask important questions about your program such as: What do I want my program to actually do? How well does it have to do it? What things will cause the code to crash?

The programmer does not need to answer all these questions before beginning but it is helpful to have some basic tests ready before beginning a project. More tests can be added as the project progresses. However as you add many tests you will want to automate that part of the process as well. To do this we have a powerful tool called `nose`.

### About `nose`

At the time of writing, the original `nose` package has been replaced by `nose2` which will be maintained for the foreseeable future and has more features than the original `nose`. Therefore, this section will be an introduction on how to use `nose2` instead of `nose`. However, `nose` and `nose2` are hardly the only packages that can do automated testing. The `nose2` package is relatively easy to use and has plenty of features. For these reasons I have elected to use it to demonstrate automated testing techniques. Below I have included an exercise to allow the reader to try a few different automated testing packages.

`nose2` works by being called in your project's root directory and searching for folders and files with names beginning with 'test'. It then runs all functions with names beginning with 'test'. If no errors occur then it gives them a pass. It then reports back what passed and what failed. The general failure conditions are 'E' for error and 'F' for assertion error. The `assert` statement is the way an assertion error is raised.

### `assert`

Open up an interactive Python prompt and practice with the `assert` statement.

```python
$ python
Python 3.X.X ...
Type "help", "copyright", "credits" or "license" for more information.
>>> assert 1==1
>>> assert 1==0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> assert 1==0, "Those numbers are not equal!"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Those numbers are not equal!
>>> assert 1 is 1
>>> assert "k" is "k"
>>> x = []
>>> y = []
>>> assert x is y, "x is not y!"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: x is not y!
>>>
```

From this you should quickly gather that the assert statement checks the Boolean truth value of the expression after it and then does nothing if it is true and raises an `AssertionError` if it is false. If a string message is included by separated commas then it will print that message out with the `AssertionError`. Many automated testing packages use this feature to test packages. Use this as much as you can. It will help you code more efficiently and effectively.

### Install `nose`

asdf

### Make your tests

afds

### Run `nose`

## Hone Your Skills

- Use automated testing to drive your development from here on out. Write tests before you write code that do what you want the code to do. Once you have done this, write code that passes those tests.
- Try out other automated testing packages to test your package. You can test some like `py.test` or `unittest` or find others via an internet search.
- Write a script that does the same thing as `nose` have it walk through all the subfolders of a folder and catch all the errors it finds and report back to the user.

<!-- Navigation -->

---

[Previous: 30-Packages-and-Project-Structure](./30-Packages-and-Project-Structure.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: index](./index.md)

---
<!-- End Navigation -->