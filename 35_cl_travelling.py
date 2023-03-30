'''
1. Bayangkan kalian akan pergi ke 5 destinasi wisata

2. Buatkan list dari 5 tempat tersebut dan tidak perlu terutut secara alphabet

3. Cetak list yang original

4. Cetak list terurut tanpa mengubah list yang asli

5. Karena dana terbatas hapus 2 tujuan, yang pertama hapus item di index 3, yang kedua hapus item index terakhiir

6. Tiba-tiba ada sponsor yang mendanai pergi ke Paris, masukkan kota Paris sebagai tujuan pertama di list

7. Cetak list setelah diurutkan permanen dan secara descending (Z-A)

'''

tujuan = ['Malaysia', 'Australia', 'Thailand', 'Singapura', 'Filipina']
print(tujuan)

print(sorted(tujuan))

del tujuan[3]
del tujuan[-1]
print(tujuan)

tujuan.insert(0, 'Paris')
print(tujuan)

tujuan.sort(reverse=True)
print(tujuan)

