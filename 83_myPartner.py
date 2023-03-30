name = input()
my_number = 0

for character in name.upper():
	my_number += ord(character)

print(f"inisial jodoh kamu adalah {chr(my_number%26+ord('A'))}")