
"""
original story:

Jake and John went fishing. While in the boat, Jake got a 
bite on his line and pulled up the biggest fish either of 
the men had ever seen. John exclaimed, "Now that is a fish!" 
The men took it home and made fish and chips.
"""

print("\n\n\t--- Wacky Stories ---\n")
print("Welcome to wacky stories! Please enter")
print("the following types of words:\n")

person_1   = input("Name of person in room > ")
person_2   = input("Name of different person in room > ")
verb1      = input("verb ending in \"ing\" > ")
noun1      = input("noun > ")
noun2      = input("noun > ")
noun3      = input("noun > ")
adjective1 = input("superlative adjective > ")
noun4      = input("noun > ")
animal1    = input("plural animal > ")
noun5      = input("noun > ")
animal2    = input("plural animal > ")
noun6      = input("plural noun > ")

print(f"""
Here is your story:

{person_1} and {person_2} went {verb1}. While in the {noun1}, {person_1}
got a {noun2} on his/her {noun3} and pulled up the {adjective1} {noun4}
either of the {animal1} had ever seen. {person_2} exclaimed, "Now that 
is a {noun5}!" The {animal2} took it home and made {noun6}.
""")