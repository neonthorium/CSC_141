guest = ["Alice", "Brian", "Trisso"]
print(guest)

guest.insert(0, "Huff")
guest.insert(2, "Colin")
guest.append("Cody")
print(guest)
print(f"\nHello {guest[0]}, would you like to come to dinner with me?")
print(f"Hello {guest[1]}, would you like to come to dinner with me?")
print(f"Hello {guest[2]}, would you like to come to dinner with me?")
print(f"Hello {guest[3]}, would you like to come to dinner with me?")
print(f"Hello {guest[4]}, would you like to come to dinner with me?")
print(f"Hello {guest[5]}, would you like to come to dinner with me?")

print(f"\nHello {guest[1]}, I have found a bigger dinner table, so I would like to invite more guests to dinner. I've sent you a new invitation, so please let me know if you can make it to dinner.")
print(f"Hello {guest[3]}, I have found a bigger dinner table, so I would like to invite more guests to dinner. I've sent you a new invitation, so please let me know if you can make it to dinner.")
print(f"Hello {guest[4]}, I have found a bigger dinner table, so I would like to invite more guests to dinner. I've sent you a new invitation, so please let me know if you can make it to dinner.")
print(f"Number of guests invited: {len(guest)}")
#3-8 Try it yourself included in the file.