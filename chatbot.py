import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I help you today? 🙂"

    # Asking about name
    elif "your name" in user_input:
        return "I’m a simple chatbot 🤖 created to chat with you."

    # Asking about well-being
    elif "how are you" in user_input:
        return "I’m doing great, thanks for asking! How about you?"

    # Asking time
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}"

    # Asking date
    elif "date" in user_input:
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {today}"

    # Asking about weather
    elif "weather" in user_input:
        return "I can’t check live weather yet 🌦️, but you can use a weather app."

    # Goodbye
    elif re.search(r"\b(bye|goodbye|see you)\b", user_input):
        return "Goodbye! Have a great day 👋"

    # Default fallback
    else:
        return "Sorry, I didn’t understand that. Can you rephrase?"

def run_chatbot():
    print("🤖 Chatbot is running! (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! 👋")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    run_chatbot()
