myName = input("Please enter your name: ")
myAge = input("What about your age: ")

print ("Hello World, my name is", myName, "and I am", myAge, "years old.")

print ("Hello World, my name is %s and I am %s year old." %(myName, myAge))

print ("Hello World, my name is {} and I am {} years old".format(myName, myAge))

#Different ways to print()

#If you need to display a long message, you can use triple-quote symbol to span message over multiple lines

print('''Hello World
My name is James and
I am 20 years old.''')

#Sometimes we might need to print some special unprintable characters such as a tab/newline
#In this case, need to use \ (backslash) character to escape character that otherwise have a different meaning


#For instance to print a tab, we type the backslash character before
#the letter t, like this: \t. Without the \ character, the letter t will be
#printed. With it, a tab is printed. Hence, if you type print
#(‘Hello\tWorld’), you’ll get Hello World

#Other common uses of the backslash character are shown below.
#>>> shows the command and the following lines show the output.

#\n (Prints a newline)

print ('Hello\nWorld')

#\\ Prints the backslash character itself
print ('\\')

#\" prints double quote so that the dobule quote does not signal the end of the string

print ("I am 5'9\" tall")

#\' Print single quote, so that the single quote does not signal the end of the string

print ('I am 5\'9" tall')

'''
If you do not want characters preceded by the \ character to be
interpreted as special characters, you can use raw strings by adding
an r before the first quote. For instance, if you do not want \t to be
interpreted as a tab, you should type print (r‘Hello\tWorld’).
You will get Hello\tWorld as the output.
'''
