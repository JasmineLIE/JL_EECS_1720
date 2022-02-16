'''
The syntax forn defining functions

def functionName(parameters):
    code detailing what the function should do
    return [expression]

There are two keywords here: def and return

def -- tells the program that the indented code from the next line onwards is part of the function
return -- the keyword we use to return an answer in a function

Once the function executes a return statement, the function will exit -- if your function does not need to return any value, you can omit return statement
Alternatively, you can write return / return None
'''

#Function to determine if a given number is a prime number

def checkIfPrime (numberToCheck):
    for x in range(2, numberToCheck): #uses for loop to divide given parameter numberToCheck by all numbers from 2 to numberToCheck
        if (numberToCheck%x == 0): # 1 -- to determine if the remainder is a zero.  If the remainder is zero, numberToCheck is not a prime number.
            return False #Return false and the function exits
        return True #if none of the division gives a rmainder of zero, return True, then the function will exit

checkIfPrime(13)
answer = checkIfPrime(13) #Here, we are passing 13 as the parameter.  We can print the answer by typing print(answer).  We'll get output: True
print (answer)