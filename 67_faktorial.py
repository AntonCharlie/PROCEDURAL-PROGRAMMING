"""
faktorial

4! = 4 x 3 x 2 x 1 = 24
   = 4 x 3!
   = 4 x 3 x 2!
   = 4 x 3 x 2 x 1!
   = 4 x 3 x 2 x 1

3! = 3 x 2 x 1 = 6
5! = 5 x 4 x 3 x 2 x 1 = 120

"""

def factorial(num):
	if num < 0:
		return "NOT DEFINED"
	if num == 1 or num == 0:
		return 1
	return num * factorial(num-1)

print(factorial(4))


