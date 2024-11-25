# 27 - Inheritance and Polymorphism

As we saw from the last lesson, object oriented programming allows us to scale our software in a convenient way. There is another powerful way object-oriented programming allows us to structure our programs. That is through a family-like structure called inheritance that gives rise to polymorphism. The following exercise will illustrate how one may use this programming to their advantage.

```python
# inheritance.py

class Automobile():
    '''
    This is the base "parent" class and 
    generally should not be instantiated.
    '''
    number_of_doors = 2
    
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        
    def __repr__(self):
        return f"""Automobile Data:
Year of manufacture : {self.year}
Automobile make     : {self.make}
Automobile model    : {self.model}"""


class Truck(Automobile):
    '''
    A Truck object is a type of Automobile.
    '''    
    def __init__(
        self, year, make, model, bed_type, bed_size, axel_weight
    ):
        super().__init__(year, make, model)
        self.bed_type = bed_type
        self.bed_size = bed_size
        self.axel_weight = axel_weight

        
class Sedan(Automobile):
    '''
    A Sedan is not a Truck but is a type of Automobile.
    '''
    number_of_doors = 4
    
    def __init__(self, year, make, model, engine_type, engine_size):
        super().__init__(year, make, model)
        self.engine_type = engine_type
        self.engine_size = engine_size
        

class Coupe(Automobile):
    '''
    A Coupe is not a Sedan or a Truck but is a type of Automobile.
    '''    
    def __init__(self, year, make, model, engine_type, engine_size):
        super().__init__(year, make, model)
        self.engine_type = engine_type
        self.engine_size = engine_size
        

class Corvette(Coupe):
    '''
    A Corvette is a specific type of Coupe.
    '''
    def __init__(self, year, edition, engine_size):
        super().__init__(
            year, "Chevrolet", "Corvette", "V8", engine_size
        )
        self.edition = edition

    def __repr__(self):
        return f"""This car is a {self.make} {self.model},"""\
    		   f""" {self.edition} Edition made in {self.year}.
It has a {self.engine_size} cubic-inch {self.engine_type} engine."""\
			f"""It is awesome!!!"""
    

t = Truck(1990, "Ford", "F-250", "Flat", "Long (8')", '3/4 Ton')
s = Sedan(2017, "Hyundai", "Elantra", 'Straight 4', 92)
p = Coupe(2012, "Toyota", "Camry", "V6", 205)
c = Corvette(1975, "Sting Ray", 350)

for car in [t,s,p,c]:
    print(car, '\n')

```

**Here is what should happen**

```
$ python inheritance.py
Automobile Data:
Year of manufacture : 1990
Automobile make     : Ford
Automobile model    : F-250 

Automobile Data:
Year of manufacture : 2017
Automobile make     : Hyundai
Automobile model    : Elantra 

Automobile Data:
Year of manufacture : 2012
Automobile make     : Toyota
Automobile model    : Camry 

This car is a Chevrolet Corvette, Sting Ray Edition made in 1975.
It has a 350 cubic-inch V8 engine. It is awesome!!! 
$
```

### Inheritance

Classes have the following syntax to define them:

```python
#     class
#     name
#      |
#      v
class Name(Parent):
#  ^          ^
#  |          |
# class     parent 
# keyword   class 
#           name
```

That is, the class with the name `Name` is a type of the previously-defined class called `Parent`. This means that class `Name` "inherits" all the attributes from the `Parent` class.  We saw this in `inheritance.py` when we had a parent class, `Automobile`, pass its attributes to each of its children. For example, in the `Truck` class we see that a `Truck` instance was able to use the `__repr__` method belonging to the `Automobile` class without it having to be explicitly coded in the `Truck` class. Another way of describing the relationship between `Automobile` and `Truck` is that a `Truck` class is a type of `Automobile` class.

This is a very useful feature as it allows a programmer to avoid having to recode every method and attribute for a set of similar classes. This also allows a clean structuring of sub-classes or "child" classes to produce powerful data structures. Much of this will come to bear later on when we do more interesting things with object-oriented programming.

### Polymorphism

Another feature of inheritance is the idea that a child class need not be exactly the same as its parent class. In fact, a the utility of this construct hinges on the idea that a child class can be a specialized instance of a parent class. This allows the creation of many child classes that specialize in particular things. The child class may take the attributes that the parent class has and build on them, adding its own attributes and methods to do what it needs to do. This concept is called "polymorphism" meaning "having many forms". After experimenting with this structure, it should become apparent how this may be used to build large data structures that model complex systems.

We saw this as well in the `Truck` class. The `Automobile` parent class had only 4 attributes namely, `number_of_doors`, `year`, `make` and `model`. The `Truck` class expanded on this data set by adding attributes that are specific to a `Truck`, namely `bed_type`, `bed_size` and `axel_weight`. Furthermore, each child class of `Automobile` brought something unique to the table by adding its own attributes or methods. In the case of the `Corvette` class,  it inherited from the `Coupe` class, a sub-class of `Automobile`. This means it took all the attributes of both the `Automobile` class and the `Coupe` class and then added its own methods and attributes. 

### Overriding and the `super` function

You may have also noticed that sometimes things defined in a parent class are redefined in a child class. This is not an accident. It is common to have a generic implementation of each method in a parent class and then a specific implementation in the child classes tailored to their specific needs. When any method or attribute is redefined in a child class this is called "overriding" the method or attribute.

This is something you can and absolutely should do when programming. It is one of the great strengths of object-oriented programming and allows the utility of polymorphism to be expressed to its fullest extent. We saw this above in every child implementation of the constructor method or `__init__` method. Every child has an `__init__` method distinct from each other and the parent class. That means the the original `__init__` belonging to `Automobile` was overridden by each child. Other overriding examples are in the `__repr__` function and the `number_of_doors` variable. In each case the overriding was done to make the class act in a unique way by defining specific behavior for a given method.

One important drawback of overriding a parent method is that, for the child, the parent's version of the method is no longer available to use if needed. To deal with this and make classes more flexible, Python has the [`super`](https://docs.python.org/3/library/functions.html#super) function. This function returns a temporary instance of the parent of the class from which it was called. This instance can be then used to call a parent's implementation of any method. As we saw above we needed to ensure that `year`, `make` and `model` were defined in the class structure for each child but rather than writing 3 extra lines of code for each child, we simply pass in the needed variables and then use `super().__init__(year, make, model)` to get the parent class to do that for us. Furthermore, the `Corvette` class specified some variables that would always be true for itself when calling the parent `Coupe` class.

For each of these features we have introduced some of the possible uses of each but you should understand that we have only scratched the surface of what object-oriented programming can do. In later lessons you will have the opportunity to use these principles in a more powerful and tangible way.

### The `__repr__` method

One thing you may still have questions about is the `__repr__` method. The `__repr__` name stands for "representation" and is intended to return a string representation of the object. 

One more powerful feature of object-oriented programming is the idea that a given method name will act in an expected way in any instance of an object. Remember that in Python, everything is an object. Therefore when we call `print(obj)` where `obj` is the object we wish to print, what is actually happens is that the `print` function looks at the object and calls its `__repr__` method (i.e. it calls `obj.__repr__()`) or some equivalent command. To make this work for any Python object, every object must have a default implementation of `__repr__`. Python enforces this by making all objects inherit from a base class that implements basic functionality like having a default string representation of any object. Therefore, when you implement a `__repr__` method you are overriding the Python base class's implementation of `__repr__` and when you call `print` on some instance of the class. This will be inherited by any children of that class unless they override the definition too. There are more functions like `__repr__` that allow you to customize your classes. You can learn more about them in [Advanced Mastery](#Advanced-Mastery) below.

## Hone your Skills

- Copy your code from `inheritance.py` into a separate text file and use code comments to mark every example in the code of children using inherited traits with something like `# inheritance used here`. Mark up the code in a similar fashion for every example of polymorphism and every example of overriding. 

- You may notice that each automobile class has more data to offer than just its year, make and model. Implement `__repr__` for every class so all of their data members are shown when you print them.
- Add a method and data attribute that sets and adjusts the color of the car. Add this color to the `__repr__` method for each class.
- Add other methods and attributes to all the children in `inheritance.py` that more fully describe each class. Why would you want certain attributes? Are there some you wouldn't want or some that are unnecessary?
- Make sure you can understand the code, then make a separate parent-child class structure using another concept with which you are familiar. For example, you could make a similar structure with genres of music or animals. Start with a parent class that defines attributes and methods that will be common to all the children.  Then define child classes that inherit from that parent and have attributes of their own especially attributes that override the parent attributes.

## Advanced Mastery

- Learn more about customized methods in the [Python Documentation](https://docs.python.org/3/reference/datamodel.html#basic-customization) on the subject. Why would you want to alter these types of functions?

- Implement operator overloading for some classes you make up yourself. These classes could represent complex numbers or numbers with units.  

  

