
error = False #flag = penanda = trigger

while not  error:
	print("we are playing now!")
	still_playing = input("Still Playing (Y/N) : ")
	if still_playing == "N":
		error = True