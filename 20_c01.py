a = 0
s = 0
print('Enter Numbers to add to the sum.')
print('Enter q to quit.')
#while a != "q" and a != "Q": (sama dengan baris 7)
#while str(a).lower() != "q": (sama dengan baris 7)
while a != "q": 
	s = s + float(a)     
	print('Current Sum:', s)            
	a = input('Number? ')        
                              
print('Total Sum =', s)
