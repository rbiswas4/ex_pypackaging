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

    Examples
    --------
    >>> x = newfunc(2.)
    >>> x * x
    4.0
    >>> newfunc(3.)
    3.0
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
    
    >>> import numpy as np
    >>> d  = readmatrix('smallmatrix.dat')
    >>> max( abs (d[0] - np.array([3., 2., 1.])) ) < 1.0e-4
    True
    """
    import numpy as np
    import os

    # print _here
    if exampledata:
        dirname = _here 
        fname = os.path.join(_here, 'example_data', fname) 
    # print fname 
    mat = np.loadtxt(fname)

    return mat
