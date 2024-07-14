import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Define patterns and responses for the chatbot
pairs = [
    ("hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    ("how are you?", ["I'm good,What about you?" , "superb, you?", "I'm doing well, how are you?."]),
    ("your name?", ["I am a chatbot.", "You can call me Chatbot."]),
    ("i am good",["good to hear"]),
    ("what is your purpose?", ["I'm here to assist you and have conversations."]),
    ("bye|goodbye", ["Goodbye!", "See you later.", "Bye!"]),
    # You can add more patterns and responses here
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Start chatting
print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
