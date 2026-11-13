from user import Admin
#This also would not import from files with numbers in the name
todd = Admin('todd', 'tiger', 't_tiger', 't_tiger@example.com', 'tigerland')
todd.describe_user()

todd_privileges = ['can add post', 'can delete post', 'can ban user']
todd.privileges.privileges = todd_privileges

print(f"\nThis admin {todd.username} has the following privileges:")
todd.privileges.show_privileges()