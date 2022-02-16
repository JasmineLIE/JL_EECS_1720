#Variables defined inside a function are treated differnetly from variables defined outside -- these are the two main differences when defining a function 
#Any variables declared inside a function is only accessible within the function -- these are oocal vairables
#Any vairables declared outside a function is known as a global variable and is accessible anywhere in the program

message1 = "Global Variable"

def myFunction():
    print("\nINSIDE THE FUNCTION")
    #Global variables are acccessible inside a function
    print (message1)
    #Declaring a local variable
    message2 = "Local Variable"
    print (message2)

#Calling my function
myFunction()

print("\nOUTSIDE THE FUNCTION")
print (message1)
print (message2)
#GLobal variables are accessible outside function print (message1)
#Local variables are NOT accessible outside function

'''
f you run the program, you will get the output below.

INSIDE THE FUNCTION
Global Variable
Local Variable

OUTSIDE THE FUNCTION
Global Variable
NameError: name 'message2' is not defined

Within the function, both local & global variables are accessible
Outside the function, the local variable message2 is not accessible.  We get a NameError when we try to access it outside the function

The second concept to understand about variable scope is that if a local variable shares the same name as a global variable, any code inside the function is accessing the local variable
Any code outside is accessing the global variable
'''

