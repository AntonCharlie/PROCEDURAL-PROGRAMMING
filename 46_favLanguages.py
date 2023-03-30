
favorite_Languages = {
	'jen' : 'python', 
	'sarah' : 'c', 
	'edward' : 'ruby', 
	'alex' : 'lua', 
	'mike' : 'python'
}


print(list(favorite_Languages.keys()))
print(tuple(favorite_Languages.values()))



for name, lang in favorite_Languages.items():
	print(f"{name.title()}'s favorite language is {lang.title()}.")


for name in sorted(favorite_Languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")



#list bisa diubah (pop, insert, remove, dll)
#tuple tidak bisa diubah

#contoh tuple
'''
rgb_color = (255, 245, 267)
position = (100, 200)
sreen_size = (1200, 868)
'''
print("The following languages have been mentioned: ")
for lang in sorted(set(favorite_Languages.values())):
	print(lang)

# set fungsinya agar tidak ada yang duplicate, agar python cuma diprint 1 kali.