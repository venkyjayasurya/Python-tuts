name="Sachin"
age=45
print("Name : %s and age : %s"%(name,age))
print("Name : %s and age : %s"%("Anjali",50))

str="Hello"
#used to Capitalise first letter of a string
print(str.capitalize())
print(str.center(10,'*'))

str="he"
message="HelloworldHelloworldHello"
#counts number of times str occurs in message
print(message.count(str,0,len(message)))

message="He is my best friend"
#returns true if message ends with friend, false otherwise
print(message.endswith("friend",15,len(message)))

str="hell"
message="Helloworld"
#checks if world is present in message. If found returns the position of
#occurance ow returns -1
print(message.find("world",0,10))

#same as find but raises an exeption if not found
#print(message.index("she",0,10))

#same as find but starts searching from the end
print(message.rfind("world",0,10))

#same as index but starts searching from the end
#print(message.rindex("She",0,10))

message="12345ABC123abc	"
print(message.isalnum())
message="JamesBond"
print(message.isalpha())
message="007"
print(message.isdigit())
message="jamesbond"
print(message.islower())
message="JAMESBOND"
print(message.isupper())
message="  "
print(message.isspace())



message="James Bond 007"
print(message.isalnum())
print(message.isalpha())
print(message.isdigit())
print(message.islower())
print(message.isupper())
print(message.isspace())


#returns a string left justified with a totol equal to the value of 1st
#parameter and columns without characters are padded with the value of 2nd parameter
print(message.ljust(20,'*'))

#returns a string right justified with a total equal to the value of 1st
#parameter and columns without characters are padded with the calue of
#2nd parameter
print(message.rjust(20,'*')) #slice
print(message[0:10:2]) #slice and stride
print(message[::-1]) #reverse
