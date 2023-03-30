

cars = ["bmw", "audi", "toyota", "subaru"]

#Sorting
cars.sort() #permanen A - Z
print(cars)

cars.sort(reverse=True) #permanen Z - A
print(cars)

print(sorted(cars)) #Tidak mempengaruhi list utama


#Searching
item = "toyota"
index_item = cars.index(item)
print(index_item)

isExist = item in cars #True
print(isExist)

if item in cars:
	index = cars.index(item)
	print(index)
else:
	print("Not Exist")


#Number of item in list = len --> menhitung jumlah
full_name = "Charlie Antoni Yusup"
print(len(full_name))

print(len(cars))



