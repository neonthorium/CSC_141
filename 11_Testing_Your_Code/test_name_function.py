from name_functions import get_formatted_name

def test_first_last_name():
    """Name test"""
    formatted_name = get_formatted_name('Tom', 'Smith')
    assert formatted_name == 'Tom Smith'

def test_first_last_middle_name():
    """Names with middle names test"""
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'