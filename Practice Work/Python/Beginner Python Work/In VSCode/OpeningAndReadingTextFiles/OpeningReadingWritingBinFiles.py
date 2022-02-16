#Binary files refers to any file that contains non-text, like image/video files
#To work with ibnaru files, use 'rb' or 'wb' mode
#copy a jpeg into your desktop and rename it myImage.jpg, now edit the program above by changing the first two lines

inputFile = open ('myImage.jpg', 'rb')
outputFile = open('myOutputImage.jpg', 'wb')

msg = inputFile.read(10)

while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()