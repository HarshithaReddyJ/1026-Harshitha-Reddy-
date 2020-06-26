#write a python function to find max of 3 numbers
def  maxofthree() :
	a=int(input("Enter a value of a :"))
	b=int(input("Enter a value of b :"))
	c=int(input("Enter a value of c:"))
	if a > b and  a > c:
		print("a is greater")
	elif  b > a and b > c :
		print("b is greater")
	else:
		print("c is greater")
maxofthree( )

#write a python program to reverse a string
def revstring( ) :
	s=input("Enter a string: ")
	str= "   "
	for i in s:
		str=i + str
		print("original string :",s)
		print("reversed string :",str)
revstring( )

#write a python function to check whethere a number is prime or not
def prime():
	n=int(input("Enter a number to check prime ot not:"))

	i=2

	count=0

	while i<=n//2:

	        if n%i==0:

	                count+=1

	        i+=1
	if count>0:

	     print("Entered number is not a prime number")

   else:

         print("Entered number is prime number")
prime( )

#Use try,except,else and finally block to check weather a number is palindrome or not
import sys
try:
	n=int(input("Enter a number: "))
except valueError:
	print("oops!",sys.exc_info( ) [ 0] ,"occured")
else :
	rev=0
	temp=n
	print("Enter number:", n)
	while n!=0:
		rev=(rev*10)+(n%10)
		n//=10
		print("reversed number:",rev)
		if temp == rev :
			print("Entered number is palindrome")
		else:
			print("Entered number is not a palindrome")
			
#5:Write a python function to find the sum of squares of first n natural numbers
def sumofsquares( ):
			n=int(input("enter a number:" ))
			i=1
			sum=0
			while i<=n:
				sum=sum+(i**2)
				i+=1
			print("sum of square of",n,"narural numbers:" ,sum)
sumofsquares( )
			
			
	
	
	
	

		
	