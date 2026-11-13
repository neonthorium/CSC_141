from my_admin import Admin

sandy = Admin('sandy', 'smith', 's_smith', 'sandy_smith@example.com', 'new york')
sandy.describe_user()

sandy_privileges = ['can add post', 'can delete post', 'can ban user']
sandy.privileges.privileges = sandy_privileges

print(f"\nThis admin {sandy.username} has the following privileges:")
sandy.privileges.show_privileges()