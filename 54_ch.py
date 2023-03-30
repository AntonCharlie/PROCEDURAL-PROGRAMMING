"""
1. Buat 3 dict yg menampilkan org berbeda (ob. person) kemudian simpan ketiganya di dalam sebuah list (ls. people). Untuk data setiap org memiliki key yang sama namun value boleh berbeda. Banyak key menimal 2. Cetak semua org yang ada di dalam list people tanpa terlihat list dan dictionarynya dengan cara kamu masing-masing. (ref 47_aliens)

2. Buat dictionary dengan nama cities. Gunakan nama kota sebagai key di dalam duct. tersebut. kemudian buatkan dict untuk setiap kota (min 2 kota) agar dapat menyimpan informasi seperti landmark dan fun fact kota tersebut. Cetak semua kota beserta info tanpa terlihat dictionarynya. (ref 52_many_users)

3. buat dictionary dengan nama obat-obatan. Gunakan nama obat sebagai key di dalam dictionarynya. Kemudian buat juga dictionary di setiap obat (min2 obat) untuk menyimpan informasi terkait kegunaan, harga, dan efek samping. Untuk info efek samping simpan minimal 2 informasi terkait kegunaan, harga, dan efek samping. Untuk info efek samping simpan minimal 2 informasi yang tergabung di dalam sebuah list. cetak semua informasi tentang obat tanpa terlihat dictionary dan listnya. (ref 53_many_pizzas)
"""

# 1
person_1 = {'body':'tinggi', 'points':10}
person_2 = {'body':'gemuk', 'points':30}
person_3 = {'body':'pendek', 'points':70}

people = [person_1, person_2, person_3]

for person in people:
	print(person)



# 2
cities = { 
	'Palembang' : {
		'pemerintahan' : 'Sumatera Selatan',
		'tempat' : "Jembatan Ampera"	
	},
	'Jakarta' : {
		'pemerintahan' : "DKI Jakarta",
		'tempat' : "Monas"
	}
}


for cityname, city_info in cities.items():
	print(f"\nKota : {cityname}")
	prop = city_info['pemerintahan']
	bangunan = city_info['tempat'].title()
	print(f"\tProvinsi : {prop}")
	print(f"\tLandmark : {bangunan}")


# 3
obat_obatan = {
	"tempra" : {
		"kegunaan" : ["mengatasi demam", "mengurangi sakit kepala"],
		"price" : 45_000
	},
	"wood's" : {
		"kegunaan" : ["meredakan batuk", "menghangatkan tenggorokan"],
		"price" : 20_000
	}
}

for obat, obat_info in obat_obatan.items():

	print(f"\n{obat.title()}")

	for data, isi in obat_info.items():

		print(f"\t{data}")
		if type(isi) == list:
			for item in isi:
				print(f"\t\t- {item}")

		else:
			print(f"\t\t{isi}")

	print() 



'''
A week ago, I read an article about an upcoming film. The film will be released on seventeenth of December, 2021. This film is about someone who wants to keep his identity and asks for help from a scientist to erase the memories of people around the world about who he is. This film is in the news because it was one of the best films in the previous episode. This movie is titled Spiderman No Way Home. I think this movie will be very interesting because the actor of Spiderman, namely Tom Holland is one of the actors i like the most, and his film is extremely incredible. 
'''
	







