#Attributes and methods instead of functions and elements (?)

class Employee:
    '''
     pass #pass if you want to leave a class empty; pass lets Python know you want to skip a line
    '''
    def __init__(self, first, last, pay): #The constructor -- initialize
    #after self, specify what other arguments you want to accept
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self): #Each method within the class automatically takes the instance as the first argument
        return '{} {}'.format(self.first, self.last)

        #Though we're not passing an arguments, emp_2. along is an instance being passed through the function, that's why we need (self)

#class is a blueprint for creating instances

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 50000) 

#These are unique isntances for the Employee class -- have different locations and memory

#Instance variables contain data unique to each instance
'''
#What above does is this:

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000 

'''
print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname()) #Without the parenthesis it just prints the method instead of the return value of the method
print(emp_2.fullname())

print(Employee.fullname(emp_1))