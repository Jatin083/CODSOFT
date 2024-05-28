import re
import random

# This define a dictionary of responses
responses = {
    'greeting': [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Hey! How's it going?",
        "Greetings! How may I help you?"
    ],
    'farewell': [
        "Goodbye! Have a great day!",
        "See you later!",
        "Take care!",
        "Bye! Come back if you have more questions."
    ],
    'how_are_you': [
        "I'm just a bot created by Jatin, but I'm here to help you!",
        "Doing great! How about you?",
        "I don't have feelings, but I'm ready to assist you!",
        "I'm functioning as expected. How can I help?"
    ],
    'name': [
        "I am a simple chatbot created by Jatin.",
        "You can call me ChatBot.",
        "I'm ChatBot, your virtual assistant.",
        "My name is ChatBot. How can I assist you?"
    ],
    'weather': [
        "I can't provide weather updates at the moment, but you can check a weather website.",
        "Sorry, I can't check the weather right now.",
        "It's always a good idea to check a reliable weather service.",
        "I don't have weather information, but I can help with other questions."
    ],
    'help': [
        "I'm here to help! You can ask me about the weather, my name, or how I'm doing.",
        "Feel free to ask me anything about weather, my identity, or my well-being.",
        "I can help with questions about myself or general information. What do you need?",
        "I'm available to answer questions about weather, my name, or general help."
    ],
    'unknown': [
        "I'm not sure how to respond to that. Can you please rephrase?",
        "Sorry, I didn't understand that. Can you ask in a different way?",
        "I'm not sure what you mean. Can you clarify?",
        "I didn't catch that. Could you say it again in a different way?"
    ]
}

# Function to get a response based on the category
def get_response(category):
    return random.choice(responses[category])

# Function to determine the category based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r'\b(hello|hi|hey)\b', user_input):
        return get_response('greeting')
    elif re.search(r'\b(bye|goodbye)\b', user_input):
        return get_response('farewell')
    elif re.search(r'\bhow are you\b', user_input):
        return get_response('how_are_you')
    elif re.search(r'\bwhat is your name\b', user_input):
        return get_response('name')
    elif re.search(r'\bweather\b', user_input):
        return get_response('weather')
    elif re.search(r'\bhelp\b', user_input):
        return get_response('help')
    else:
        return get_response('unknown')

# Chat loop
print("Chatbot: Hello! Type 'bye' to end the conversation.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    if re.search(r'\b(bye|goodbye)\b', user_input):
        break
