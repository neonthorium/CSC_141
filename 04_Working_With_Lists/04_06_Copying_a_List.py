my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
#doing 'friend_foods = my_foods' makes it all one list when in the end we want two separate lists

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)