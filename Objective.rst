The purpose of packaging code is to make life easier. This means that there are
 certain features of code that are desirable from the viewpoint of convenience
 of use. So, our objective is to package code in a way such that the following
features, which might be desirable.

We use square brackets to add a more detailed explanataion of the point
Objectives:
----------

- package code, so that the modules in the package can be imported from anywhere in the system either because `python setup.py install` has been used, or `python setup.py build` has been used to install them to a build directory that can be added to python sites. [While it is possible to append pythonpath, both dynamically and statically, there are good reasons to use the setup method). First, this is more standard convention which is necessary for installers like pypy or pip. Secondly, it is a useful way to test code on someone's machine through virtual environments. This is also what happens in readthedocs, which we will use for hosting documentation.]
- Package code in a way so that small datafiles shipped with the code can be found without requiring one to know the absolute paths to data. This is largely so that examples using the code may be written. [Can probably do this through something like _here = something.__file__, and defining data locations relative to that. Is there a better way?]
- Automatic documentation using sphinx, hosted at readthedocs, acting on .rst files. [This means that by following certain syntax rules while using docstrings, in the code itself, it will be possible to look at nice html/latex/pdf documentation linking to source code]
- Automatic testing from docstrings, with methods of switching off particular tests for certain builds (eg. to stop time consuming tests, when relevant parts of code have not been changed) 
- Continuous integration: Check if sets of tests are passing for a particular commit. 
- Versioning: Mapping git hashes to an easily readable version number so that position in code history is trivially available. For branches, this should reference the version of the parent (may or may not be master), and the evolution of the branch. 
- Can I run on a virtual env and install packages that the code may depend on as part of the setup? Do these go into pip-requirements? What if installing some dependency is non-trivial and cannot be achieved by pip. [Our package may depend on other packages. How do we test this in a virtual environment the same way that readthedocs will do.] 
- Why does sphinx need to run the file and find errors? (probably to get inherited properties?)
- How can sphinx help with obtaining attributes and methods of subclasses?
