import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage
import random
from datetime import datetime
import re

greetings = ["Hello! How can I help you today? 🙂", 
             "Hi there! What can I do for you today?", 
             "Hey! How's it going?"]


farewells = ["Goodbye! Have a great day 👋", 
             "See you later! Take care!", 
             "Bye! Stay safe!"]


small_talk = ["I'm just a bot, but I'm doing well!", 
              "I’m here to chat with you! How are you?"]


jokes = [
    "Why did the computer show up at work late? It had a hard drive!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "I would tell you a UDP joke, but you might not get it."
]


def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return random.choice(greetings)

    # Asking about name
    elif re.search(r"\b(your name|who are you)\b", user_input):
        return "I’m a simple chatbot 🤖 created to chat with you."

    # Asking about well-being
    elif re.search(r"\b(how are you|how's it going)\b", user_input):
        return random.choice(small_talk)

    # Asking time
    elif re.search(r"\btime\b", user_input):
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}"

    # Asking date
    elif re.search(r"\bdate\b", user_input):
        today = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {today}"

    # Asking about weather
    elif re.search(r"\bweather\b", user_input):
        return "I can't check live weather yet 🌦️, but you can try a weather app."

    # Simple math queries
    elif re.search(r"\b(what is|whats|calculate|solve)\b", user_input):
        try:
            # Remove question words to get expression
            expression = re.sub(r'\b(what is|whats|calculate|solve)\b', '', user_input)
            expression = re.sub(r'[^0-9\+\-\*\/\.\(\)]', '', expression)
            result = eval(expression)
            return f"The answer is {result}"
        except:
            return "I couldn't solve that math problem 😅. Try a simpler one."

    # Asking for a joke
    elif re.search(r"\b(joke|funny)\b", user_input):
        return random.choice(jokes)

    # Farewell
    elif re.search(r"\b(bye|goodbye|see you)\b", user_input):
        return random.choice(farewells)

    # Default fallback
    else:
        return ("Sorry, I didn’t understand that 😕. "
                "You can ask me about time, date, weather, math, or even a joke!")


def send_message(event=None):
    user_msg = user_input.get()
    if user_msg.strip() != "":
        chat_window.config(state='normal')
        
        chat_window.insert(tk.END, "You: " + user_msg + "\n", "user")
     
        response = chatbot_response(user_msg)
        chat_window.insert(tk.END, "🤖 Chatbot: " + response + "\n\n", "bot")
        chat_window.config(state='disabled')
        chat_window.yview(tk.END)
        user_input.delete(0, tk.END)


root = tk.Tk()
root.title("🤖 Chatbot GUI")
root.geometry("550x650")
root.configure(bg="#f0f0f0")


chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, font=("Helvetica", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Tag colors
chat_window.tag_config("user", foreground="#1a73e8", font=("Helvetica", 12, "bold"))
chat_window.tag_config("bot", foreground="#e91e63", font=("Helvetica", 12))

# Input field
user_input = tk.Entry(root, font=("Helvetica", 14))
user_input.pack(padx=10, pady=(0,10), fill=tk.X)
user_input.focus()

# Send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Helvetica", 12), bg="#1a73e8", fg="white")
send_button.pack(padx=10, pady=(0,10))

root.bind('<Return>', send_message)

root.mainloop()
