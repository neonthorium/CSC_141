my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for value in my_foods:
    print(value.title())

print("\nMy friend's favorite foods are:")
for value in friend_foods:
    print(value.title())