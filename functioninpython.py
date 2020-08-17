str1="Welcome to the World of Python"
str2="the"
# in and not in operators
if str2 in str1:
	print("Found")
else:
	print("Not Found")

if "Python" not in str1:
	print("Not Found")
else:
	print("Found")

#ASCII/UTF functions ord() and chr()
print(ord('a')) #ordinal
print(chr(97))

#convert to upper and lowercase
str3=str1.upper()
str4=str1.lower()
print(str3)
print(str4)

#split a string into words and return a list containing those words
str5=str1.split()
print(str5)

#join words in a string using a delimiter
city={"Hyderabad","Banglore","Mumbai","Kolkata","Chennai"}
str6=','.join(city)
print(str6)
print('-'.join(str5))

#count the occurance of a character or string
print(str6.count('a'))
print(str4.find("of"))

	