<!-- Navigation -->

---

[Previous: 28-Modules](./28-Modules.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 30-Packages and Project Structure](./30-Packages-and-Project-Structure.md)

---
<!-- End Navigation -->

# 29 - Comments and Code Documentation

As you were implementing the project in the previous section, you were guided by the multi-line comment strings under each class or function label. I put those there to guide you but also to introduce you to a style of commenting and documentation used among professionals. 

### Docstrings

The "string literals" or multi-line comments under each labels are recognized by python as documentation strings or "docstrings" for short. You will see these commonly in professional code and you may also use them at the beginning of a module to give general information about the module.

The following example will set out some use cases. Don't bother to write this out just read and understand it.

```python
"""
file: docstrings.py
author: Mark Redd
github: flythereddflagg
about:
    This module has some dummy functions and a dummy class to demonstrate
    proper usage of docstrings.
"""

class Dummy():
    """
    Impliments Nothing of value. Is for demonstration purposes only.
    Notice the indentation level of this doc string. Notice how it
    is different from the methods in this class.
    Attributes:
        a (integer): a meaningless value
        b (string): a meaningless word
    """
    def __init__(self, a, b):
        """Constructor for the Dummy class"""
        self.a = a
        self.b = b
    
    def jump(how_high, when):
        """
        This is a function or method belonging to the Dummy class
        that will take longer than one sentence to explain. Where
        this is the case be as detailed as necessary. Some functions
        are so complex that they require many lines of code to explain
        the intent and use of a function. For such cases it is useful
        to list the parameters and what they mean. e.g. :
        Parameters:
            - how_high (integer): the height you want the dummy to jump
                in feet
            - when (datetime instance): a Python datetime instance specifying
                the moment when you want the dummy to jump
        
        Likewise it is useful to tell what the function returns e.g. :
        Returns:
            - success (boolean): True if the jump completed successfully
                False otherwise.
        """
        return True
    
    def slide(left_right):
        """
        It is not always necessary that you be extremely detailed. For 
        instance you could get the needed information across with 
        something like:
        
        Returns True for a successful slide "left" or "right".
        On an unsuccessful slide, returns False and increments a.
        """
        success = True
        if left_right == "left" and success:
            return True
        elif left_right == "right" and success:
            return True
        else:
            self.a += 1
            return False
        

def give_me_an_a():
    """Gives you an A. Notice the indentation of the doc string"""
    return 'A'

if __name__ == "__main__":
    #help(__name__)
	#help(give_me_an_a)
    #help(Dummy)
    #help(Dummy.__init__)
    #help(Dummy.jump)
    #help(Dummy.slide)
```

### The `help` function

You will see at the bottom of the `docstrings.py` script there are several lines commented out. Copy-paste this script into a separate text file and uncomment those lines one by one. What do they do? You will see the docstrings show up as you do. This can also be done in the interactive prompt. Try the following commands and notice the output.

```python
$ python
Python 3.x.x ...
Type "help", "copyright", "credits" or "license" for more information.
>>> import docstrings
>>> help(docstrings)
>>> help(docstrings.Dummy)
>>>
```

For more information just type `help()` into the prompt. This will turn on the interactive help. This functionality is used by Python programmers everywhere to help the user learn the API. If you need information on a class or function you have imported this will give you what you need.

I have introduced this feature now instead of earlier for a few reasons. Before using the feature, understanding classes and docstrings will help you understand how to use this feature and implement it in your own projects. Therefore from here on out, I expect you to include clear documentation for all your modules, classes and functions.

## Hone your skills

- Go back over some of the scripts and projects you have done so far in the course. Add docstrings to them so they can be used with the `help` function.
- Look up how you can generate web documentation from your docstrings using tools like [pydoc](https://docs.python.org/3.7/library/pydoc.html), [sphinx](http://www.sphinx-doc.org/en/master/) or [Read the Docs](https://readthedocs.org/). See if you can find some other tools to help you do this. (There are many more.)

## Advanced Mastery

- Make a full website from the documentation you pull from your docstrings. You do not have to serve it but make it useable for a website format.

<!-- Navigation -->

---

[Previous: 28-Modules](./28-Modules.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 30-Packages and Project Structure](./30-Packages-and-Project-Structure.md)

---
<!-- End Navigation -->

