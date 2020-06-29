#1python program to calculate length of a string
s=input("enter a string:")
print("the length of a enterd string is :",len(s))

#2python program to count the number of characters in a string
def char_frequency( str1):
	dict = { }
	for n in str1:
		keys=dict.keys( )
		if n in keys:
			dict[ n ] += 1
		else:
			dict[  n] = 1
	return dict
print(char_frequency('GITAM'))

#3python program to remove a new line character
str="GITAM UNIVERSITY\n"
print(str)
print(str.rstrip())

#4python program to occurance of substring in a string
str="Hari went to college at mornning and Hari came back from college at evenong"
print(str)
print(str.count(college))


#5write a program to find the length of a string"refrigerator" with out using len function
a="refrigerator"
count=0
for i in a:
	count=count+1
	print(count)

	
#6python program to convert a string in a list
string="Bangalore is a beautiful city"
print(string)
print("string converted to list",string.split())
#python program to perform deletion of a character

a=input("Enter a string:")
b=input("Enter a character to delete:")
c=""
for i in a:
if i==b:
continue
else:
c=c+i
print("After deleting a charcter:",c)

#7:Write a python program to print every character entered by user in a newline using loop
a=input("enter a string")
for i in a:
	print(i)
	
#8:Write a python program to get a single string from given two strings,seperated by a space and swap the first two characters of
string
In [9]:
a1=input("Enter first string:")
a2=input("Enter second string:")
l1=len(a1)
l2=len(a2)
b1=a2[0:2]+a1[2:l1]
b2=a1[0:2]+a2[2:l2]
c=b1+' '+b2
print(c)

#9.Write a python program to take input from user and print the input in both upper case and lower case
a=input("Enter a string")
print("Entered string in upper case:",a.upper())
print("Entered string in lower case:",a.lower())

		
