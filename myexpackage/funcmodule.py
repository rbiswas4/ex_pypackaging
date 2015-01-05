"""
Added to check the building of documentation with two modules

"""
import os
_here = os.path.dirname(os.path.realpath(__file__))
def newfunc(x):
    """
    returns the argument


    Parameters
    ----------
    x : float, mandatory
        single argument x of the function

    Returns
    -------
    xvalue : float, returns the argument f the function


    .. note:: Yes, this is a stupid function.

    """

    return x

def readmatrix(fname, exampledata=True):
    """
    reads the matrix in an ASCII file to a `np.ndarray`

    Parameters
    ----------

    fname: mandatory, string
        filename for ASCII file containing the data
    exampledata: bool, optional defaults to True
        if true, implies that the file is in the exampledata directory

    Returns
    -------
    matrix : `np.ndarray`
    """
    import numpy as np
    import os

    print _here
    if exampledata:
        fname = os.path.join(_here, fname) 
    print fname 
    mat = np.loadtxt(fname)

    return mat
