#1.     What is dictionary in Python? Explain with an example.

#  Ans- Dictionary in Python is an unordered collection of data values , used to store data values in key:value pairs(key/value pairs.)
#   Example :
# Creating a dictionary with Integer keys :::
Dict = {1:'Python' , 2:'program'}
print("\nDictionary with the use of Integer keys:")
print(Dict)
# Creating a dictionary with Mixed keys :::
Dict = {'Name' : 'Python' , 1 : [1,2,3,4,5]}
print("\nDictionary with the use of mixed keys :")
print(Dict)

#  2. Write a Python program to sum all the items in a list. 
total = 0
list1 = [10,20,30]
for ele in range(0,len(list1)) :
	total = total + list1[ele]
print("Sum of all the items in a list : ",total)

#   3. Write a Python program to create a list of empty dictionaries.
n = 5
b  = [{ } for _ in range(n)]
print(b)

#  4.  Write a Python program to access dictionary keys element by index. 
num = {'Python' : 1 , 'Programming' : 2 , 'Language' : 3 }
print(list(num)[0])

# 5.  Write a Python program to iterate over dictionaries using for loops.
d = {'Red' : 1 , 'Green' : 2 , 'Blue' : 3}
for color_key , value in d.items() :
	print(color_key , 'corresponds to' , d[color_key])
#  6.Write a Python program to sum all the items in a dictionary. 

my_dict = {'d1' : 150 , 'd2' : 25 , 'd3' : -25}
print(sum(my_dict.values()))

#  7.Write a Python script to concatenate following dictionaries to create a new one.       Sample Dictionary : 
#   a. dic1={1:10, 2:20} 
#   b. dic2={3:30, 4:40} 
#   c. dic3={5:50,6:60} 
#   Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 

dic1 = {1:10, 2:20} 
dic2 = {3:30, 4:40} 
dic3 = {5:50,6:60} 
dic4 = { }
for d in (dic1 , dic2 , dic3) : dic4.update(d)
print(dic4)