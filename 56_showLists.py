#aList = [1, 2, 3 ,4, 5]

aList = [
	[1, 2, 3, 4, 5],  # [0][0], [0][1], [0][2], ....
	[6, 7, 8, 9, 10],
	[11, 12, 13, 14, 15],
	[16, 17, 18, 19, 20]  # ..... [4][4]
]

'''
for item in aList:
	print(item, end=" ")
print()
'''

for row in aList:
	for col in row:
		print(col, end=" ")
	print()
#col = kolom