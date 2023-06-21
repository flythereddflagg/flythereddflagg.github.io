# 18 - Iterables

The [Python Documentation](https://docs.python.org/3/glossary.html#term-iterable) defines an iterable this way:

- Iterable: An object capable of returning its members one at a time.

Iterables are a powerful way to structure data. In this lesson, we will introduce a common type of iterable called sequenced types and explore how to use them. Note that there are many iterable types that we will not cover here but these (the sequenced types) are the most common. This is the longest exercise you've done so far so don't get complacent. Make sure that it is exactly as it appears here.

```python
# iterables.py

# --- strings --- 
example_string = "Hello World!"
print("A string:", example_string)
print("") # white space to make output readable

# --- ranges ---
example_range = range(5)
print("A range:", example_range)
print("")

# --- lists ---
# brackets initialize a list
example_list = ["tea", "biscuts", "crackers", "kale"]
print("A list:", example_list)

# lists are mutable
print("adding cheese to the list...")
example_list.append("cheese")
print(example_list)

print("changing the first element to 'Lemon Tea'...")
example_list[0] = "Lemon Tea"
print(example_list)

print("popping off the last element...")
example_list.pop()
print(example_list)
print("")

# --- tuples ---
# parethesis define a tuple
example_tuple = ("tea", "biscuts", "crackers", "kale")
print("A tuple:", example_tuple)

# a comma-separated list can also define a tuple
example_tuple = "biscuts", "crackers",  "kale", "tea"
print("Another tuple:", example_tuple)

# tuples are immutable
# notice how this throws an error:
# comment it out after you have looked at the error
# example_tuple[-1] = "Lemon tea" # throws an error

print("")

# --- Common among iterables ---

# all iterables are subscriptable and sliceable
print("The last element and")
print("The first two elements of each iterable:")
print("Last:",     example_string[-1])
print("First two:",example_string[:2])
print("Last:",     example_range[-1])
print("First two:",example_range[:2])
print("Last:",     example_list[-1])
print("First two:",example_list[:2])
print("Last:",     example_tuple[-1])
print("First two:",example_tuple[:2])
print("")


# all iterables have a length (len())
print("length of string: ", len(example_string))
print("length of range:  ", len(example_range))
print("length of list:   ", len(example_list))
print("length of tuple:  ", len(example_tuple))
print("")

# all iterables can be used to make for-loops
print("For-loop examples of each:")
for character in example_string:
    print(character, end=" ")

print("")
    
for index_value in example_range:
    print(index_value, end=" ")

print("")   
    
for element in example_list:
    print(element, end=" ")

print("")
    
for variable in example_tuple:
    print(variable, end=" ")

print("\n")

# you can check if something is 'in'
# a sequence iterable
print('"Hello" in example_string:', 
      "Hello" in example_string)
print('3 in example_range:', 
      3 in example_range)
print('"kale" in example_list:', 
      "kale" in example_list)
print('"potatoes" in example_tuple:',
      "potatoes" in example_tuple)

```

### Here is what should happen

```
$ python iterables.py
A string: Hello World!

A range: range(0, 5)

A list: ['tea', 'biscuts', 'crackers', 'kale']
adding cheese to the list...
['tea', 'biscuts', 'crackers', 'kale', 'cheese']
changing the first element to 'Lemon Tea'...
['Lemon Tea', 'biscuts', 'crackers', 'kale', 'cheese']
popping off the last element...
['Lemon Tea', 'biscuts', 'crackers', 'kale']

A tuple: ('tea', 'biscuts', 'crackers', 'kale')
Another tuple: ('biscuts', 'crackers', 'kale', 'tea')

The last element and
The first two elements of each iterable:
Last: !
First two: He
Last: 4
First two: range(0, 2)
Last: kale
First two: ['Lemon Tea', 'biscuts']
Last: tea
First two: ('biscuts', 'crackers')

length of string:  12
length of range:   5
length of list:    4
length of tuple:   4

For-loop examples of each:
H e l l o   W o r l d ! 
0 1 2 3 4 
Lemon Tea biscuts crackers kale 
biscuts crackers kale tea 

"Hello" in example_string: True
3 in example_range: True
"kale" in example_list: True
"potatoes" in example_tuple: False
$
```

**What is happening here?**

We have just dumped a lot of information on you. This is probably the longest script you've written yet. We will go through each step by step. Lets start with each type of iterable.

## String

We have already covered a lot about strings. It turns out, however, that strings are iterables and have all the properties that we see at the end of the script. We will deal with these in more detail below but just understand that strings have all those common properties.

## Range

Ranges can be thought of as a very specific subset of a list. The subset is a list of integers with a set pattern. Ranges are most useful in for-loop construction when you want a loop to run a specific number of times. They have other uses but the for-loop case is most common.

## List

A list is a very powerful sequence type. Unlike a string which must contain only letters and a range which can only contain integers in a specified order, a list is exactly what it sounds like. A list is an object that holds objects or references to objects in a specified order. A list could be a shopping list where the elements are strings:

`shopping_list = ["cheese" "milk", "sugar", "eggs"]`

or it could be a list of names of a bunch of file objects:

`files = [file1, file2, file3]`

or it could be a bunch of different types of objects:

`objects = [12, 23.5, "Nougat"]`

The point is, lists can do many things and can be the structure for many types of data. A common use of lists for example is to define matrices for math:

```python
matrix_a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```

which is just a list of lists of numbers. They have all sorts of methods tied to them that can be used to manipulate data. For many of the more complex problems we will tackle, lists or list-like object will be our work horse.

## Tuple

Tuples are interesting beasts in Python. Without getting into gory details, tuples are like lists that cannot be changed once they are created and are fixed in memory. You may think of them as a "read-only" list. You may rightly ask why they even exist if all they appear to be is a less-useful list. The advantage of tuples is that, because they cannot be changed, the computer can use them more efficiently. However, they do have some uses that can be of interest. (See Hone Your Skills for more on this.) 

## Subscripts, Slices and Concatenation

A useful feature all sequenced iterators have is that of subscripting and slicing.  It may not be clear what this means however. The following two operations allow us to conveniently work with sequenced iterables. 

- **Subscript** 

  Suppose we have a list of strings like `shopping_list = ["cheese" "milk", "sugar", "eggs"]` and we just want to get `"sugar"` out of the list. We can do that through subscripting. The "subscript" or "get item" operator is the pair of brackets after the name of the iterator (in this case, `shopping_list[]`). The number that goes between the brackets is the index of the item that is being retrieved. Therefore, if we want to get `"sugar"` out of the list we can store it in a new variable like this: `sugar_item = shopping_list[2]`. (Remember that Python indices start with 0 so the third item in the list has an index of 2.)

- **Slice**

  Slicing is just like subscripting but instead of getting one element of the list we are getting multiple adjacent elements. The syntax is as follows.

   `list_name[first_index : second_index]` 

  where `first_index` is the first included element in the slice and `second_element` is the first element not included in the slice. Therefore if we write `shopping_list[1:3]` we get `['sugar', 'eggs']` back. This is because we are including element `1` and `2` but not `3`. Also, `shopping_list[2:3]` is not the same as `shopping_list[2]` but instead, returns the same type of iterable with a length of 1 containing `shopping_list[2]`. 

  If the `first_index` is omitted, everything from the beginning to the `second_index` is extracted. Likewise, if `second_index` is omitted, everything from `first_index` to the end is extracted.
  
- Like strings, all sequenced iterators may be concatenated with the `+` operator and multiplied by integers. (See the section on Math and Data.)

## For-loops, Length and the `in` operator

Each of the properties that we used in `iterables.py`  that are common to all iterables are both useful and easy to understand given the context we now have.

- **For-loops:** Any iterable used in the definition of a for-loop is defined (as in the lesson on loops) as `for i in iterable:` where `i` can be called the loop variable. In the case of any sequenced iterable the loop variable takes on the next value in the sequence for each loop.
- **`len()`:** This is a built-in function that can find the length of any iterable if it is at all possible. The function has many uses including use for referencing by index instead of element ( i.e. using `range(len(iterable))` instead of just `iterable` in a for-loop.)
- **The `in` operator** will return true if the operand on the left exists as one of the elements on the right or if a series of elements exist on the right. And the logic reads just like in English.

## Hone Your Skills

- Look at documentation on [lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists). Lists can do a lot of things, experiment with each method listed in the documentation. What are some different ways you could use a list?
- The three things common to all iterables we did in `iterables.py` are not the only things you can do to all the sequenced iterables. Look at the [Documentation](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) for operations that can be performed on all the iterables. Experiment with all of these and find out how you could find a delete a particular value from a list using these operations.
- Try putting negative numbers into the subscript operator. Start with `-1`. What happens? How can you use this to your advantage?
- Look up the documentation on [tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) and learn how to pack and unpack variables. How could this be useful?

