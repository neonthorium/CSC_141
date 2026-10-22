people = []

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}
people.append(person)

person = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}
people.append(person)

person = {
    'first_name': 'Michael',
    'last_name': 'Johnson',
    'age': 35,
    'city': 'Chicago'
}
people.append(person)

for person in people:
    name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"{name} of {city} is {age} years old.")