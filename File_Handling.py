file_pointer = open("Readme.txt","r")
contents_we_read = file_pointer.read()
print(contents_we_read)
file_pointer.close() #If you open a file don't forget to close it.

#Read the amount of number you want
file_pointer1 = open("Readme.txt","r")
contents_we_read1 = file_pointer1.read(6)  #<here i mention 6 so it will read 6 chr only
print(contents_we_read1)
file_pointer1.close()

#Read line one by one readline() and readlines() are two different functions
file_pointer2 = open("Readme.txt","r")
print(file_pointer2.readline(),end="")
print(file_pointer2.readline())
file_pointer2.close()

#Append mode working
#Writing on the text file
file_pointer = open("Readme.txt","w") #File na ho to yay bana dy ga
file_pointer.write("Hammad is a good boy this is the line I am writing using write function")
file_pointer.close()

#File main append kysy karna hay
file_pointer22 = open("Readme.txt","a")  #data replace nai kary ga purany main new append kar dy ga
file_pointer22.writelines("Hammad is a good boy this is the line I am writing using write function")
file_pointer22.close()

#Do both read and write
file_pointer25 = open("Readme.txt","r+")  #data replace nai kary ga purany main new append kar dy ga
print(file_pointer25.read())
file_pointer25.write("This is new line with r+")
file_pointer25.close()