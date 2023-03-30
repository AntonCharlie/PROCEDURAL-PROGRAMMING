#uri online, hackerrank, tlx toki

import os
import time

def cetak_pilihan():
	print("Pilihan : ")
	print("cr - konversi dari Celcius ke Reamur")
	print("cf - konversi dari Celcius ke Fahrenheit")
	print("ck - konversi dari Celcius ke Kelvin")
	print("rc - konversi dari Reamur ke Celcius")
	print("rf - konversi dari Reamur ke Fahrenheit")
	print("rk - konversi dari Reamur ke Kelvin")
	print("fc - konversi dari Fahrenheit ke Celcius")
	print("fr - konversi dari Fahrenheit ke Reamur")
	print("fk - konversi dari Fahrenheit ke Kelvin")
	print("kc - konversi dari Kelvin ke Celcius")
	print("kr - konversi dari Kelvin ke Reamur")
	print("kf - konversi dari Kelvin ke Fahrenheit")
	print("q - keluar dari program")


def celcius_ke_reamur(suhu_cr):
	return (4.0 /5.0) * suhu_cr

def celcius_ke_fahrenheit(suhu_cf):
	return ((9.0 / 5.0) * suhu_cf) + 32

def celcius_ke_kelvin(suhu_ck):
 	return suhu_ck + 273

def reamur_ke_celcius(suhu_rc):
	return (5.0 / 4.0) * suhu_rc

def reamur_ke_fahrenheit(suhu_rf):
	return ((9.0 / 4.0) * suhu_rf) + 32

def reamur_ke_kelvin(suhu_rk):
	return ((5.0 / 4.0) * suhu_rk) + 273

def fahrenheit_ke_celcius(suhu_fc):
	return (suhu_fc - 32) * (5.0 / 9.0)

def fahrenheit_ke_reamur(suhu_fr):
	return (4.0 / 9.0) * (suhu_fr - 32)

def fahrenheit_ke_kelvin(suhu_fk):
	return ((5.0 / 9.0) * (suhu_fk - 32)) + 273

def kelvin_ke_celcius(suhu_kc):
	return (suhu_kc - 273)

def kelvin_ke_reamur(suhu_kr):
	return (4.0 / 5.0) * (suhu_kr - 273)

def kelvin_ke_fahrenheit(suhu_kf):
	return ((9.0 / 5.0) * (suhu_kf - 273)) + 32


running = True
pilihan = None
while running:
	os.system("cls")
	cetak_pilihan()
	pilihan = input("Pilihan : ")

	
	if pilihan == "cr":
		main_cr = float(input("Suhu Celcius-nya : "))
		result = celcius_ke_reamur(main_cr)
		print(f"Reamur : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "cf":
		main_cf = float(input("Suhu Celcius-nya : "))
		result = celcius_ke_fahrenheit(main_cf)
		print(f"Fahrenheit : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "ck":
		main_ck = float(input("Suhu Celcius-nya : "))
		result = celcius_ke_kelvin(main_ck)
		print(f"Kelvin : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "rc":
		main_rc = float(input("Suhu Reamur-nya : "))
		result = reamur_ke_celcius(main_rc)
		print(f"Celcius : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "rf":
		main_rf = float(input("Suhu Reamur-nya : "))
		result = reamur_ke_fahrenheit(main_rf)
		print(f"Fahrenheit : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "rk":
		main_rk = float(input("Suhu Reamur-nya : "))
		result = reamur_ke_kelvin(main_rk)
		print(f"Kelvin : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "fc":
		main_fc = float(input("Suhu Fahrenheit-nya : "))
		result = fahrenheit_ke_celcius(main_fc)
		print(f"Celcius : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "fr":
		main_fr = float(input("Suhu Fahrenheit-nya : "))
		result = fahrenheit_ke_reamur(main_fr)
		print(f"Fahrenheit : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "fk":
		main_fk = float(input("Suhu Fahrenheit-nya : "))
		result = fahrenheit_ke_kelvin(main_fk)
		print(f"Fahrenheit : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "kc":
		main_kc = float(input("Suhu Kelvin-nya : "))
		result = kelvin_ke_celcius(main_kc)
		print(f"Kelvin : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "kr":
		main_kr = float(input("Suhu Kelvin-nya : "))
		result = kelvin_ke_reamur(main_kr)
		print(f"Kelvin : {result}")
		input("Tekan Enter untuk ke Menu Utama")

	elif pilihan == "kf":
		main_kf = float(input("Suhu Kelvin-nya : "))
		result = kelvin_ke_fahrenheit(main_kf)
		print(f"Kelvin : {result}")
		input("Tekan Enter untuk ke menu Utama")

	elif pilihan == "q":
		running = False
		print("Bye bye, [Keluar dalam 1 detik]")
		time.sleep(1)
 