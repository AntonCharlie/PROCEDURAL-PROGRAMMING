#Try Except .... "Handling Error"

while True:
	a = input("a = ")
	b = input("b = ")

	try:
		res = int(a)/int(b)
	except ZeroDivisionError as err:
		print(f"You can't divide by zero.\nError:{err}")
	except ValueError:
		print("You must input integer number!")
	else:
		print(f"a : b = {res}")
	finally:
		print("Done!")
		
	quit = input("Quit (y/n) ?")
	if quit == "y":
		break

"""
notes:

while:
	pass
else:
	pass



for i in range():
	pass
else:
	pass
"""