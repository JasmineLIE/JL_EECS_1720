f = open ('C:\\Users\hwafu\OneDrive\Documents\GitHub\JL_EECS_1720\Practice Work\Python\Beginner Python Work\In VSCode\OpeningAndReadingTextFiles\myfile.txt', 'r')

for line in f:
    print (line, end = '')

f.close()