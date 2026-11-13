from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f']

winning_ticket = []
print("Winning ticket numbers:")

while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)
    if pulled_item not in winning_ticket:
        print(f"We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)

print(f"\nWinning ticket: {winning_ticket}")