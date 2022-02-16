#Read a file by buffer size so our program does not use too many memory resources

inputFile = open('C:\\Users\hwafu\OneDrive\Documents\GitHub\JL_EECS_1720\Practice Work\Python\Beginner Python Work\In VSCode\OpeningAndReadingTextFiles/myfile.txt', 'r')

outputFile = open('myoutputfile.txt', 'w')

msg = inputFile.read(10)

while len(msg):
    outputFile.write(msg + '\n')
    (msg) = inputFile.read(10) #this and the while loop loops through 10 bytes at a time - the value 10 in the () tells the read() function to read only 10 bytes.  The while condition while lens(msg): checks the length of the variable msh.  So long as the length is not zero, the loop will run
'''
Within the while loop, the statement outputFile.write(msg) writes the message to the output file
After writing the message, the statement msg = inputFile.read(10) reads the next 10 bytes and keeps doing it until the entire file is read
When that happens, the program closes both files

When you run the program, a new myoutputfile.txt will be created.  When you open the file, you'll notice that it has the same content as your input file myfile.txt
To prove that it reads only 10 bytes at a time, you can change the line outputFile.write(msg) in the program to outputFile.write(msg + '\n')
Now run the program again -- myoutputfile.txt now contains lines with at most 10 characters
'''
inputFile.close()
outputFile.close()

#inputFile.txt and outputFile.txt opened for reading and writing
