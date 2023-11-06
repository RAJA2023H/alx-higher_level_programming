#!/usr/bin/python3
"""
MyList that inherits from list
"""

class MyList(list):
    """
    MyList subclass
    """

    def __init__(self):
        """
        intialize MyList object
        """
        super().__init__()

    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))
