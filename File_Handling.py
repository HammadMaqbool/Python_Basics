file_pointer = open("Readme.txt","r")
contents_we_read = file_pointer.read()
print(contents_we_read)
file_pointer.close() #If you open a file don't forget to close it.

#Read the amount of number you want
file_pointer1 = open("Readme.txt","r")
contents_we_read1 = file_pointer1.read(6)  #<here i mention 6 so it will read 6 chr only
print(contents_we_read1)
file_pointer1.close()

#Read line one by one
file_pointer2 = open("Readme.txt","r")
print(file_pointer2.readline(),end="")
print(file_pointer2.readline())
file_pointer2.close()