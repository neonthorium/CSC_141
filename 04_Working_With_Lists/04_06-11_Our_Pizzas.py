pizzas = ['pepperoni', 'anchovies', 'mushroom', 'canadian bacon', 'sausage']
friend_pizzas = pizzas[:]

pizzas.append('cocktail')
friend_pizzas.append('mexican')

print("My favorite pizzas are:")
for value in pizzas:
    print(value.title())
print("\nMy friend's favorite pizzas are:")
for value in friend_pizzas:
    print(value.title())