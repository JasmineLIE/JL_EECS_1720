#A dictionary is a collection of data PAIRS -- e.x: if we want to store username and age of 5 users
'''
To declare:
dicitonaryName = {dictionary key : data}

'''

myDictionary = {"Peter":38, "John":51, "Alex":13, "Alvin":"Not Available"}

#Can also declare using dict() method

userNameAndAge = dict(Peter = 38, John = 51, Alex = 13, Alvin = "Not Available")

#To access individual items in dictionary, use dictionanry keys
userNameAndAge["John"] #You'll get the value 51

#To modify items:
userNameAndAge["John"] = 21

diciotnaryName = {} #To declare a dictionary without asigning any intiial values

#To add itmes:

userNameAndAge["Joe"] = 40

#To remove items:
del userNameAndAge["Alex"]
                   

#Declaring the dictionary, dictionary keys and data can be different data types
myDict = {"One":1.35, 2.5:"Two Point Five", 3:"+",7.9:2}

#print entire dir.
print(myDict)

#Print certain items
print(myDict["One"])
print(myDict[7.9])

#Modify the items
myDict[2.5] = "Two and a Half"
print(myDict)

#Add a new item
myDict["New Item"] = "I'm New"
print(myDict)

#Remove Items
del myDict["One"]
print(myDict)
    
