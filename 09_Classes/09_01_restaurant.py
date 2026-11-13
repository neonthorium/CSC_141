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

restaurant = Restaurant("The Southwest Adventure", "Cajun cuisine")
print(f"\n{restaurant.name}")
print(f"{restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()