import re
str="She sells sea shells on the sea shore"
pattern1="sells"
if re.match(pattern1,str):	#retunrs true or false
	print("Match Found")
else:
	print(pattern1," is not present in ",str)
pattern2="she"
if re.match(pattern2,str,re.I):		#here re.I used to ignore the case sensitivity of the pattern2
	print("Match Found")
else:
	print(pattern2," is not present in ",str)

if re.search(pattern1,str):
	print("Match Found")
else:
	print(pattern1," is not found in ",str)

pattern3="sea"
print(re.findall(pattern3,str))
print(re.split(pattern3,str))
print(re.sub(pattern3,"ocean",str,1))