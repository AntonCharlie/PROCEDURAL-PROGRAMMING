
available_toppings = ['mushroom', 'cheese', 'pineapple', 'pepperoni']

requested_toppings = []

stop = False

while not stop:
	topping = input("Input your topping here ('q' to quit: )")
	if topping != 'q':
		requested_toppings.append(topping)
	else:
		stop = True


for requested_toppings in requested_toppings:
	if requested_toppings in available_toppings:
		print(f"Adding {requested_toppings}.")
	else:
		print(f"Sorry, we don't have {requested_toppings}")

print(f"\nFinished making your pizza...")
