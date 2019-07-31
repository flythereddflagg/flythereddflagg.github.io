#  30 - Packages and Project structure

This section is low on code but introduces some powerful features of Python that will enable you to scale your code to do large, maintainable projects. Within the next few lessons you will be doing another project. This time your project will be object-oriented. You will use a class structure to do something interesting. You should start thinking about what you want to do right now. So far you have done a project in which you probably made a structure of global variables (i.e. variables that were defined outside of any function or class) and used functions to act on those variables. This project will focus on using the object-oriented features of Python to make the best and most robust piece of software that you can.

However, before we can write these larger codes we must learn how to structure projects to  organize our code. The following exercise will walk you through building a basic structure for your project.

### Building a Basic Project Structure

Go to your CLI, navigate to a place where you will build your project build the following project structure using the CLI commands you have learned. Enter the following commands:

For Linux and Mac:

```bash
$ mkdir emails
$ mkdir ./emails/emails ./emails/bin ./emails/docs ./emails/tests
$ touch ./emails/README.md
$ touch ./emails/emails/__init__.py ./emails/tests/__init__.py
$ touch ./emails/bin/placeholder.txt ./emails/docs/placeholder.txt
$ ls -R ./emails/
```

For windows:

```powershell
> mkdir emails
> mkdir ./emails/emails 
> mkdir ./emails/bin 
> mkdir ./emails/docs 
> mkdir ./emails/tests
> New-Item ./emails/README.md
> New-Item ./emails/emails/__init__.py 
> New-Item ./emails/tests/__init__.py
> New-Item ./emails/bin/placeholder.txt
> New-Item ./emails/docs/placeholder.txt
> ls -R ./emails/
```

When you are done your structure should look like this:

```
./emails/:
	emails
    bin
    docs
    tests
    README.md

    ./emails/bin:
    	placeholder.txt

    ./emails/docs:
    	placeholder.txt
     
    ./emails/emails:
    	__init__.py

    ./emails/tests:
    	__init__.py
```

### The `emails` package

You have just created project called `emails` that contains two packages called `emails` and `tests`. Both of these packages contain an `__init__.py` file. This file tells python to treat the folder that contains it as its own module. Therefore, any code in `./emails/emails/__init__.py` may be imported from emails as: `from emails import a_thing` where `a_thing` is any class, function or variable defined inside of the `__init__.py` script. Other Python scripts may be placed in the folder as well (regardless of the presence of an `__init__.py` script) and classes functions or variables may be imported as: `from emails.module import a_thing` where `module` corresponds to `module.py` inside the folder. The `emails` folder is where we want to put all of our Python source code for the project. The `tests` package is where we can write automated tests for our `emails` package. We will work mainly with these two folders for this section. 

The other two folders are `bin` and `docs` and contain binary or executable files we wish to include with our code and documentation about our code respectively. The structure we have just made is not the only or "correct" way to structure a project but it is a convenient way to start a project. For our purposes it is a good idea not to have an empty folder so we have put a `placeholder.txt` file in each empty folder.

### Make a project

Now that we have our project 'skeleton' in place, copy your working code from the modules section into the `emails` folder. Because you will run this in the context of the `emails` package make sure you change the following imports to reflect this. Change:

```python
from database_manager import DatabaseManager
```

to:

```python
from emails.database_manager import DatabaseManager
```

This will ensure that you are importing from the right environment. If you are using your modules in a project structure you will need to make sure they are referenced correctly or your project will break.

Test your project by opening a python prompt in your project's root directory and executing the following commands:

```python
$ pwd
.../path/to/project/emails/
$ python
Python 3.x.x ...
Type "help", "copyright", "credits" or "license" for more information.
>>> from emails.user_interface import run_ui_test
>>> run_ui_test()
```

Your project should run as it always has.

If the above test worked, congradulations! You have yourself a working project! You can add code to the  `emails` folder or documentation to the `docs` folder as you see fit. But for our purposes, the real utiltiy of the project structure is the abliity you have to automatically test your project with a little tool called `nose`.

This will be covered in the next section.

## Hone Your Skills

- if you haven't already, now would be a good time to turn the documentation in your docstrings into a human readable manual. If you are unsure where to start, try using [pydoc](https://docs.python.org/3.7/library/pydoc.html) and invoke it by using `python -m pydoc`. (Enter `python --help` to get an idea of how this works).
- Begin building your own project! Have an idea you want to see? Start by building a similar project structure as above but replace every instance of `emails` with the name of your own project. Begin fleshing out what you want to see from this project. 


