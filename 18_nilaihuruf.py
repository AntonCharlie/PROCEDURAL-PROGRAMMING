"""

Guru akan memberikan nilai huruf ke siswa
dengan aturan sebagai berikut
A >= 90
B >= 75
C >= 65
D >= 50
F


"""

nilaiSiswa = float(input("Berapa nilainya: "))
#bottom to top
if nilaiSiswa < 50:
	print("nilai huruf = F")
elif nilaiSiswa < 65:
	print("nilai huruf = D")
elif nilaiSiswa < 75:
	print("nilai huruf = C")
elif nilaiSiswa < 90:
	print("nilai huruf = B")
else:
	print("nilai huruf = A")



#top to bottom
if nilaiSiswa >= 90:
	print("nilai huruf = A")
elif nilaiSiswa >= 75:
	print("nilai huruf = B")
elif nilaiSiswa >= 65:
	print("nilai huruf = C")
elif nilaiSiswa >= 50:
	print("nilai huruf = D")
else:
	print("nilai huruf = F")
	
