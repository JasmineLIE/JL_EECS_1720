#For Loop -- executes a block of code repeatedly until the condition in the for statement is no longer valid

#Looping through an interable -- an interable refers to anything that can be looped over

'''
The syntax:

for a in iterable:
    print (a)
'''

pets = ['cats', 'dogs', 'rabbits', 'hamsters']

for myPets in pets:
    print (myPets)

#Here, we have declared the list pets and gave it the members from the pets [] array
 #the statement myPets in pets: loops through the pets list and assigns each emmber in the list to the variable myPet

#Can also display the index of the members in the list
    #To do so, use enumerate() function

for index, myPets in enumerate(pets):
    print(index, myPets)


#the next exmaple shows how to loop through a string:

message = 'Hello'

for i in message:
    print (i)
    

#Prints every letter out one at a time
'''
H
E
L
L
O
'''

#Looping through a sequence of numbers
'''
range() function comes in handy -- generates list of numbers and has syntax range (start, end, step)

if the start is not given, the numbers generated will start from zero

When using format() method for strings, the position of parameters start form zero
When using range() function, if start is not given, the number genereated is zero

For instance

range(5) will generate list [0, 1, 2, 3, 4, 5]

Below should get
0
1
2
3
4

'''

for i in range(5):
    print (i)
