# Q1. Write a Python program to read first n line of a file?
import os
path=os.path.dirname(__file__)
# print(path)
path =path+"/"

# def firstLinesFromAFile(fiel,nlines):
#       data=file.readlines()
#       length=len(data)
#       print(str(data[:nlines:]))

# file=open(path+"abc.txt","r+")
# firstLinesFromAFile(file,3)

# Q2. Write a python program to read last n line of a file?
# def lastLinesFromAFile(fiel,nlines):
#       data=file.readlines()
#       length=len(data)
#       print(str(data[length-nlines::1]))

# file=open(path+"abc.txt","r+")
# lastLinesFromAFile(file,3)

# # Q3. Write a python program to find the longest word?
# def longestWordsInafile(file):
#       allwords=[]
#       data=file.readlines()
#       for i in data:
#             words=i.split()
#             allwords=allwords+words
#       maxlength=0 
#       for i in allwords:
#             if(len(i)>maxlength):
#                   maxlength=len(i)
#       for i in allwords:
#             if maxlength==len(i):
#                   print(i)

# # file=open(path+"abc.txt","r")
# # longestWordsInafile(file)

# #Q4 .WAP to handle file not found exception?
# def openAFile(path,str):
#       try:
#             file=open(path+str,"r")
#       except FileNotFoundError:
#             print("Exception is handled")
#             file=open(path+str,"w+")

#       return file
# print("=====================")
# file=openAFile(path,"abcd.txt")
# file.write("jdsjljldj")
# file.close()

#Q5. When to write try, except, else and finally,
#    Wap to explain your answer?


#Q6. WAP to find unique number of words in a file?
file=open(path+"abcd.txt","r+")
s=set()
paragraph=file.readlines()
for sentence in paragraph:
      words=sentence.split()
      for word in words:
            s.add(word)
print(s)


#Q7.WAP to handle a None type Exception handling in python!

#Q8.Write a python program to get the file size of a plain file.







