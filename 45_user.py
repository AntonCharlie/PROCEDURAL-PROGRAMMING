

user_0 = {
	'username' : 'oke123',
	'first' : 'Budi',
	'last' : 'Santoso'
}

for item in user_0:
	print("key:", item)
	print("val:", user_0[item])

print(user_0.items())


for key, val in user_0.items():
	print("key:", key)
	print("val:", val)

#baris 9-13 sama dengan 16-18


for key in user_0.keys():
	print("key:", key)

for val in user_0.values():
	print("val:", val)
