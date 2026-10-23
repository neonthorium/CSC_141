prompt = "\nWhat games would you like to play?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    game = input(prompt)
    if game == 'quit':
        break
    else:
        print(f"\nI'll add {game} to your list of games.")