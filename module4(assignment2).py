#1.Write a Python program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
    
#2.python program to remove consecitue duplicate form list.

x = [1,2,4,7,3,7,8,4,4,9]

previous_value = None
new_lst = [ ]

for elem in x:
   if elem != previous_value:
       new_lst.append(elem)
       previous_value = elem

print(new_lst)    

#3.python program to find unique element from a list.
def unique(a):
	uniquevalues =[ ]
	for i in a:
		if i not in uniquevalues:
			uniquevalues.append(i)
			for i in uniquevalues:
				print(i)
				
a=list()
n=int(input("Enter the size of the List ::"))
print("Enter the Element of List ::")
 for i in range(int(n)):
       k=int(input(" "))
      a.append(k)
      
print("the unique value from the  list is :"  ")
unique(a)

#4.python program to check whether a number is in given range.

def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)

#5.write a python program that accept a string and calcluate the number of uppercase and lowercase letter.

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The Ball bounse it Back')


	

  
	
	