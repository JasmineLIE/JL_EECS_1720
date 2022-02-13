#While Loop -- Repeatedly execute instructions inside the loop while a certain conditions remains valid
'''
The structure of  awhile statement is as follows:

While condition is true:
    do A

Most of the time when using a while loop, need to first declare a variable to function as a loop counter
The condition in the while statement will evaluate the value of counter to determine if it smaller (or greater) than a certain value
If it is, the loop will be executed, let's look at a sample program

'''

counter = 5

while counter > 0:
    print ("Counter = ", counter)
    counter = counter - 1
    

#Break -- When working with loops, sometimes you may want to exit the entire loop when certain condition is met.  To do that, use break keyword

    j = 0

    for i in range(5):
        j = j + 2
        print ('i = ', i, ', k = ', j)
        if j == 6:
            break;

#Without break keyword, the program should loop from i = 0 to i = 4 because we used function range(5)

#Continue -- Keyword, the rest of the loop after the keyword is skipped for the iteration.  E.x:

j = 0
for i in range(5):
    j = j + 2
    print ('\ni = ', i, ', j = ', j)
    if j == 6:
        continue
    print ('I will be skipped over if j=6')
