cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars.sort()
print(f"\n{cars}")
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\n{cars}")
cars.reverse()
print(cars)
print(len(cars))
print(f"Number of cars in the list: {len(cars)}")