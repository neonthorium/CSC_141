class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        msg = f"{self.name} is now open!"
        print(f"\n{msg}")

the_southwest_adventure = Restaurant("The Southwest Adventure", "Cajun cuisine")
the_southwest_adventure.describe_restaurant()

thai_delight = Restaurant("Thai Delight", "Thai cuisine")
thai_delight.describe_restaurant()

happy_cow = Restaurant("Happy Cow", "Vegetarian cuisine")
happy_cow.describe_restaurant()