#Importing Modules

'''
Python comes with a built-in functions-- these functions are saved in files known as modules
To use built-in codes in Python modules, we have to import them into out program first
Do that first by using import keyword
There are three ways to do it:
'''

#First way: import entire module writing import moduleName

'''
For instance, to import the random module, we write import random.

To use the randrange() function in the random module, we write random.randrange(1, 10)

If you find it too troublesome to write random each time you use the
function, you can import the module by writing import random as
r (where r is any name of your choice). Now to use the
randrange() function, you simply write r.randrange(1, 10).

The third way to import modules is to import specific functions from
the module by writing
from moduleName import name1[, name2[, ...
nameN]].

'''

import random
random.randrange(1, 10)

from random import randrange, randint
randrange(1, 10)

import random as r #r can be any name you want

r.randrange(1, 10)

