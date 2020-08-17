def fact(n):
	if n==1 :
		return 1
	else :
		return( n * fact(n-1))
x=int(input("Enter a Number"))
y=fact(x)
print("The Factorial is %d",y)

