#Condition Statements

#Similar syntax to JS

'''
Not equals:
5 != 2
Greater than:
5>2
Smaller than:
2<5
Greater than or equals to:
5>=2
5>=5
Smaller than or equals to:
2 <= 5
2 <= 2
'''

#The difference is that the logical operators-- and, or, not-- are in English rather than symbols

# 5 > 2 or 7 >10 or 3 == 2 -- type these into the console; this will return true because the first condition is true

#The not operator returns True if the condition after the not keyword is false, else it will return False
#i.e: 'not 2>5 will return True since 2 is not greater than 5

#If statements

'''
Structure FOllows:

If condition 1 is met:
    do A
elif condition 2 is met:
    do B
else:
    do E
'''

#Anything indented is treated as a block of code that will be executed if the condition evaluates to true

userInput = input('Enter 1 or 2: ')

if userInput == "1":
    print ("Hello World!")
    print ("How are you?")
elif userInput == "2":
    print ("Python Rocks!")
    print ("I love Python")
else:
    print ("You did not enter a valid number")

#Inline If -- statement similar to if statement but more conveninent if you need to perform simple tax (like switch statement?)

num1 = 12 if myInt==10 else 13


#the statement assigns 12 to num1 (Task a) if myInt == 10.  Else it assigns 13 to num1 (task B)

print ("This is task A" if myInt == 10 else "This is task B")
