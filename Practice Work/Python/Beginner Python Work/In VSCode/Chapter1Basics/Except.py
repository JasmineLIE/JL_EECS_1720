#A control statement that controls how the program proceeds when an error occurs

'''
Syntax:

try:
    do something
except:
    do something else when the erorr eccors
'''

try:
    answer =12/0
    print (answer)
except:
    print ("An error occured")

#When the program is run, you get message "An error occured".  
#This is bc when the program tries to execute the statement =12/0 in try block, error occurs since it cannot divide numbers by zero
#The remaining of the try block is ignored and the statement in the except block is executed instead

#Fore more specific error messages:

try:
    userInput1 = int(input("Please enter a number:"))
    userInput2 = int(input("Please enter another number: "))
    answer = userInput1/userInput2
    print("This answer is", answer)
    myFile = open("missing.txt", 'r')
except ValueError:
    print ("Error: You did not enter a number")
except ZeroDivisionError:
    print ("Error: Cannot divide by zero")
except Exception as e:
    print ("Unknown error:", e)

'''
The list below denotes the various outputs for different user inputs
>>>>denotes the user input and => denotes the output

>>>Please enter a number: m
=> ERROR: You did not enter a number

Reason: User entered a string which cannot be cast into an integer
This is a ValueError. Hence, the statement in the except

ValueError block is displayed.
>>>Please enter a number: 12
>>>Please enter another number: 0
=> Error: Cannot divide by zero

Reason: userInput2 = 0. Since we cannot divide a number by
zero, this is a ZeroDivisionError. The statement in the except
ZeroDivisionError block is displayed.

>>>Please enter a number: 12
>>>Please enter another number: 3
=> The answer is 4.0
=> Unknown error: [Errno 2] No such file or
directory: 'missing.txt'

Reason: User enters acceptable values and the line print ("The
answer is ", answer) executes correctly. However, the next
line raises an error as missing.txt is not found. Since this is not a
ValueError or a ZeroDivisionError, the last except block is
executed.

ValueError and ZeroDivisionError are two of the many predefined error types in Python. ValueError is raised when a built-in
operation or function receives a parameter that has the right type but
an inappropriate value. ZeroDivisionError is raised when the
program tries to divide by zero. Other common errors in Python
include

IOError:
Raised when an I/O operation (such as the built-in open() function)
fails for an I/O-related reason, e.g., “file not found”.

ImportError:
Raised when an import statement fails to find the module definition

IndexError:
Raised when a sequence (e.g. string, list, tuple) index is out of
range.

KeyError:
Raised when a dictionary key is not found.

NameError:
Raised when a local or global name is not found.

TypeError:
Raised when an operation or function is applied to an object of
inappropriate type.

For more error types:
https://docs.python.org/3/library/exceptions.html

'''

#Python also comes with pre-defined error messages for each of the different types of errors
#IF you want to display the message, use the keyword after the error type
#E.x: to display ValueError message write:

'''
except ValueError as e: 
    print(e)

e is the variable name assigned to the error.
You can give it some other names, but it is common practice to use e. 
The last except statement in our program:

except Exception as e:
    print:("Unown Error: ", e)
'''