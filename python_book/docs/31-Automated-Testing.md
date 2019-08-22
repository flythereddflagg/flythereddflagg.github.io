<!-- Navigation -->

---

[Previous: 30-Packages-and-Project-Structure](./30-Packages-and-Project-Structure.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 32-Do-Another-Project](./32-Do-Another-Project.md)

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

### The `assert` statement

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

### Install `nose2`

Go to your terminal and install `nose2` using `pip`.

```
$ pip install nose2 --user
```

Remember that to install Python packages with `pip` it is best to just use the `--user` option to avoid permission errors that can occur on operating systems.

### Make your tests

Put the following file in the `tests` directory of your project. Write out the following tests:

```python
# tests/test_general.py
from emails.database_manager import DatabaseManager
from emails.user_interface import UserInterface
import os


def test_dbman():
    filename = 'data.json'
    name = "./joe manyouare"
    data = [name, 29382984, "coolguy@glasdkfj.com"]
    
    dbman = DatabaseManager(filename)  
    dbman.add_item(data)
    assert name in dbman.__repr__(), "Name not added!"
    
    dbman.remove_item(name)
    assert not(name in dbman.__repr__())
    os.remove(filename) # clean up the file afterward
    

def test_ui_export():
    filename = 'data.json'
    name = "joe manyouare"
    export = 'data.txt'
    data = [name, 29382984, "coolguy@glasdkfj.com"]
    
    dbman = DatabaseManager(filename)
    ui = UserInterface(dbman)
    dbman.add_item(data)
    ui.export(export)
    
    try:
        with open(export, 'r') as f:
            contents = f.read()
        export_exists = True
    except FileNotFoundError:
        export_exists = False
    
    assert export_exists
    
    os.remove(filename)
    os.remove(export) # clean up the file afterward

```

This file may vary somewhat depending on how you implemented your `emails` project. If you find your implementation cannot pass these tests because you structured your project differently, make appropriate changes so that these tests test the "add/remove" functionality of your database manager and the "export" functionality of your user interface.

### Run `nose2`

Now from the root directory of your project run the following commands:

```bash
$ nose2
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
$
```

If you get the above output, congratulations! Your tests all passed! 

### Your Assignment

Write more tests in separate functions to ensure that as many parts of the program are working as possible. If your tests fail, use the principles in the "Do a project" section to debug and fix those problems.  Continue using `nose2` to test your program as a whole until your program is free of bugs. Make multiple test modules to test different sub sections of your code. In each file make multiple tests that test individual units of the module. Remember that each filename must begin with "test" and each variable name must also begin with "test".

## Hone Your Skills

- Use automated testing to drive your development from here on out. Write tests before you write code that do what you want the code to do. Once you have done this, write code that passes those tests.
- Check out the documentation on `nose2` to see how you can better test your programs [here](https://docs.nose2.io/en/latest/).
- Try out other automated testing packages to test your package. You can test some like `py.test` or `unittest` or find others via an internet search.

## Advanced Mastery

- Write a script that does the same thing as `nose` have it walk through all the subfolders of a folder and catch all the errors it finds and report back to the user.

<!-- Navigation -->

---

[Previous: 30-Packages-and-Project-Structure](./30-Packages-and-Project-Structure.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 32-Do-Another-Project](./32-Do-Another-Project.md)

---
<!-- End Navigation -->
