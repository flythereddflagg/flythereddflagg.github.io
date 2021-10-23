# E1 - Getting Started...Again

<!--How much math should they know?-->

The sections of this book that start with an E indicate that this is a tutorial related to science and engineering. In these sections I assume you know a lot more math and more about how to do basic things on your computer (like downloading and installing programs). Plus, if you have gleaned anything from the first 33 sections of the book then you will know that anything you could want to know about your computer or programming is just an internet search away. Here we will cover some common tools you will need to succeed in the Science-Technology-Engineering-Math (STEM) space. WIthout further ado, lets get started!

## Conda

First things first, I am going to have you uninstall Python. 

"What?" you say in disbelief. Don't worry, we will replace it with something better. Or rather, we will replace it with Python but a different distribution of Python called Anaconda.

### What is Anaconda?

Anaconda is a tool for doing scientific programming in a convenient way using Python. Think of it as Python with some (Read: a whole lot of) extra bells and whistles. If you go to the [Anaconda Download Page](https://www.anaconda.com/products/individual) and get it right now you will download Python bundled with hundreds of other libraries used in for various STEM applications. However, **I am going to recommend you do something different**. Instead of downloading half the internet when you only need a few libraries here and there, I recommend you get [Miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links), which is Anaconda without hundreds of bundled packages. Instead of all those you get one extremely useful tool: conda.

### What is conda?

Conda is what `pip` wishes it could be. We have disucssed how ti install more packages with `pip` but it turns out that many times, especially with packages that are used in STEM programming pip will fail to install them correclty or you will run into other issues where one package depends on another but one specific package version that you cannot upgrade until blah blah blah. If you are doing scientific programming you do not want to bother with all that mess. This is where Conda comes in. Conda keeps track of all of this for you and that should be its main pull and you will find everything is much easier once you just start using it so lets go!

## Reinstall Python (but better)

If you are on Windows, go ahead and uninstall Python. If you are on Mac or Linux, check if Python is naitvely installed on your system if it is then DO NOT UNINSTALL! (Unless you want to break your computer. You do you.)

### Install Miniconda on Windows

Now I could just give you the link to [Miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links), and you could just install it (and if that is what you want to do I fully support your decision). However, I tthink that if you want a smoother and cleaner experience you should use a commandline installer like [Scoop](https://scoop.sh). So to get miniconda:

- Follow the [Scoop](https://scoop.sh) link and follow the instructions at the bottom of the page. (Remember that you can use right-click in Powershell to paste copied commands.)
- Once Scoop is installed, install Git with `scoop install git` (scoop uses git to install and update apps)
- Once Git is installed simpy install Miniconda with `scoop install miniconda3`.
- Once the installation finishes you are done! Yay!

The beautiful thing about command line installers is that it is super fast to install anything you want with little to no drama. Granted, there is a learning curve but once you get the hang of it you will wonder why you did it any other way. Given that you should already be familiar with the command line, this should be simple!

### Install miniconda on Mac

*This space intentionally left blank.*

### Install miniconda on Linux

*This space intentionally left blank.*

## Setup Your Main Environment

Lets install the main packages you will need for most scientific computing. Install the following packages with:

```bash
$ conda install numpy scipy pandas ipython jupyter matplotlib sympy
```

### Wait a second, what did I just do?

Using the Conda package manager, you installed 6 packages and their respective dependecies that are used all the time in STEM programming. You may find you do not need all of these, but they are the most common and there will be introductory sections on all of them. Breifly, they are described here:

- `numpy` 
- `scipy`
- `pandas`
- `ipython`
- `jupyter`
- `matplotlib`
- `sympy`

