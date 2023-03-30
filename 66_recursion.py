
for number in range(1,11):
	print(number, end=" ")
print()
# 1, 2, 3, ..., 10

number = 1
while number < 11:
	print(number, end=" ")
	number += 1
print()
# 1, 2, 3, ..., 10

def counting(start, stop):
	if start < stop:
		print(start, end=" ")
		return counting(start+1, stop)
	print()

counting(1, 11)
# 1, 2, 3, ..., 10