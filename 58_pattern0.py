'''

*
**
***
****

baris 1, bintang / kolom 1
baris 2, biintang 2
baris 3, bintang 3

row = n, bintang = n

baris 0, bintang 1, row = n, stars = n + 1 = row += 1
'''

rows = 5


for row in range(rows):
	for star in range(row+1):
		print("*", end=" ")

	print()