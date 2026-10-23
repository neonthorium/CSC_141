sandwich_orders = [
    'pastrami', 'grilled cheese', 'pastrami',
    'turkey', 'ham', 'pastrami', 'roast beef', 'veggie'
]
finished_sandwiches = []

print("I'm sorry, but we have run out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nI'm making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"\nI made a {sandwich} sandwich.")