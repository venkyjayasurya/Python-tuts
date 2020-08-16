#Menu_Area
from AreaPackage import Area
while(1):
	print("1.Triangle\n2.Parallelogram\n3.Rhombus\n4.Rectangle\n5.Square\n6.Trapezoid\n7.Circle\n8.Exit")
	ch=int(input("Enter Ur Choie:"))
	if ch==1:
		Area.Triangle()
	elif ch==2:
		Area.Parallelogram()
	elif ch==3:
		Area.Rhombus()
	elif ch==4:
		Area.Rectangle()
	elif ch==5:
		Area.Square()
	elif ch==6:
		Area.Trapezoid()
	elif ch==7:
		Area.Circle()
	elif ch==8:
		exit(0)
	else:
		print("Enter Right Choice")
