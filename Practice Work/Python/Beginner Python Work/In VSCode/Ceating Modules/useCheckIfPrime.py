import sys
if 'C:\\Users\hwafu\OneDrive\Documents\GitHub\JL_EECS_1720\Practice Work\Python\Beginner Python Work\In VSCode\MyPythonModules' not in sys.path:
    sys.path.append('C:\\Users\hwafu\OneDrive\Documents\GitHub\JL_EECS_1720\Practice Work\Python\Beginner Python Work\In VSCode\MyPythonModules')

#to import modules not in the folder of the code -- list of directories that Python goes through to search for modules and files
#so if this folder containing the modules is not here (and it is in this location), then bind it from that location to here
import prime
answer = prime.checkIfPrime(13)
print (answer)
