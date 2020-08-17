'''python strings are immutable which means that once created they cannot be changed.
Whenever you try to modify an existing string variable a new string is created'''


str1="Hello !"
print("String 1 is ",str1)			#Hello!
print("ID of string 1 is", id(str1)) 		#address of str1

str2="World"
print("string 2 is", str2)			#world
print("ID of string 2 is ", id(str2))		#address of str2

str1=str1+str2
print("string 1 after concatenation is", str1)	#string 1 after concatenation is Hello!World
print("ID of string 1 is ",id(str1))		#address of str1

str3=str1
print("string 3 is", str3)			#Hello!world
print("ID of strig 3 is ", id(str3))		#address of str3

str3="Python"
print(str3)					#python
print("Id of string 3 is", id(str3))		#address of str3
