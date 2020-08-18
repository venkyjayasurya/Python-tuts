def local():
	global c	#c value cannot be assigned here itself
	c=30
	a=10	#local variable a
	b=20	#local variable b
	print(a)
	print(b)
	print(c)
local()
a=15 #global variable a
b=25 #global variable b
print(a)
print(b)
print(c)