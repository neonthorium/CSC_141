from user_admin import User

class Admin(User):
    """Represent an admin user."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin user."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

class Privileges:
    """Represent privileges of an admin user."""
    def __init__(self, privileges=[]):
        """Initialize the privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges of the admin user."""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")