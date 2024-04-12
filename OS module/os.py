import os

os.getcwd() # current working directory

f = open("Practice.txt","w+") # here we open a textfile 
f.write("This is a test string") # text writing in the files.
f.close() # here we close the file.

print(os.listdir()) # to know files in my cd


import send2trash


send2trash.send2trash()