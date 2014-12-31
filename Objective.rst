This is a list of objectives that woudl be nice to have working in the packaging:

Objectives:
----------

- Setup so that the modules in the package can be imported from anywhere in the system either because `python setup.py install` has been used, or `python setup.py build` has been used to install them to a build directory that can be added to python sites.
- Setup a way to see data files that are part of the package. ie. if one imports the package at some location on the machine, the data should be loaded in the same way. (Can probably do this through something like _here = something.__file__, and defining data locations relative to that. Is there a better way?)
- Automatic documentation using sphinx, hosted at readthedocs, acting on .rst files
- Automatic testing from docstrings, with methods of switching off particular tests for certain builds (eg. to stop time consuming tests, when relevant parts of code have not been changed)
- Continuous integration
- Versioning: Mapping git hashes to an easily readable version number so that position in code history is trivially available. For branches, this should reference the version of the parent (may or may not be master), and the evolution of the branch. 

