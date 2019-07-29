<!-- Navigation -->

---

[Previous: 25-Do a Project](./25-Do-a-Project.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 27-Inheritance and Polymorphism](./27-Inheritance-and-Polymorphism.md)

---
<!-- End Navigation -->

# 26 - Objects and Classes

Now that you have finished your project you should feel more or less comfortable with the basics of Python. The next thing to learn about is a new paradigm of programming: Object oriented programming!

There are two shorter exercises in this section as well as some new vocabulary. Ensure that you understand all the terms in **bold** as you go along as these concepts will come up later.

### What is object oriented programming?

In Python, everything is an object. That means that every type of data is held inside a container of memory. Inside this container is everything the object needs to work. For an example, we will use some list objects in Python. Do the following exercise:

```python
# list_objects.py

list_object = []
# this is more or less equivalent to
list_object2 = list()

print("Initial objects", list_object, list_object2)

# now that we have these objects built 
# or "initialized" we can call methods on them!

list_object.append(23)
list_object2.append(24)

print("Added 1 element to each", list_object, list_object2)
list_object.append(36)
list_object2.append(45)

print("Added another element to each", list_object, list_object2)
# now we will remove both elements of each
list_object.pop()
list_object2.pop()
print("Popped off one element", list_object, list_object2)

list_object.pop()
list_object2.pop()
print("Popped off the other", list_object, list_object2)
```

**Here is what should happen**

```
$ python list_objects.py
Initial objects [] []
Added 1 element to each [23] [24]
Added another element to each [23, 36] [24, 45]
Popped off one element [23] [24]
Popped off the other [] []
$
```

From this short exercise you should be able to see the following:

- **Objects must be called into existence by some function**

  You may not see exactly where it happens but when you write `x = []` you are effectively calling `list()` and setting it equal to x. You will not see the details of this but they are implemented in the Python code somewhere. The process of calling an object into existence is called **instantiation** and the function that makes it happen is called an **object constructor.** Another way to think about this relationship is that `list_object1` and `list_object2` are both **instances** of a `list` data type.

- **Objects have and can be modified by methods**

  You have seen before and in this short exercise that functions may be called with dot syntax (e.g. `list_object.pop()`). I have mentioned before that these functions are called **methods** and "belong" to the object they are being called from. A method may do anything the programmer wishes but often are used to modify the object or, more specifically, the data or variables that "belong" to the object. The variables that "belong" to the object are called the object's **attributes**.

### Objects are handled by reference

Since everything is an object in Python, this may not make much sense until you see the effects of this behavior. In Python when you write code like:

```python
x = 2
y = x
y += 3
```

You would rightly expect that `x = 2` and `y = 5`. However should you do something similar with a list:

```python
x = [2]
y = x
y[0] += 3
```

You will find that `y[0] = 5` *and* `x[0] = 5`. This is because you just made two variables `x` and `y` that refer to the same object! This is how all objects behave. The variable names act only as a reference. Therefore when you modified one of the variables it changed the object that both variables pointed to. This idea of only replicating a reference to an object is called a **shallow copy** of an object. If you wish to have a distinct **deep copy** of an list object you may use the `list.copy()` method as follows:

```python
x = [2]
y = x.copy()
y[0] += 3
```

This will return `y[0] = 5` and `x[0] = 2`. This may not make a big difference right now, but understanding this upfront will aid your understanding of how objects behave.

### Classes

Python has a way for the programmer to define their own objects with unique behavior. These are called classes. The next exercise will help you understand how they work.

```python
# learn_classes.py

class Cat():
    species = "Felis catus"
    
    def __init__(self, name, color, favorite_food):
        self.name = name
        self.color = color
        self.favorite_food = favorite_food
    
    
    def print_introduction(self):
        print(f'This is {self.name}. '\
              f'He is of the species \'{self.species}\'.')
        print(f'He is a/an {self.color} cat. '\
              f'He really likes {self.favorite_food}!')



cat1 = Cat("Snowflake", "White", "Fish")
cat2 = Cat("Milo", "Orange", "Bacon")

for cat in [cat1, cat2]:
    cat.print_introduction()

```

**Here is what should happen**

```
$ python learn_classes.py
This is Snowflake. He is of the species 'Felis catus'.
He is a/an White cat. He really likes Fish!
This is Milo. He is of the species 'Felis catus'.
He is a/an Orange cat. He really likes Bacon!
$
```

From this exercise you should see that with the `class` keyword we are defining a new data type or a "class" of objects. Therefore each object created from the "class" template is also called an **instance** of that class. As I said before, in Python, everything is an object. That means that somewhere in the Python source code there must be some Python `class` definition (or some equivalent definition) that defines the structure and behavior of all Python objects.

### Defining Behavior and Data Structures

It may not be obvious right now but, this structure of programming allows you to scale your programs in a very powerful way. In a class, the programmer may define any behavior he/she wants for the class of objects once and may reuse that behavior for every instance of the class. The way that behavior is defined is via **methods** and **attributes**.

#### Attributes and the `self` variable

Any object that is contained by the class or object is considered an attribute of the class or object. This includes functions and the data members inside the class. Functions inside the class are called **methods** and **members** are generally any other objects contained in the class. These are generally referenced in code with the dot syntax (i.e. `object_name.attribute_name`). However, you may have noticed that inside the class definition you see that they are referenced using the `self` variable. 

`self` is just a variable that could be named anything but is used by convention in Python. It is a reference to the **instance** of the object that is referring to the attribute. Therefore when you instantiated the cats named "Snowflake" and "Milo" when you called `.print_introduction` on both of them they produced their respective data types in the print statement. In the class definition, if one simply tried to print `name` instead of `self.name`, Python looks for a global variable called name and will throw an error if it cannot find one.

#### Methods

**Methods** are just functions defined in the class definition and operate solely within the context of the class or **instances** of the class. Methods are there to define how a class will behave. In fact, a class can be altered to act in all sorts of useful ways (see [Advanced Mastery](#Advanced-Mastery) below). As a matter of good coding practice, methods should alter the class's members or return outputs of the class but should not alter other objects or classes not referred to by the class.

## Hone Your Skills

- Experiment with how objects are handled by reference. Try doing different things with lists for example.  Can you predict what different actions will do to an object?
- Make your own classes and experiment with what you can do. How can this make your programs cleaner? Consider the project you just did in the previous lesson. How could object-oriented programming simplify and improve your code?

## Advanced Mastery

- Look up operator overloading in Python and see if you can write some classes that do it. You may want to implement something like how complex numbers should act or numbers with units.

<!-- Navigation -->

---

[Previous: 25-Do a Project](./25-Do-a-Project.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 27-Inheritance and Polymorphism](./27-Inheritance-and-Polymorphism.md)

---
<!-- End Navigation -->
