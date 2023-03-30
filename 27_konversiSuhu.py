
def cetak_pilihan():
	print("Pilihan : ")
	print("c - konversi dari Celcius")
	print("f - konversi dari Fahrenheit")
	print("q - keluar dari program")

def celcius_ke_fahrenheit(suhu_c):
	return 9.0 / 5.0 * suhu_c + 32

def fahrenheit_ke_celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0

pilihan = None

while pilihan != "q":

	cetak_pilihan()
	pilihan = input("Pilihan : ")

	if pilihan == "c":
		main_c = float(input("Suhu Celcius-nya : "))
		result = celcius_ke_fahrenheit(main_c)
		print(result)
	elif pilihan == "f":
		main_f = float(input("Suhu Fahrenheit-nya : "))
		print(f"Celcius : {fahrenheit_ke_celcius(main_f)}")
