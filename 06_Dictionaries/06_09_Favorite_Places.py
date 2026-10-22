favorite_places = {
    'jen': ['paris', 'tokyo', 'new york'],
    'sarah': ['london', 'berlin', 'amsterdam'],
    'david': ['sydney', 'tokyo', 'paris']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")