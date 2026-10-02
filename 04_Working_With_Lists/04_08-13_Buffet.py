foods = ('sushi', 'tacos', 'pizza', 'sandwhiches', 'popcorn')
print("Menu: Today's meal options:")
for food in foods:
    print(food.title())
#foods[2] = 'cake' does not work, tuple object does not support item assignment
foods = ('sushi', 'tacos', 'donuts', 'pizza', 'crab', 'popcorn')
print("\nModified Menu:")
for food in foods:
    print(food.title())