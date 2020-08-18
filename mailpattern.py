import re
emailp="^[a-z]+[0-9]*@[a-z]+.com"
email=input("Enter your Email id: ")
if re.match(emailp,email):
	print("Thank You :) ")
else:
	print("Invalid Email id")

mobilep="[0-9]{10}"
mobile=input("Enter YOur Mobile Number:")
if re.match(mobilep,mobile):
	print("Thank You :) ")
else:
	print("Invalid Mobile Number")

pattern="\w"
s=input("Enter a Line of Text")
if re.match(pattern,s):
	print("There are words")
else:
	print("No words")

m=re.match("ai","It is raining in Hyd")
print(m)