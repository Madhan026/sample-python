# Simple Chatbot using basic NLP

# Step 1: Dictionary of possible responses
responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What can I do for you today?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "thank you": "You're welcome!",
    "what is your name": "I’m a simple chatbot created using Python.",
    "help": "I can answer greetings and some basic questions."
}

# Step 2: Preprocess input for matching
def preprocess(text):
    return text.lower().strip()

# Step 3: Chat loop
print("mybot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    user_input = preprocess(user_input)

    if user_input == "bye":
        print("mybot: Goodbye! Talk to you later.")
        break

    found = False
    for key in responses:
        if key in user_input:
            print("mybot:", responses[key])
            found = True
            break

    if not found:
        print("mytbot: I'm not sure how to respond to that.")
