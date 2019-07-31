
# 20 - Dictionaries

In the last lesson we learned about sequenced iterables. In this lesson we will learn about one of the most powerful iterables that does not exist in a sequence. This is called a dictionary. The following lesson will introduce and illustrate how to use a dictionary.

```python
# dictionary_practice.py

# curly braces or just "braces" define a dictionary
player_data = {"Name":"Jack", "Team":"Wildcats", "Wins":3}

#  we subscript with a keyword instead of an index,
print(player_data["Name"])
print(player_data["Team"])
print(player_data["Wins"],"\n")

# a dictionary is an iterable
for key in player_data:
    print(key, ":", player_data[key])

print("")

# another possibly better way to do the same thing
for key, value in player_data.items():
    print(key, ":", value)
    
print("")

# dictionaries are mutable and extendable
player_data["Wins"]  += 1
player_data["Height"] = "6'2\""

for key, value in player_data.items():
    print(key, ":", value)
    
print("")

# you can also delete items too
del player_data["Height"]

for key, value in player_data.items():
    print(key, ":", value)
```

**Here is what should happen**

```
$ python dictionary_practice.py
Jack
Wildcats
3 

Name : Jack
Team : Wildcats
Wins : 3

Name : Jack
Team : Wildcats
Wins : 3

Name : Jack
Team : Wildcats
Wins : 4
Height : 6'2"

Name : Jack
Team : Wildcats
Wins : 4
$
```

### Dictionaries

A dictionary is a mapping type, that is, a data type that takes one kind of object and connects it to another. In other programming languages this is Dictionaries are nothing short of magic in programming for their efficiency and usefulness. A dictionary can be like a mini database or a convenient way to describe almost any object.

As we saw above, dictionaries can be thought of as a list of unique keys that, when passed in the subscript operator, return a corresponding value. These key-value pairs allow a data structure that acts like a literal dictionary. This short lesson is only do introduce dictionaries but there are many things you can do with them.

<!-- Continue Here -->

## Hone Your Skills

- Look up the documentation on[ Mapping Types (dictionaries)](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) and experiment with all the dictionary methods. Think about how you might go about making a dictionary that can turn English into Python code.

## Advanced Mastery

- Search the Internet and learn about hashmaps and how they work. From what you learn, why are dictionaries/hashmaps so efficient? How can you use this to make your code better?

