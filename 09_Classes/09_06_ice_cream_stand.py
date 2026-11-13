class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves amazing {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        msg = f"{self.name} is now open!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Increment the number of customers served."""
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

big_boy = IceCreamStand('Big Boy')
big_boy.flavors = ['vanilla', 'chocolate', 'strawberry']

big_boy.describe_restaurant()
big_boy.display_flavors()