#TO create a module, save the file with a .py extension and put it in the same folder as the Python file you are going to import it from

def checkIfPrime (numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0):
            return False
    return True

