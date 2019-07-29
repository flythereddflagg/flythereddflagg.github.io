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
    # help(__name__)
	# help(give_me_an_a)
    # help(Dummy)
    # help(Dummy.__init__)
    # help(Dummy.jump)
    # help(Dummy.slide)