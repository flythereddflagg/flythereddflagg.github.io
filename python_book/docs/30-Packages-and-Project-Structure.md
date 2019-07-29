<!-- Navigation -->

---

[Previous: 29-Comments and Code Documentation](./29-Comments-and-Code-Documentation.md) | [Table of Contents](./00-Table-of-Contents.md) | 

---
<!-- End Navigation -->
#  30 - Packages and Project structure

This section is low on code but introduces some powerful features of Python that will enable you to scale your code to do large, maintainable projects. Within the next several lessons you will be doing another project. This time your project will be object-oriented. You will use a class structure to do something interesting. You should start thinking about what you want to do right now. So far you have done a project in which you probably made a structure of global variables (i.e. variables that were defined outside of any function or class) and used functions to act on those variables. This project will focus on using the object-oriented features of Python to make the best and most robust piece of software that you can.

However, before we can write these larger codes we must learn how to structure projects to  organize our code. The following exercise will walk you through building a basic structure for your project.

### Building a Basic Project Structure

Go to your CLI, navigate to a place where you will build your project build the following project structure using the CLI commands you have learned. Enter the following commands:

```bash
$ mkdir apple
$ mkdir ./apple/apple ./apple/bin ./apple/docs ./apple/tests
$ touch ./apple/README.md
$ touch ./apple/apple/__init__.py ./apple/tests/__init__.py
$ touch ./apple/bin/placeholder.txt ./apple/docs/placeholder.txt
$ ls -R ./apple/
```

When you are done your structure should look like this:

```
./apple/:
	apple
    bin
    docs
    tests
    README.md

    ./apple/bin:
    	placeholder.txt

    ./apple/docs:
    	placeholder.txt
     
    ./apple/apple:
    	__init__.py

    ./apple/tests:
    	__init__.py
```

### The `apple` package

You have just created project called `apple` that contains two packages called `apple` and `tests`. Both of these packages contain an `__init__.py` file. This fiile 

### Make a project

adfs

### Testing with nose

adsf



<!-- Navigation -->

---

[Previous: 29-Comments and Code Documentation](./29-Comments-and-Code-Documentation.md) | [Table of Contents](./00-Table-of-Contents.md) | 

---
<!-- End Navigation -->
