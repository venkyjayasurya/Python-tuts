n=int(input("Enter a Number?"))
k=n
s=0
while n>0:
	r=int(n%10)
	s=int(s*10 + r)
	n=int(n/10)
print("Reverse of %d is %d"%(k,s))
