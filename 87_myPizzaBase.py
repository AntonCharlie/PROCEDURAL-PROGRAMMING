
# regular arg with keywords arbitrary arguments

def make_pizza(**dough):
	print(f"\n Making  pizza with the following toppings:")
	print(dough)

def make_premium_pizza(size, *toppings, **dough): 
	print(f"\n Making a {size}cm pizza with the following toppings:")
	if toppings: # len(toppings) > 0
		for topping in toppings:
			print(f"\t-{topping}")
	else:
		print("\t(No topping.)")
	if dough:
		print()
		for key, val in dough.items():
			print(key,val)

make_pizza(thickness="thick")
make_pizza(thickness="thin", size=20)
make_pizza()

make_premium_pizza(12, "cheese", "peperoni", thickness="thick", crust=True)