def make_shirt(size='Large', message='I love Python'):
    """Display the size that's going to be made."""
    print(f"\nThe size of the shirt is {size}.")
    print(f"It says '{message}'.")

make_shirt()
make_shirt(size='Medium')
make_shirt(size='Small', message='I love coding')