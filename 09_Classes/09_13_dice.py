from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, sides=6):
        """Initialize the die with a default of 6 sides."""
        self.sides = sides

    def roll_die(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.sides)

d6 = Die()  # Create a 6-sided die

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

d10 = Die(sides=10)  # Create a 10-sided die

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

d20 = Die(sides=20)  # Create a 20-sided die

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)