# path="C:\\Users\\python_Workspace\\unit-03\\abc.txt"
# file=open(path,'r')
# #for i in file:
# #   print(i)
# print(file.read())

# import os
# path=os.getcwd()+"\\unit-03\\"
# #getc            wd-working directory
# print(path)

'''
modes
r-read a file
w-open existing file write operation if file contain data it get overwrite
a-if file contain data than the data will be .cant read file
r+-read than write.pre data and override/overwrite
w+-raed than write.disadvantage pre existng data will be overwrite
a+-file can be read.data not override/overwrite
'''

# path="C:\\Users\\python_Workspace\\unit-03\\abc.txt"
# file=open(path,'a+')
# file.write("class")
# file.seek(0)            #moving pointer to starting
# print(file.read())
# #various Modes of opening a file

'''
r:Just to read a file, can not perform any other operations
w:open an exiting file for write operation.
  If the file already contains some data then it will be overwritten.
  you cannot read a file from the same file object.
w+:Read +w{functionalites}
a:open an exiting file for append operation.
   \It won't override exiting data.
a+:Read + Append + dont override
r+:To read and write data into the file.
   The previous data in the file will
   also be overridden.
   if file does not exist then it will not create a new file.

'''
import os
path=os.path.dirname(__file__)
print(path)
path =path+"/"
# file=open(path+"abc.txt",'w+')
# file.write("rahul rocks")
# file.seek(0)
# print(file.read())

# #a mode:can not read,write,does not override
# file=open(path+"abc.txt","a+")
# file.write("-10")
# file.seek(0)
# print(file.read())

#if file does not exist then new file will
#not be created in case of r+ mode(sol:w/w+ mode)
# file=open(path+"abcd.txt","r+")
#It will throw an Exception

#Renaming a file(case insentive)
import os
# os.rename(path+"ABC.txt", path+"abc123.txt")

#Deleting a file(case insenstive)
# os.remove(path+"ABC.txt")

file =open(path+'abc.txt','r+')
# print(file.read())

data=file.readlines()
# print(type(data))
count=0
for i in data:
      print(type(i))#string
      word=i.split()
      count+=1
      print(word)
print("Total lines in the paragraph",count)

