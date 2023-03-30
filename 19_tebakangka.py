#import random
from random import randint
import os

os.system("cls")#untuk membersihkan yang di atas
angkaBenar = randint(0, 10)
angkaTebakan = None

while angkaTebakan != angkaBenar:
	angkaTebakan = int(input("Angka Tebakannya = "))

	if angkaTebakan == angkaBenar:
		print("Yeay Anda Benar!!")
	elif angkaTebakan > angkaBenar:
		print(f"Angkanya lebih kecil dari {angkaTebakan}")
	elif angkaTebakan < angkaBenar:
		print(f"Angkanya lebih besar dari {angkaTebakan}")
		#f harus diikuti {} -=> tdk ush pakai koma lagi, langsung lanjut.




		#buat program untuk ngecek apa bil. tersebut kelipatan 3