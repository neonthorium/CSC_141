motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('harley-davidson')
print(motorcycles)

motorcycles_1 = []
motorcycles_1.append('honda')
motorcycles_1.append('yamaha')
motorcycles_1.append('suzuki')
print(motorcycles_1)
#We've created a seperate list to demonstrate the append() method.

motorcycles_2 = ['honda', 'yamaha', 'suzuki']
motorcycles_2.insert(0, 'ducati')
print(motorcycles_2)

motorcycles_3 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_3)

del motorcycles_3[0]
print(motorcycles_3)
#This section removes the first item in the third list, which is 'honda'.

del motorcycles[1]
print(motorcycles)
#This section revisits the first list and removes the second item in the list, which is 'yamaha'.

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

last_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'bmw']
too_expensive = 'bmw'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")