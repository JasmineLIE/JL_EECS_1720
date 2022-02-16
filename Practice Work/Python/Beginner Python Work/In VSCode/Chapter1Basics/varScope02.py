'''
The second concept to understand about variable scope is that 
if a local variable shares the same name as a global variable,
any code inside the function is accessing the local variable
Any code outside is accessing the global variable
'''

message1 = "Global Variable (shares same name as a local variable)"

def myFunction():
    message1 = "Local Variable (shares same name as a global variable)"
    print ("\nINSIDE THE FUNCTION")
    print (message1)

#Calling the function
myFunction()

#Printing message1 OUTSIDE the function
print("\nOUTSIDE THE FUNCTION")
print(message1)

'''
You’ll get the output as follows:

INSIDE THE FUNCTION
Local Variable (shares same name as a global
variable)

OUTSIDE THE FUNCTION
Global Variable (shares same name as a local
variable)

When we print message1 inside the function, it prints "Local
Variable (shares same name as a global variable)"
as it is printing the local variable. When we print it outside, it is
accessing the global variable and hence prints "Global Variable
(shares same name as a local variable)"

'''