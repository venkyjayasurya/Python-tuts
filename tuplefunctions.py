tatacars=(("Nexon","Harrier","Tiago","Nexon"))
mycar=input("Enter Your Car Model:")

#we can delete the tuple but we cant modify it

#index() searches the tuple for a specified value and returns the
#position of where it was found
print(tatacars.index(mycar))

#count() returns the number of times a specified value occurs in a tuple
print(tatacars.count(mycar))

print(tatacars)

for x in tatacars:
	print(x)

del tatacars
print(tatacars)