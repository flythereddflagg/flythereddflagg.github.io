
# 7 - Escape Characters

Based on the previous section, you may ask "What do I do if I need a string to have a mixture of double and single quotes?" For example:

```
John's character says, "I'd like to buy some cheese."
```

This is where escape characters come in handy. An escape character is a text character that can be represented by a backslash (`\`) followed by a character or series of characters (e.g. `\t`, `\n`, `\u03b7`). Escape characters make possible the mixing of single and double quotes (among many other things) as you will see in this next exercise.

Now go back to your text editor and write the following code (again, do NOT copy-paste it). Notice the use of escape characters and try to figure out what each one does.

```python
# esc_chars.py

# here is an example of the use of escape characters
# Both of lines do the same thing
# Why might you prefer one over the other?
print("John's character says, \"I'd like to buy some cheese.\"")
print('John\'s character says, "I\'d like to buy some cheese."')

# here are some more escape character examples
# notice what all the other escape characters do
print("\nThere once was an old man from Peru")
print("who dreamed he was eating his shoe.")
print("\tHe woke up in fright,")
print("\tin the middle of the night,")
print("and found it was perfectly true!\n\n")

# here are a few more new characters and examples
print("\t\tI have tabbed over here!")

print("I am about to do a carriage return!\rI did it!--")

print("How do you print a backslash? \\ like that!")

print("\nI just made a new line! Now I will do another!\n")
print("Here is a greek eta character: \u03b7")
```

### Here is what should happen

(If needed, see [Section 4](./04-Hello-World.md#making-and-running-your-first-python-file) to review how to run a script.)

```
$ python esc_chars.py
John's character says, "I'd like to buy some cheese."
John's character says, "I'd like to buy some cheese."

There once was an old man from Peru
who dreamed he was eating his shoe.
	He woke up in fright,
	in the middle of the night,
and found it was perfectly true!


		I have tabbed over here!
I did it!--to do a carriage return!
How do you print a backslash? \ like that!

I just made a new line! Now I will do another!

Here is a greek eta character: η
```

If on any of these exercises you do not see the output appear *exactly* as you saw it in the book, go back and fix it until it does. 

### What is happening here?

Let's examine all the escape characters introduced in this exercise:

- `\'` and `\"`: These are quote escapes and tell python to treat them as part of the text of the string rather than the beginning or ending of a string. Hence, both times you wrote the mixed quote sentence you could enclose the text with either `"` or `'` and print the same string depending on which escapes you used.
- `\n`: This is a newline character and printing it makes a newline on which you can continue to write text. The print statement automatically adds this character to the end of the given string. In some languages like C you must explicitly put in this character yourself.
- `\t`: This is the tab character and printing it inserts 4 or 8 spaces depending on the system you are using.
- `\r`: This is the carriage return character and it returns the cursor to the beginning of the line. Once this happens any subsequent characters printed overwrite the previous ones. Notice how the first part of the printed line is now overwritten with the "I did it!" part.
- `\\`: This is the backslash character and tells python to treat this character as a single backslash. As you can see, the only thing that came out of the print statement was a single backslash.
- `\u03b7`: This is called a "<span title="Unicode: formally the Unicode Standard, an information technology standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems.">**Unicode**</span> escape character". The computer knows that if it encounters a `\` followed by a `u` it will expect a 4-digit <span title="Hexadecimal: A base-16 number system that includes digits 0-9 and the letters A, B, C, D, E, F (case-insensitive) to represent numbers. Often, you will see hexidecimal numbers prepended with '0x' to indicate that they are hexidecimal.">**hexadecimal**</span> code to follow. It follows the format `\uhhhh` where `hhhh` is the 4-digit hexadecimal code that corresponds to what was printed (in this case, $\eta$). Using that 4-digit hexadecimal code you can express over 65000 characters (a massively larger character set than the standard 128 characters used in <span title="ASCII: American Standard Code for Information Interchange; ASCII text: a standardized code in which characters are represented for computer storage and transmission by the numbers 0 through 127.">**ASCII text**</span>). If you want to know a character's code simply search on the internet for "Unicode *CHARACTER NAME*". (e.g. "Unicode eta" for $ \eta $)

These are not all the potential escape characters. You can learn more about these by doing the exercises under [Hone your skills](#Hone-your-skills). For now, understand that these are only a small part of python's printing and display capabilities but what we have covered here are the most useful and used most often in programming. 

## Hone Your Skills

- Look up what hexadecimal is. Why is it used?
- Using the Internet and experimenting in Python, figure out what the following escape characters do.
  - `\a`
  - `\b	`
  - `\f	`
  - `\N{char}	`
  - `\o**	`
  - `\x**	`
- Look up how to make Python print $\epsilon = \gamma c^2$ (those are the greek letters epsilon ($\epsilon$) and gamma ($\gamma$) and the equation reads: "epsilon equals gamma c squared")

## Advanced Mastery

- Make Python print out the [Navier-Stokes Equations](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations) for a 3-D system in Cartesian coordinates formatted like a normal math equation using escape sequences and print statements.

