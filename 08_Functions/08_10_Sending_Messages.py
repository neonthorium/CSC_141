def show_messages(messages):
    """Prints each message in the list."""
    print("Messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Simulates sending each message, until none are left.
    Moves each message to sent_messages after sending."""
    print("Sending messages...")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["Hello!", "How are you?", "Goodbye!"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal:")
print(messages)
print(sent_messages)