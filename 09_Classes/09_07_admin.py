class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")
    
    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

class Admin(User):
    """Represent an admin user."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin user."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges of the admin user."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

sammy = Admin('sammy', 'swiss', 's_swiss', 's_swiss@example.com', 'switzerland')
sammy.describe_user()

sammy.privileges = ['can modify post', 'can delete post', 'can ban user']

sammy.show_privileges()