#!/usr/bin/env python
"""
example to read example data packaged with the code
"""
import myexpackage.funcmodule as fm
"Just reading a text file without adding paths"
d  = fm.readmatrix('smallmatrix.dat') 
print d
