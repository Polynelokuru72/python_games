# chatbot.py

def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "how are you": "I'm just a program, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "what is your name": "I'm ChatBot, your friendly assistant!",
        "help": "I'm here to assist you. Try asking me questions!"
    }
    # The `get` method returns a default message if the user input doesn't match any key
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

def main():
    print("Welcome to the ChatBot! Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            # Respond and break the loop to end the conversation
            print("Bot:", chatbot_response(user_input))
            break
        
        # Respond to the user
        print("Bot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()
