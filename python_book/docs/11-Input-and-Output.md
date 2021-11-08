<!-- Navigation -->

---

[Previous: 10 - Better String Formatting](./10-Better-String-Formatting.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 12 - Math and Data](./12-Math-and-Data.md)

---
<!-- End Navigation -->
# 11 - Input and Output

Up to now, we have had our scripts take pre-determined input and turn it into output in the form of text printed to the console screen. Our script does nothing else.  What if we want to be able to do more than that? What if we want to interact with the user? In this lesson we will cover getting and using user input.

Lets start with this exercise:

```python
# input_output.py

# use input() to get user input
user_name = input("Enter your name      : ")
user_age  = input("Enter your age       : ")
user_job  = input("Enter your occupation: ")

# let's print out what we got from the user
print(f"Hello {user_name}! You are {user_age} years old.")
print(f"You work as a/an {user_job}.")
```

**Here is what should happen**

(If needed, see [Section 4](./04-Hello-World.md#making-and-running-your-first-python-file) to review how to run a script.)

```
$ python io_files.py
Enter your name      : John Doe
Enter your age       : 30
Enter your occupation: Panda Caretaker
Hello John Doe! You are 30 years old.
You work as a/an Panda Caretaker.
$
```
**What is happening here?** 

As you can see the built-in `input` function allows you to take user data and store it in variables. Whatever the user enters into the input is saved as a string and you can then do what you wish with it.

### Do a mini project

With this capability, we can start to write programs that can be used by someone other than the programmer! To get you used to this, I want you to write your own first program.

You can do any project you want using everything you have learned so far. If you have something you really want to do, go for it. I only ask that you do the following in your project:

- Use some format statements
- Use the input function

Beyond that you can do any project you want. If you do not know what you want to do I will suggest the following project.

#### The Wacky Stories Game

You may have heard of the game [Mad Libs](http://www.madlibs.com). This is a similar concept that you will implement yourself.

The rules of the game are simple. Take a short story such as the following:

*Jake and John went fishing. While in the boat, Jake got a bite on his line and pulled up the biggest fish either of the men had ever seen. John exclaimed, "Now that is a fish!" The men took it home and made fish and chips.*

The story should be a bit longer but for our purposes this will do. You'll notice that this story is rather mundane so we are going to make it wacky! Take the text of the story and replace key words from the story with a prompt for the type of word in parentheses.

*(Name of person in the room[person 1]) and (Name of different person in the room[person 2]) went (verb ending in 'ing'). While in the (noun), (person 1) got a (noun) on his/her (noun) and pulled up the (superlative adjective) (noun) either of the (plural animal) had ever seen. (person 2) exclaimed, "Now that is a (noun)!" The (plural animal) took it home and made (plural noun).*

Prompt the user for each unique word and save each of these to a variable. Then using what you have learned, print out the complete story with the users words in place of the omitted words so you could get a story like:

*Jill and Mark went farming. While in the needle, Jill
got a Canned air on his/her guitar and pulled up the greatest germ
either of the sloths had ever seen. Mark exclaimed, "Now that
is a gift card!" The cockroaches took it home and made slides.*

### Hone Your Skills

- Play with the "Wacky Stories" concept and make other stories and play the game with friends and family! 

<!-- Navigation -->

---

[Previous: 10 - Better String Formatting](./10-Better-String-Formatting.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 12 - Math and Data](./12-Math-and-Data.md)

---
<!-- End Navigation -->
