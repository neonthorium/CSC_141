favorite_numbers = {
    'alice': [8, 12, 16],
    'bob': [42, 7],
    'charlie': [3, 14, 15, 92],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"    {number}")