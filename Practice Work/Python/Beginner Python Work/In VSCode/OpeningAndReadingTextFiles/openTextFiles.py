f = open ('C:\\Users\hwafu\OneDrive\Documents\GitHub\JL_EECS_1720\Practice Work\Python\Beginner Python Work\In VSCode\OpeningAndReadingTextFiles\myfile.txt', 'r')

firstline = f.readline()
secondline = f.readline()
print (firstline)
print (secondline)

f.close()

#need an open() and close() at the beginning and end of the code
#open() function allows python to read whatever is indiciated as the parameters
#the first paramater is the path to the file, the second parameter is the mode
'''
open() modes:

'r' mode: For reading only

'w' mode: For writing only
If a specified file does not exist, it will be created
If the specified file exists, any data written in the file is automatically added to the end

'a' mode: For appending. 
If a specified file does not exist, it will be created
if the specified file exists, any data written to the file is automatically added to the end

'r+' mode: For both reading and writing

Each time the readline() functio is called, it reads a new line from the file
Since readline() is called twice, it reads the first two lines

readline() function adds the \n at the end of each line
If you do not want the extra line, you can print(firstline, end = '') -- this will remove the \n characters


'''