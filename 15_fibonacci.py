#a = 0
#b = 1
#count = 0
#max_count = 20


#while count < max_count:
#	count += 1
#	print(a, end=" ")
#	old_a = a
#	a = b
#	b = old_a + b
	
#print()
#buat baris bilangan baru

a = 0
b = 2
count = 0
max_count = 10

while count < max_count:
	count += 1
	print(b, end=" ")
	old_b = b
	new_b = old_b + b
	print(new_b)