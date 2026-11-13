from random import choice

def get_winning_ticket(possibilities):
    """Return a random winning ticket from the list of possibilities."""
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket

def check_ticket(user_ticket, winning_ticket):
    """Check if the user's ticket matches the winning ticket."""
    for element in user_ticket:
        if element not in winning_ticket:
            return False

    return True

def make_random_ticket(possibilities):
    """Return a random ticket from the list of possibilities."""
    ticket = []
    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket

possibilities = [1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

max_tries = 1000000  # Set a maximum number of tries to prevent infinite loops

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        print(f"Reached maximum tries ({max_tries}) without winning.")
        break

if won:
    print(f"\nWinning ticket: {winning_ticket}")
    print(f"Your ticket: {new_ticket}")
    print(f"You won after {plays} plays!")
else:
    print(f"\nWinning ticket: {winning_ticket}")
    print(f"You did not win after {plays} plays.")