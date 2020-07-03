#  1. Write a python program to create a tuple...

x = ()      # create an empty tuple
print(x)
tupleb = tuple()      # create an empty tuple with tuple() function built-in python.
print(tupleb)



#  2.Write a python program to create a tuple with different data types...

# Type-1 :

tupleb = ("tuple",True,10.0,5)
print(tupleb)


# Type-2 :
	
 # an empty tuple :

t = ( )  
print(t)

# tuple with items :

tuple = ('python' , 'tuple')       
print(tuple)

# concatenating 2 tuples :
	
tuple1 = (0,1,2,3)
tuple2 = ('python','program')
print(tuple1 + tuple2)

# nested tuples :
	
tuple1 = (0,1,2,3)
tuple2 = ('python','program')
tuple3 = (tuple1,tuple2)
print(tuple3)

#  tuple repitition :
	
tuple1 = ('python',)*3
print(tuple1)

# tuples are immutable :
	
tuple1 = (0,1,2,3)
print(tuple1)

# length of a tuple :
	
tuple1 = ('python','program')
print(len(tuple1))



#  3.Write a python program to convert tuple to a string...

tuple = ('p','y','t','h','o','n')
str = ''.join(tuple)
print(str)



# 4.Write a python program to slice a tuple...

tuples = (1,2,3,4,5,6,7,8,9)
slice = tuples[3:5]
print(slice)

tuples = (1,2,3,4,5,6,7,8,9)
slice = tuples[:]
print(slice)

tuples = (1,2,3,4,5,6,7,8,9)
slice = tuples[-8:-4]
print(slice)



#  5. Write a python program to find the length of a tuple...

tuple1 = tuple("python")
print(tuple1)
print("The length of a tuple is : " ,len(tuple1))



# 6. Write a python program to convert tuple to a dictionary...

tuplex = ((2,"b"),(3,"s"))
print(dict((y,x) for x , y in tuplex))



# 7.Write a python program to reverse a tuple...

x = ("python")
y = reversed(x)
print(tuple(y))



#  8. Write a python program to convert a list of tuples into a dictionary...

l = [("b",1) , ("s",2) , ("r",3)]
d = { }
for a , b in l :
	d.setdefault(a,[ ]).append(b)
print(d)


#  9. Write a python program to convert a list to a tuple...

# Type-1 :

listx = [1,2,3,4,5]
print(listx)
tuplex = tuple(listx)
print(tuplex)

# Type-2 :

def convert(list) :
	return tuple(list)
list = [1,2,3]
print(convert(list))