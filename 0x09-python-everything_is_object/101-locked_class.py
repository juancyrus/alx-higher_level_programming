#!/usr/bin/python3
class LockedClass():
    """Class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']
