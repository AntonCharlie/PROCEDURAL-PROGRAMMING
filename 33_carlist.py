#Changing - Adding - Removing Elements

motors = ['honda', 'yamaha', 'suzuki']
#			0		  1		     2
print(motors)


#Changing / Modifying
motors[1] = 'ducati'
print(motors)


#Adding Element
motors.append('kawasaki')  #ujung list
print(motors)

#Insert Element
motors.insert(0, 'bmw')
print(motors)


motors.insert(3, 'kaisar')
print(motors)


#Removing Element
motors.pop(3)#argumen diisi dengan index element
print(motors)

motors.remove('honda')#argumen diisi dengan value element
print(motors)

del motors[-1]
print(motors)