#!/usr/bin/env python
"""
Example of a module with a class and a function autodocumented by sphinx and
readthedos.
"""

class myclass(object):
    """
    Class holding a single member variable x.

    Parameters
    ----------
        val : float, mandatory
            initial value of the instance variable x

    Attributes
    ----------
        var : float storing member value x
    """
    def __init__(self, val):
        self.x = val
    
    @property
    def var(self):
        return self.x
    def setvar(self, x):
        """
        set the value of the member variable var
        Parameters
        ----------
            x : float, mandatory
                value to which var will be set
        Returns 
            None
        -------
        """
        self.x = x

    def square(self):
        x = self.x
        self.x = x*x


def myfunc(x):
    """
    returns the square of the argument x.

    Parameters
    ----------
        x : float, mandatory
            value that you want to square

    Returns
    -------
        float, desired square of x 
    """
    return x *x 
