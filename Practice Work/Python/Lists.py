#Type Casting in Python -- To convert one data type to another

'''
The three built in functions in Python to allow us to type-cast
int(), float(), and str() functions

int() takes a float/appropriate string and converts it into an integer.
For floats to integer, the decimal is cut off
For strings to intgers, any whole numbers are converted, but words and deicmals are not

'''

#List --  a collection of data, normally related

#Declaring a list"

'''
listname = [initial values]
'''

userAge = [21, 22, 23, 24, 25]
listName = [] #Can also declare without assigning any variables

#We use append() method to add items to a list

userAge[0] = 21
userAge[1] = 22

#The last item in the list has an index of -1, the second last has index of -2, and so on so forth

userAge[-1] = 25
userAge[-2] = 24

#Can assign a list, or part of it, to a variable

userAge2 = userAge

userAge3 = userAge[2:4]
#Here, you are assiging items with index 2 to index 4-1 from the list userAge (index 2&3)
#Notation 2:4 is known as a slice; when we use a slice notation, the items at the start index is always included, but the items at the end are excluded
#The slice notation includes a third number known as the stepper
'''
userAge4 = userAge[1:5:2] --  we will get a sub list containing every second number ffom index 1 to 5-1, because the stepper is 2
Hence, userAge4 = 22, 25]

userAge[ :4] gives value from index 0 to 4-1
userAge[1: ] gives values from indez 1 to index 5-1 (since the size of userAge is 5; it has 5 items)

'''

#To modify items in a list, write listNamepindex of item to be mofided] = new value

userAge[1] = 5
#If you want to modify the second item, now the list becomes userAge = [21, 5, 23, 24, 25]

userAge.append(99)
#99 is now added to the end of the list

#To remove items, write del listName[index of item to be deletd]

del userAge[2]

#Now the list becomes userAge = [21, 5, 24, 25, 00] (the third item was deleted)


#declaring the list, list elements can be different data types

myList = [1, 2, 3, 4, 5, "Hello"]

#print the entire list
print(myList)

#print the third item
print(myList[2])

#print the last tiem
print(myList[-1])

#assign myList (from index 1-4) to myList2 and print myList2
myList2 = myList[1:5]
print(myList2)

#modify the second item in myList and print the updated list

myList[1] = 20
print(myList)

#Append a new item to myList and print the updated list
myList.append("How are you")
print(myList)

#remove the sixth item from myList and print the updated list
del myList[5]
print(myList)

#Tuples
'''
Tuples are ilke list but you cannot modify their values -- the intiial values will stay for the rest of the program
Useful for when your program needs to store things like names of the months of the year
'''

monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

#You can access individual values of a tuple using their indexes like w/ list
'''
monthsOfYear[0] ' "Jan"
monthsOfYear[-1] = "Dec"
'''
print(monthsOfYear)
