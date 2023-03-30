
my_foods = ['pizza', 'combro', 'ongol ongol']

my_fav_food = my_foods[1:3]

print(my_foods, "\n", my_fav_food)

#my_friend_foods = my_foods # alias : mereferensikan data
my_friend_foods = my_foods[:]

#print(my_friend_foods)
my_friend_foods.append("burger")
print(my_friend_foods)

print(my_foods)