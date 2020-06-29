#convert binary to decimal

b=list(input("enter a binary number :"))
value =0
for i in range(len(b)):
	digit=b.pop( )
	if  digit == '1':
		value = value + pow(2,i)
print("Decimal  value of the number is ",value)

#Generate first N Numbers of fibonacci series.Take N value from user

n=int(input("Enter the value :"))
n1 , n2 = 0 , 1
count=0
if n <= 0:
	print("please enter a positive number")
elif n == 1 :
	print("fibinocci sequence up to",n," :")
	print(n1)
else:
	print("fibonacci sequence")
	while count < n:
		print(n1)
		nth=n1 + n2
		n1=n2
		n2 =nth
		count +=  1
		
#Display multiplication table of k.take k value from user.
		
n=int(input(" ente a k value :"))
print("Multiplication table of k")
for i in range(1 ,11):
	print(n,"x",i,"=",n*i)	
	
#write a program to find a highest common factor
def compute_hcf(x , y) :
					while( y):
						x , y = y ,   x % y
						return x
hcf=compute_hcf( 300 , 400)
print("the hcf is",hcf)

#write a python program that accepts a word from the user & reverse.
def revstring( ):
	s=int(input("Enter a word:"))
	str=" "
	for i in s :
		str=i+str
		print("original word:",s)
		print("Reversed word :",str)
revstring( )

#python program to count of even and odd in a given sequense of numbers
list =[ 2 , 9 , 8 , 5 ,12 , 17]
even_count , odd_count = 0 , 0
for num in list :
					if num % 2 == 0 :
						even_count += 1
					else:
						odd_count  +=  1
print("even number in the list:",even_count)
print("odd number in the list",odd_count)

#python program to print all the number from 0 to 6 except 3 and 6
for x in range(6):
					if(x == 3 and x == 6):
						continue
						print(x,end="  ")
print("\n"")

#Take 10 integers from keyboard using loop and print their average value on the screen .print the fallowing pattern
*
**
***
****
def pypart(n): 

    myList = [] 

    for i in range(1,n+1): 

        myList.append("*"*i) 

    print("\n".join(myList)) 

n = 5
pypart(n) 


						
					
					
							

	
	