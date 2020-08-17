#else-if
n=int(input("Enter Your Marks:"))
if (n>80 and n<=100):
	print("Distinction")
elif n>70 and n<=80 :
	print("A Grade")
elif n>50 and n<=70 :
	print("B Grade")
else :
	print("Fail")
