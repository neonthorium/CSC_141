class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        msg = f"{self.name} is now open!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Add the given amount to the number of customers served."""
        self.number_served += additional_served

restaurant = Restaurant("The Southwest Adventure", "Cajun cuisine")
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 5
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(10)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(509)
print(f"Number served: {restaurant.number_served}")