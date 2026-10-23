def describe_city(city, country='Mexico'):
    """Display information about a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Mexico City')
describe_city('Vancouver', 'Canada')
describe_city('Monterrey')