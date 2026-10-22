cities = {
    'new york': {
        'country': 'usa',
        'population': 8_419_600,
        'township': 'manhattan'
    },
    'london': {
        'country': 'uk',
        'population': 9_426_700,
        'township': 'city of london'
    },
    'tokyo': {
        'country': 'japan',
        'population': 13_929_286,
        'township': 'shibuya'
    }
}
for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    township = city_info['township']

    print(f"\n{city.title()} is in {country.title()}.")
    print(f"It has a population of about {population}.")
    print(f"The township is {township.title()}.")