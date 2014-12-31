Here are a list of things that are not working for me:
- _build/html/index.html actually parses attributes from parameters in classes, (built with Sphinx) but is lost in readthedocs
- I put in a setup.py file which can install this project and can be imported into python. However in order to get this to work, I still need to use sys.path.insert in the conf. file. Seems like I shoudl be able to do it without that. 
- The readthedocs page is quite ugly, and the side-bar is not being used at all. In fact the numpy style docs created by sphinx itself is a lot better aesthetically, along with real issues mentioned above.
Have not tried:
1. Testing code using docstrings
