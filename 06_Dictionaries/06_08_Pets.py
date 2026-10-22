pets = []

pet = {
    'animal type': 'dog',
    'name': 'willie',
    'owner': 'john',
    'weight': 45,
    'eats': 'dirt'
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'whiskers',
    'owner': 'jane',
    'weight': 10,
    'eats': 'mice'
}
pets.append(pet)

pet = {
    'animal type': 'parrot',
    'name': 'polly',
    'owner': 'mike',
    'weight': 2,
    'eats': 'seeds'
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")