#!/usr/bin/python3
'''
This is the "101-locked_class" module.
The locked_class module contains one class, "LockedClass".
'''


class LockedClass:
    '''This is the "LockedClass" class.
    The class prevents the user from creating any new instance attributes not
    named "first_name".
    '''

    __slots__ = ['first_name']

    def __init__(self, first=""):
        self.first_name = first