

daftarAngka = [7, 8, 3, 9, 0, 3, 5, 10, 2, 7]
daftarAngka.sort()

prev = None
for angka in daftarAngka:
    if angka == prev:
        print(f"Angka {angka} duplikat!")
    prev = angka