# def city_country(city, country):
#     """Return string"""
#     return f"{city.title()}, {country.title()}"

def city_country(city, country, population):
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" - population {population}"
    return output_string