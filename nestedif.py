a =int(input("Enter the 1st Number?"))
b =int(input("Enter the 2nd Number?"))
c =int(input("Enter the 3rd Number?"))
if a>b:
	if a>c:
		print("Bigger is", a)
	else:
		print("Bigger is", c)
else:
	if b>c:
		print("Bigger is", b)
	else:
		print("Bigger is", c)
