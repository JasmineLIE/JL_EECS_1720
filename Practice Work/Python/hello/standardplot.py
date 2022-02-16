import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot

#You can install libraries within the terminal for use, to access them in a program, you need to switch to that environment which has the libraries
#https://code.visualstudio.com/docs/python/python-tutorial
#To install things, you may be blocked, if so, run this:
'''
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
Select your new environment by using the Python: Select Interpreter command from the Command Palette.
# Windows (may require elevation)
python -m pip install matplotlib
'''