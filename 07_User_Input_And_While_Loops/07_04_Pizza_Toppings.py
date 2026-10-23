prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"\nI'll add {topping} to your pizza.")