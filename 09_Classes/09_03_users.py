class User:
    """A simple attempt to represent a user."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user's attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\nUser: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nHello, {self.username}! Welcome back.")

tom = User('tom', 'smith', 'tsmith', 'tsmith@example.com', 'new york')
tom.describe_user()
tom.greet_user()

jane = User('jane', 'doe', 'jdoe', 'jdoe@example.com', 'los angeles')
jane.describe_user()
jane.greet_user()