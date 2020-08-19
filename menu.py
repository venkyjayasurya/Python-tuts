x= int(input("Enter 1st Number:"))
y= int(input("Enter 2nd Number:"))
while 1 :
	ch= int(input("1. Add\n2. Sub\n3. Mult\n4. Div\n5. Exit\nEnter the Choice: "))
	if( ch==1):
		c=x+y
		print(" Add is :",c)
	elif( ch==2):
		c=x-y
		print(" Sub is :",c)
	elif( ch==3):
		c=x*y
		print(" Mult is :",c)
	elif( ch==4):
		c=x/y
		print(" Division is :",c)
	elif( ch==5):
		exit(0)
	else:
		print("Enter Correct Choice")