def make_car(manufacturer, model, **options):
    """Build a dictionary containing information about a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value
    return car_dict

my_mitsubishi = make_car('mitsubishi', 'outlander', color='blue', tow_package=True)
print(my_mitsubishi)

my_old_toyota = make_car('toyota', 'corolla', year=2010, color='red', sunroof=True)
print(my_old_toyota)