guest = ["Alice", "Brian", "Trisso"]
popped_guest = guest.pop(0)
guest.append("Huff")
print(guest)
print(f"\nHello {guest[0]}, would you like to come to dinner with me?")
print(f"Hello {guest[1]}, would you like to come to dinner with me?")
print(f"Hello {guest[2]}, would you like to come to dinner with me?")
print(f"\n{popped_guest} could not make it to dinner.")
print(f"Number of guests invited: {len(guest)}")
#3-8 Try it yourself included in the file.