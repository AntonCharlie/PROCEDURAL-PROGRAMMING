
favorite_languages = {
	'jen' : ['python', 'javascript'],
	'sarah' : ['c'],
	'edward' : ['go', 'typescript'],
	'billi' : ['python', 'haskel']
}

for name, languages in favorite_languages.items():
	print(f"{name.title()}'s favorite languges are :")

	for language in languages:
		print(f"\t{language.upper()}")
