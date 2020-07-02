#1:Write a Python program to read an entire text file.
my_file=open('harshitha.txt "," r")
for line in my_file:
	print(line)
my_file.close( )

#2:Write a Python program to read first n lines of a file

my_file=open("hati1.txt","r")
n=int(input("Enter no.of lines to read:"))
i=0
for line in my_file:
    if i<n:
    	print(line)
         i+=1
    else:
    break
my_file.close()


#3:Write a Python program to append text to a file and display the text.
In [9]:
my_file=open("hari1.txt","a")
my_file.write("This is python assignment\n")
my_file1=open("hari1.txt","r")
for line in my_file1:
     print(line)
my_file.close()

#4:Write a Python program to read last n lines of a file.
	
my_file=open("hari2.txt","r")
n=int(input("Enter no.of lines to read:"))
for line in (my_file.readlines()[-n:]):
	print(lines)
my_file.close( )

#5:Write a Python program to read a file line by line store it into a variable.

my_file=open("hari2.txt","r")
a=" "
for line in my_file:
    a=a+line
print(a)
my_file.close( )

#6:Write a Python program to read a file line by line and store it into a list.

my_file=open("hari2.txt","r")
l=[ ]
for line in my_file:
     l.append(line)
print(l)
my_file.close()

#7:Write a Python program to read a file line by line store it into an array.

my_file=open("hari2.txt","r")
l=[]
for line in my_file:
l.append(line)
print(l)
my_file.close()

#8:Write a Python program to count the number of lines in a text file.
my_file=open("hari2.txt","r")
count=0
for line in my_file:
count+=1
print("No.of lines in saketh2.txt:",count)

#9:Write a Python program to get the file size of a plain file.
In [25]:
import os
size=os.path.getsize("hari2.txt")
print("Size of saketh2.txt:",size,"bytes")

#10:Write a Python program to copy the contents of a file to another file .
In [28]:
my_file1=open("hari2.txt","r")
my_file2=open("hari3.txt","w")
for line in my_file1:
       my_file2.write(line)
my_file3=open("hari3.txt","r")
for line in my_file3:
      print(line)
my_file1.close()
my_file2.close()
my_file3.close()

#11:Write a Python program to sum all the items in a list.
In [29]:
l=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in l:
sum+=i
print("Sum of elements of list:",sum)

#12:Write a Python program to multiplies all the items in a list.

l=[1,2,3,4,5,6,7,8,9,10]
mul=1
for i in l:
     mul*=i
print("Multiplication of elements of list:",mul)

#13:Write a Python program to get the largest & smallest number from a list

l=[1,2,3,4,5,6,7,8,9,10]
s=l[0]
h=l[0]
for i in l: 
      if s>i:
         s=i
      if h<i:
          h=i
print("Smallest value in list:",s)
print("largest value in list:",h)

#14:Write a Python program to remove duplicates from a list.
In [32]:
l1=[10,20,30,40,10,20,30,40]
l2=[]
for i in l1:
if i not in l2:
l2.append(i)
else:
continue
print("After removing duplicates:")
print("List:",l2)
#15:Write a Python program to check a list is empty or not.
In [33]:
l=[]
if len(l)==0:
       print("List is empty")
else:
       print("List is not empty")
       
#16:Write a Python program to clone or copy a list.
In [36]:
l1=[10,20,30,40]
l2=[]
for i in l1:
     l2.append(i)    
print(12)

#17:Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : ['Red', 'Green', 'White',
'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']
In [1]:
l1= ['Red','Green','White','Black','Pink','Yellow']
l2=[]
i=0
while i<len(l1): 
        if i==0 or i==4 or i==5:
                  i+=1
                  continue
        else:
              l2.append(l1[i])
                    i+=1
print("After removing 0th,4th and 5th positions:")
print("List" ,12)

#18:Write a Python program to print the numbers of a specified list after removing even numbers from it.

l1=[1,2,3,4,5,6,7,8,9,10]
l2=[]
for i in l1:
        if i%2==0:
             continue
        else:
              l2.append(i)
print("After removing even numbers from list:")
print("list",12)

#19:Write a Python program to shuffle and print a specified list.
In [3]:
from random import shuffle
l=[1,2,3,4,5,6,7,8,9,10]
shuffle(l)
print(l)

#20:Write a Python program to get the difference between the two lists.
l1=[10,20,30,40,50,60,70,80,90,100]
l2=[1,2,3,4,5,6,7,8,9,10]
l3=[]
if len(l1)==len(l2):
         i,j=0,0
         while i<len(l1) and j<len(l2):
                 l3.append(l1[i]-l2[j])
                  i+=1
                  j+=1
         print("Difference between two lists:",l3)
else:
        print("No.of elements are different.Not able to do difference")
        
        

 



	
	