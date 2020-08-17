marks = int(input("Enter the Marks?"))
if marks > 85 and marks <=100:
	print("Congrats! You scored Grade A..")
elif marks > 60 and marks <85:
	print("Congrats! You scored Grade B..")
elif marks > 40 and marks <=60:
	print("You scored Grade C..")
else:
	print("Your Failed")
