#write a python program to find area of a circle using math function
import math
r=float(input("enter the radius of a circle :"))
area=math.pi*r*r
print("area of a circle is",area)

#write a python program to find area of a regular polygon using math function
import math
s=int(input("enter no. of sides:" ))
l=int(input("enter the length of each side:"))
area = s *( l ** 2)/( 4 * math.tan(math.pi * s))
print(" area of polygon of", s,"sides:", area)

#write a python program to find area of segment of a circle using math function
r=float(input("Enter the radius if a circle :"))
a=float(input("Enter the angle :"))
if a >= 360:
	print("angle is not possible")
else:
	area=(math.pi*(r**2))*(a/360)
	print("area of segment:",area)
	
#write a python program to shuffel a list
l1=[ 100, 1, 2 , 3, 40 ,"hai" , "hello"]

import random
list=[100,1,2,3,30,40,"hai","hello"]
random.shuffle(list)
print(list)	

#write a program to generate a random number b/w 1,10000 & diff b/w each random number is 50

import random
n=int(input("Enter no.of numbers to generate:"))
i=0
while i<n:
	print(random.randrange(1,10000,50))
	i+=1

#write a pytho program by using math modules
#a.sin 60
import math
print(math.sin(60))	

				
#b.cos(pi)
import math
print(math.cos(pi))

#c.tan 90
import math 
print(math.tan(90))

#d.angle of sin(0.8660254037844386)
import math
print(math.sin(0.8660254037844386))

#e.5^8
import math
print(math.pow(5,8))

#f.square root of 400
import math
print(math.sqrt(400))

#g.the value of 5^e
import math
print(math.pow(5,math.e))

#h.the value of log(1024),base 2
import math
print(math.log(1024,2))

#i.the value of log(1024),base 10
import math
print(math.log(1024,10))

#j.the flore and ceiling value of23.56
import math
print("print flore value of 23.56:",math.flore(23.56))
print("print ceiling value of 23.56:",math.ceiling(23.56))



