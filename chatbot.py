print("===== BASIC CHATBOT =====")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! Nice to meet you.")
    elif user == "how are you":
        print("Bot: I'm fine, thank you.")
    elif user == "what is your name":
        print("Bot: I am CodeAlpha Chatbot.")
    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: Sorry, I don't understand.")