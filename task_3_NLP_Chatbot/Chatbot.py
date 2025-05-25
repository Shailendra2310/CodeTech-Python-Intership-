# Task 3 - Simple Chatbot using NLTK

import nltk
import random
from nltk.chat.util import Chat, reflections

# Sample chatbot pairs
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["what is your name?", ["I am a chatbot created by Shailendra."]],
    ["how are you?", ["I'm doing well, thank you!", "All good here."]],
    ["what can you do?", ["I can answer basic questions."]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Bye!"]],
    ["(.*)", ["Sorry, I didn't understand that. Can you rephrase?"]]
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Start chatting
print("Hello! I'm your chatbot. Type 'bye' to exit.")
chatbot.converse()
