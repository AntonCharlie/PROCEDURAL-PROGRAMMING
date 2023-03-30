import random
import os

def setting_up_board(rows):
	board = []

	for row in range(rows):
		line = []
		for item in range(rows):
			line.append("O") # ["O", "O", "O", "O", "O"]
		board.append(line)

	return board

def setting_up_ship_location(rows):
	location = [str(random.randint(0, rows-1)), str(random.randint(0, rows-1))]
	return location

def printing_board(board):
	os.system("cls")
	for row in board:
		for item in row:
			print(item, end=" ")
		print() #kalau sudah selesai 1 baris

def check_user_input():
	user_input = input("Enter Ship Location: ").split(" ") 
	if my_ship == user_input:
		return True
	else:
		my_board[int(user_input[0])][int(user_input[1])] = " "
		return False

win = False
attempt = 1

my_board = setting_up_board(5)
my_ship = setting_up_ship_location(5)

while not win:
	printing_board(my_board)
	print(my_ship)
	win = check_user_input()
	if not win:
		attempt += 1

		if attempt == 11:
			print(f"KALAH ! (SUDAH SALAH NEBAK 10 KALI !!)")
			break

	elif win == True:
		print(f"SELAMAT ANDA MENANG DALAM {attempt} PERCOBAAN")
	


		



