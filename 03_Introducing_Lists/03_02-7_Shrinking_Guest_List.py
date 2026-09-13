guest = ['Huff', 'Alice', 'Colin', 'Brian', 'Trisso', 'Cody']
print(f"\nHello {guest[0]}, I am sorry to inform you that I can only invite two guests to dinner. I apologize for the inconvenience, but I will have to remove you from the guest list.")
popped_guest = guest.pop(0)
print(f"\nHello {guest[0]}, I am sorry to inform you that I can only invite two guests to dinner. I apologize for the inconvenience, but I will have to remove you from the guest list.")
popped_guest_1 = guest.pop(0)
print(f"\nHello {guest[0]}, I am sorry to inform you that I can only invite two guests to dinner. I apologize for the inconvenience, but I will have to remove you from the guest list.")
popped_guest_2 = guest.pop(0)
print(f"\nHello {guest[0]}, I am sorry to inform you that I can only invite two guests to dinner. I apologize for the inconvenience, but I will have to remove you from the guest list.")
popped_guest_3 = guest.pop(0)
print(f"\nHello {guest[0]}, you are still invited to dinner.")
print(f"Hello {guest[1]}, you are still invited to dinner.")
print(f"Number of guests invited: {len(guest)}")
del guest[1]
del guest[0]
print(guest)
#3-8 Try it yourself included in the file.