def add(a,b):
	c=a+b
	print(" Add is :",c)
def sub(a,b):
	c=a-b
	print(" Sub is :",c)
def mult(a,b):
	c=a*b
	print(" Mult is :",c)
def div(a,b):
	c=a/b
	print(" Division is :",c)

x= int(input("Enter 1st Number:"))
y= int(input("Enter 2nd Number:"))
while 1 :
	ch= int(input("1. Add\n2. Sub\n3. Mult\n4. Div\n5. Exit\nEnter the Choice: "))
	if( ch==1):
		add(x,y)		
	elif( ch==2):
		sub(x,y)		
	elif( ch==3):
		mult(x,y)		
	elif( ch==4):
		div(x,y)		
	elif( ch==5):
		exit(0)
	else:
		print("Enter Correct Choice")