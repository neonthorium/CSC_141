def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'm gonna make you a fantastic sandwich!")
    for item in items:
        print(f"    . . .adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('ham', 'cheese', 'lettuce', 'tomato')
make_sandwich('turkey', 'bacon', 'avocado')
make_sandwich('peanut butter', 'jelly')